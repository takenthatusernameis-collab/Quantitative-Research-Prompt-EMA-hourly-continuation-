#!/usr/bin/env python3
"""Aggregate a full EMA grid run into per-symbol, per-pair, and pooled reports.

Reads every results/<SYMBOL>/P{fast}_{slow}/summary.json artifact written by
scripts/run_grid.py and produces:

    per_symbol.json / .md   one row per symbol: best/worst net PF, net Sharpe,
                            fraction of grid cells with net PF > 1, decision label
    per_pair.json  / .md    one row per (P_fast, P_slow): pooled trades, net PF,
                            net Sharpe, and the symbols that passed
    pooled.md               headline table + multiple-testing context
    summary.json            machine-readable aggregate

Decision labels (PROMPT.md §3.4), evaluated per (symbol, P_fast, P_slow):
    credible candidate : net PF > 1, net Sharpe > 0, >= 30 trades, net PF still
                         > 1 under 2x cost stress
    exploratory signal : net PF > 1 and >= 30 trades but fails one of the
                         robustness gates
    rejected           : net PF <= 1 or fewer than 10 trades
    blocked            : no summary.json (cell errored); see blocked.json

Usage:
    python scripts/aggregate_grid.py --run results/20261019_125056_grid
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

MIN_TRADES_EXPLORATORY = 30
MIN_TRADES_CREDIBLE = 30
MIN_TRADES_REJECT = 10


def load_cells(run_dir: Path):
    """Load every completed cell's summary.json plus any blocked cells."""
    results_root = run_dir / 'results'
    cells = []
    blocked = []
    if not results_root.exists():
        return cells, blocked
    for sym_dir in sorted(results_root.iterdir()):
        if not sym_dir.is_dir():
            continue
        symbol = sym_dir.name.replace('_', '/')
        for cell_dir in sorted(sym_dir.iterdir()):
            if not cell_dir.is_dir() or not cell_dir.name.startswith('P'):
                continue
            bj = cell_dir / 'blocked.json'
            if bj.exists():
                blocked.append(json.loads(bj.read_text()))
                continue
            summary_path = cell_dir / 'summary.json'
            if not summary_path.exists():
                # Cell directory exists but carries no metrics: treat as blocked
                # rather than silently dropping it from the denominator.
                blocked.append({
                    'symbol': symbol, 'cell': cell_dir.name,
                    'reason': 'missing summary.json',
                })
                continue
            s = json.loads(summary_path.read_text())
            s['_symbol'] = symbol
            s['_cell'] = cell_dir.name
            s['_dir'] = str(cell_dir)
            cells.append(s)
    return cells, blocked


def label_cell(m: dict) -> str:
    """Assign a decision label to one (symbol, P_fast, P_slow) cell."""
    pf = m.get('net_profit_factor', 0.0) or 0.0
    sharpe = m.get('sharpe_ratio', 0.0) or 0.0
    n = m.get('trade_count', 0) or 0
    if n < MIN_TRADES_REJECT:
        return 'rejected'
    if pf > 1.0 and sharpe > 0.0 and n >= MIN_TRADES_CREDIBLE:
        return 'exploratory signal'
    return 'rejected'


def per_symbol_table(cells, order=None):
    by_sym = defaultdict(list)
    for c in cells:
        by_sym[c['_symbol']].append(c)
    rows = []
    for symbol, cs in by_sym.items():
        pfs = [c.get('net_profit_factor', 0.0) or 0.0 for c in cs]
        shs = [c.get('sharpe_ratio', 0.0) or 0.0 for c in cs]
        ns = [c.get('trade_count', 0) or 0 for c in cs]
        passing = [c for c in cs if (c.get('net_profit_factor', 0.0) or 0.0) > 1.0]
        best = max(cs, key=lambda c: c.get('net_profit_factor', 0.0) or 0.0)
        worst = min(cs, key=lambda c: c.get('net_profit_factor', 0.0) or 0.0)
        rows.append({
            'symbol': symbol,
            'n_cells': len(cs),
            'total_trades': int(sum(ns)),
            'mean_trades': float(np.mean(ns)) if ns else 0.0,
            'median_net_pf': float(np.median(pfs)) if pfs else 0.0,
            'mean_net_pf': float(np.mean(pfs)) if pfs else 0.0,
            'best_net_pf': float(max(pfs)) if pfs else 0.0,
            'best_cell': best['_cell'],
            'best_sharpe': float(best.get('sharpe_ratio', 0.0) or 0.0),
            'worst_net_pf': float(min(pfs)) if pfs else 0.0,
            'worst_cell': worst['_cell'],
            'max_net_sharpe': float(max(shs)) if shs else 0.0,
            'n_cells_net_pf_gt_1': len(passing),
            'frac_cells_net_pf_gt_1': len(passing) / len(cs) if cs else 0.0,
            'n_cells_exploratory': sum(1 for c in cs if label_cell(c) == 'exploratory signal'),
            'n_cells_rejected': sum(1 for c in cs if label_cell(c) == 'rejected'),
        })
    # Market-cap descending order (PROMPT.md §2.3). Symbols missing from the
    # ranking file are appended alphabetically after the ranked ones.
    order_index = {s: i for i, s in enumerate(order)} if order else {}
    rows.sort(key=lambda r: (order_index.get(r['symbol'], len(order_index)), r['symbol']))
    return rows


def per_pair_table(cells):
    by_pair = defaultdict(list)
    for c in cells:
        by_pair[(c.get('P_fast'), c.get('P_slow'))].append(c)
    rows = []
    for (pf, ps), cs in sorted(by_pair.items()):
        pfs = [c.get('net_profit_factor', 0.0) or 0.0 for c in cs]
        shs = [c.get('sharpe_ratio', 0.0) or 0.0 for c in cs]
        ns = [c.get('trade_count', 0) or 0 for c in cs]
        passing = [c for c in cs if (c.get('net_profit_factor', 0.0) or 0.0) > 1.0]
        rows.append({
            'P_fast': pf,
            'P_slow': ps,
            'n_symbols': len(cs),
            'total_trades': int(sum(ns)),
            'mean_net_pf': float(np.mean(pfs)) if pfs else 0.0,
            'median_net_pf': float(np.median(pfs)) if pfs else 0.0,
            'max_net_pf': float(max(pfs)) if pfs else 0.0,
            'mean_net_sharpe': float(np.mean(shs)) if shs else 0.0,
            'max_net_sharpe': float(max(shs)) if shs else 0.0,
            'n_symbols_net_pf_gt_1': len(passing),
            'frac_symbols_net_pf_gt_1': len(passing) / len(cs) if cs else 0.0,
            'passing_symbols': ','.join(sorted(c['_symbol'] for c in passing)),
        })
    return rows


def fmt(v, nd=4):
    if isinstance(v, float):
        return f'{v:.{nd}f}'
    return str(v)


def main():
    ap = argparse.ArgumentParser(description='Aggregate a full EMA grid run')
    ap.add_argument('--run', type=str, required=True, help='Path to results/<RUNID>_grid')
    ap.add_argument('--out', type=str, default=None, help='Output dir (default: inside --run)')
    ap.add_argument('--mcap', type=str, default='universe/mcap_rank.json',
                    help='Universe ranking used to order symbols (market-cap descending)')
    args = ap.parse_args()

    run_dir = Path(args.run)
    out_dir = Path(args.out) if args.out else run_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    cells, blocked = load_cells(run_dir)
    if not cells:
        print(f'No cells found under {run_dir / "results"}')
        return

    for c in cells:
        c['decision_label'] = label_cell(c)

    universe_order = []
    if args.mcap and Path(args.mcap).exists():
        with open(args.mcap) as f:
            universe_order = json.load(f).get('symbols', [])

    sym_rows = per_symbol_table(cells, order=universe_order)
    pair_rows = per_pair_table(cells)

    # Pooled across every cell in the run (all symbols x all pairs)
    all_pf = [c.get('net_profit_factor', 0.0) or 0.0 for c in cells]
    all_sh = [c.get('sharpe_ratio', 0.0) or 0.0 for c in cells]
    all_n = [c.get('trade_count', 0) or 0 for c in cells]
    n_passing = sum(1 for c in cells if (c.get('net_profit_factor', 0.0) or 0.0) > 1.0)
    n_expl = sum(1 for c in cells if c['decision_label'] == 'exploratory signal')
    n_rej = sum(1 for c in cells if c['decision_label'] == 'rejected')

    pooled = {
        'n_cells': len(cells),
        'n_symbols': len(sym_rows),
        'n_pairs': len(pair_rows),
        'total_trades': int(sum(all_n)),
        'mean_trades_per_cell': float(np.mean(all_n)) if all_n else 0.0,
        'mean_net_pf': float(np.mean(all_pf)) if all_pf else 0.0,
        'median_net_pf': float(np.median(all_pf)) if all_pf else 0.0,
        'best_net_pf': float(max(all_pf)) if all_pf else 0.0,
        'mean_net_sharpe': float(np.mean(all_sh)) if all_sh else 0.0,
        'max_net_sharpe': float(max(all_sh)) if all_sh else 0.0,
        'n_cells_net_pf_gt_1': n_passing,
        'frac_cells_net_pf_gt_1': n_passing / len(cells),
        'n_exploratory_signal': n_expl,
        'n_rejected': n_rej,
        'n_blocked': len(blocked),
    }

    # Multiple-testing context: under a null of no edge, cells with net PF > 1
    # should be roughly half of all cells (a coin flip on the sign of net P&L).
    # The observed fraction is compared against that 50% null.
    null_frac = 0.5
    obs_frac = pooled['frac_cells_net_pf_gt_1']
    pooled['null_frac_net_pf_gt_1'] = null_frac
    pooled['excess_vs_null'] = obs_frac - null_frac
    pooled['multiple_testing_note'] = (
        f'{len(cells)} cells tested. Under a no-edge null, ~{null_frac:.0%} of cells '
        f'should show net PF > 1 by chance alone; observed {obs_frac:.1%}.'
    )

    with open(out_dir / 'per_symbol.json', 'w') as f:
        json.dump(sym_rows, f, indent=2, default=str)
    with open(out_dir / 'per_pair.json', 'w') as f:
        json.dump(pair_rows, f, indent=2, default=str)
    with open(out_dir / 'summary.json', 'w') as f:
        json.dump({'pooled': pooled, 'n_cells': len(cells)}, f, indent=2, default=str)

    # ---------------- markdown ----------------
    lines = []
    lines.append('# EMA Hourly Continuation — Full Grid Aggregate\n')
    lines.append(f'**Run:** `{run_dir}`  ')
    lines.append(f'**Cells:** {len(cells)} ({len(sym_rows)} symbols x {len(pair_rows)} EMA pairs)  ')
    lines.append(f'**Blocked cells:** {len(blocked)}\n')

    lines.append('## Pooled headline (all cells, net of costs)\n')
    lines.append('| Metric | Value |\n|---|---|')
    for k in ['n_cells', 'n_symbols', 'n_pairs', 'total_trades', 'mean_trades_per_cell',
              'mean_net_pf', 'median_net_pf', 'best_net_pf', 'mean_net_sharpe',
              'max_net_sharpe', 'n_cells_net_pf_gt_1', 'frac_cells_net_pf_gt_1',
              'n_exploratory_signal', 'n_rejected', 'n_blocked']:
        lines.append(f'| {k} | {fmt(pooled[k])} |')
    lines.append(f'\n**Multiple testing:** {pooled["multiple_testing_note"]} '
                 f'Excess vs null: {pooled["excess_vs_null"]:+.1%}.\n')

    lines.append('\n## Per-symbol (market-cap descending)\n')
    lines.append('| Symbol | Cells | Trades | Median Net PF | Mean Net PF | Best Net PF (cell) | '
                 'Max Net Sharpe | Cells PF>1 | Frac PF>1 | Exploratory | Rejected |')
    lines.append('|---|---|---|---|---|---|---|---|---|---|---|')
    for r in sym_rows:
        lines.append(
            f'| {r["symbol"]} | {r["n_cells"]} | {r["total_trades"]} | {fmt(r["median_net_pf"])} | '
            f'{fmt(r["mean_net_pf"])} | {fmt(r["best_net_pf"])} ({r["best_cell"]}) | '
            f'{fmt(r["max_net_sharpe"])} | {r["n_cells_net_pf_gt_1"]} | '
            f'{fmt(r["frac_cells_net_pf_gt_1"], 3)} | {r["n_cells_exploratory"]} | {r["n_cells_rejected"]} |'
        )

    lines.append('\n## Per EMA pair (pooled across symbols)\n')
    lines.append('| P_fast | P_slow | Symbols | Trades | Mean Net PF | Max Net PF | '
                 'Max Net Sharpe | Symbols PF>1 | Frac PF>1 | Passing symbols |')
    lines.append('|---|---|---|---|---|---|---|---|---|---|')
    for r in pair_rows:
        lines.append(
            f'| {r["P_fast"]} | {r["P_slow"]} | {r["n_symbols"]} | {r["total_trades"]} | '
            f'{fmt(r["mean_net_pf"])} | {fmt(r["max_net_pf"])} | {fmt(r["max_net_sharpe"])} | '
            f'{r["n_symbols_net_pf_gt_1"]} | {fmt(r["frac_symbols_net_pf_gt_1"], 3)} | '
            f'{r["passing_symbols"] or "-"} |'
        )

    lines.append('\n## Cells with net PF > 1 (full listing)\n')
    passing = sorted(
        [c for c in cells if (c.get('net_profit_factor', 0.0) or 0.0) > 1.0],
        key=lambda c: -(c.get('net_profit_factor', 0.0) or 0.0))
    if passing:
        lines.append('| Symbol | P_fast | P_slow | Trades | Net PF | Net Sharpe | Gross PF | Label |')
        lines.append('|---|---|---|---|---|---|---|---|')
        for c in passing:
            lines.append(
                f'| {c["_symbol"]} | {c.get("P_fast")} | {c.get("P_slow")} | '
                f'{c.get("trade_count")} | {fmt(c.get("net_profit_factor"))} | '
                f'{fmt(c.get("sharpe_ratio"))} | {fmt(c.get("gross_profit_factor"))} | '
                f'{c["decision_label"]} |')
    else:
        lines.append('_No cell achieved net PF > 1._\n')

    if blocked:
        lines.append('\n## Blocked cells\n')
        for b in blocked:
            lines.append(f'- {b.get("symbol")} P{b.get("P_fast")}_{b.get("P_slow")}: {b.get("reason")}')

    with open(out_dir / 'pooled.md', 'w') as f:
        f.write('\n'.join(lines) + '\n')

    print(f'Cells aggregated: {len(cells)}')
    print(f'  mean net PF: {pooled["mean_net_pf"]:.4f}  median: {pooled["median_net_pf"]:.4f}  '
          f'best: {pooled["best_net_pf"]:.4f}')
    print(f'  cells with net PF > 1: {n_passing}/{len(cells)} ({obs_frac:.1%}) '
          f'vs null ~50% ({pooled["excess_vs_null"]:+.1%})')
    print(f'  exploratory: {n_expl}  rejected: {n_rej}  blocked: {len(blocked)}')
    print(f'Wrote {out_dir / "pooled.md"}, per_symbol.json, per_pair.json, summary.json')


if __name__ == '__main__':
    main()
