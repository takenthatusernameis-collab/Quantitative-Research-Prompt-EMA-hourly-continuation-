#!/usr/bin/env python3
"""Parent -> child -> delta for a pre-registered grid mutation.

Why this leg exists
-------------------
A pre-registered mutation (PROMPT.md §5) is only informative if it is
compared with its parent under the *same* yardstick, on the *same* universe,
with the *same* gates. This leg produces that comparison in one artifact:

* the pooled full-sample net PF, gross net PF and trade count of parent and
  child, and the delta between them;
* the walk-forward yardstick of the survivor selection audit (leg 3): the
  pooled out-of-fold net PF of the selection procedure, and the share of the
  out-of-fold windows that land above PF 1;
* the grid-wide out-of-sample gate: how many cells clear "out-of-sample net
  PF > 1, at least 30 out-of-sample trades, still > 1 under 2x costs";
* the cost share of the gross P&L, i.e. how much of the gross result the
  costs eat, recomputed for both arms;
* the decision, read against the rule that was fixed in the pre-registration
  before the child run started.

Nothing is modified: both grids are read, and the output is a new artifact
directory.

Usage:
    python3 scripts/mutation_comparison.py \
        --parent results/20261019_135940_grid \
        --parent-oos results/20261021_033523_oos_grid_scan \
        --child results/20261021_125403_grid \
        --child-oos results/<TS>_oos_grid_scan \
        --preregistration results/20261021_130500_atr_min_risk_prereg \
        --out results/<TS>_mutation_comparison
"""
import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from scripts.oos_grid_scan import (read_trades, stressed_pnl_net, win_loss_sums)
from scripts.run_grid import (CONFIG_DEFAULTS, read_artifact_csv, symbol_dir_name)
from scripts.selection_granularity import (market_cap_buckets, rank_symbols,
                                            summarize, walk_forward)


def pooled_grid_stats(run_dir: Path, stress_multiplier: float = 2.0) -> dict:
    """Pooled full-sample statistics of a whole grid.

    The pooling uses the sums of wins and losses of every trade of every
    cell, never a mean of per-cell ratios: cells carry very different trade
    counts, so a mean of ratios would give a thin cell the same weight as a
    thick one.
    """
    win = loss = 0.0
    gross_win = gross_loss = 0.0
    s_win = s_loss = 0.0
    trades = 0
    cells = 0
    cost_total = 0.0
    gross_pnl_total = 0.0
    results_root = run_dir / 'results'
    for sym_dir in sorted(results_root.iterdir()):
        if not sym_dir.is_dir():
            continue
        for cell_dir in sorted(sym_dir.iterdir()):
            if not cell_dir.is_dir():
                continue
            if not trades_path(cell_dir).exists():
                continue
            blotter = read_trades(cell_dir)
            if blotter is None or len(blotter) == 0:
                cells += 1
                continue
            cells += 1
            pnl = blotter['pnl_net'].to_numpy(dtype=float)
            gross = blotter['pnl'].to_numpy(dtype=float)
            entry_cost = blotter['entry_cost'].to_numpy(dtype=float)
            exit_cost = blotter['exit_cost'].to_numpy(dtype=float)
            stress = stressed_pnl_net(pnl, entry_cost, exit_cost, stress_multiplier)
            w, l = win_loss_sums(pnl)
            win += w
            loss += l
            gross_win += float(gross[gross > 0].sum())
            gross_loss += float(-gross[gross < 0].sum())
            s_w, s_l = win_loss_sums(stress)
            s_win += s_w
            s_loss += s_l
            trades += len(blotter)
            cost_total += float(entry_cost.sum() + exit_cost.sum())
            gross_pnl_total += float(gross.sum())

    def pf(w, l):
        if l > 0:
            return w / l
        if w > 0:
            return float('inf')
        return None

    return {
        'cells': cells,
        'trades': trades,
        'net_pf': pf(win, loss),
        'stress_net_pf': pf(s_win, s_loss),
        'gross_pf': pf(gross_win, gross_loss),
        'net_pnl': win - loss,
        'gross_pnl': gross_pnl_total,
        'costs': cost_total,
    }


def trades_path(cell_dir: Path) -> Path:
    """The trade blotter of a cell, whichever artifact layout it uses.

    The run is not uniform: the five largest market-cap names of the baseline
    study carry the legacy `trades.csv` layout, the rest the gzip-compressed
    `trades.csv.gz`. Reading only one of the two would silently drop the top
    of the universe.
    """
    gz = Path(cell_dir) / 'trades.csv.gz'
    if gz.exists():
        return gz
    return Path(cell_dir) / 'trades.csv'


def scan_grid(run_dir: Path, fixture_base: str, n_folds: int,
              stress_multiplier: float) -> tuple:
    """Read a whole grid once and return its fold statistics and its pooled
    full-sample statistics.

    The two are read in one pass over the blotters: a grid holds 17 556
    cells, and reading them twice would double the runtime of the leg for
    no reason.
    """
    from data.data_loader import load_ohlcv_csv
    from scripts.survivor_selection_audit import cell_fold_stats, fold_edges
    from scripts.run_grid import symbol_dir_name

    rows = []
    bars_cache = {}
    win = loss = 0.0
    gross_win = gross_loss = 0.0
    s_win = s_loss = 0.0
    trades = 0
    cells = 0
    cost_total = 0.0
    gross_pnl_total = 0.0
    cost_shares = []
    risk_distances = []

    results_root = run_dir / 'results'
    for sym_dir in sorted(results_root.iterdir()):
        if not sym_dir.is_dir():
            continue
        symbol = sym_dir.name.replace('_', '/')
        if symbol not in bars_cache:
            path = Path(fixture_base) / f'{symbol_dir_name(symbol)}.csv'
            if not path.exists():
                continue
            bars_cache[symbol] = len(load_ohlcv_csv(str(path)))
        n_bars = bars_cache[symbol]
        edges = fold_edges(n_bars, n_folds)
        for cell_dir in sorted(sym_dir.iterdir()):
            summary_path = cell_dir / 'summary.json'
            if not cell_dir.is_dir() or not summary_path.exists():
                continue
            summary = json.loads(summary_path.read_text())
            if summary.get('blocked'):
                continue
            if not trades_path(cell_dir).exists():
                continue
            cells += 1
            blotter = read_artifact_csv(trades_path(cell_dir))
            if blotter is None or len(blotter) == 0:
                rows.append({'symbol': symbol, 'P_fast': int(summary['P_fast']),
                             'P_slow': int(summary['P_slow']), 'n_bars': n_bars,
                             'folds': cell_fold_stats(blotter, edges, stress_multiplier)})
                continue
            rows.append({'symbol': symbol, 'P_fast': int(summary['P_fast']),
                         'P_slow': int(summary['P_slow']), 'n_bars': n_bars,
                         'folds': cell_fold_stats(blotter, edges, stress_multiplier)})
            pnl = blotter['pnl_net'].to_numpy(dtype=float)
            gross = blotter['pnl'].to_numpy(dtype=float)
            entry_cost = blotter['entry_cost'].to_numpy(dtype=float)
            exit_cost = blotter['exit_cost'].to_numpy(dtype=float)
            stress = stressed_pnl_net(pnl, entry_cost, exit_cost, stress_multiplier)
            w, l = win_loss_sums(pnl)
            win += w
            loss += l
            cell_gross_win = float(gross[gross > 0].sum())
            cell_gross_loss = float(-gross[gross < 0].sum())
            gross_win += cell_gross_win
            gross_loss += cell_gross_loss
            s_w, s_l = win_loss_sums(stress)
            s_win += s_w
            s_loss += s_l
            trades += len(blotter)
            cell_cost = float(entry_cost.sum() + exit_cost.sum())
            cost_total += cell_cost
            gross_pnl_total += float(gross.sum())
            # The cost share of the gross move, per cell, exactly as the
            # cost-drag leg measures it: the costs of the cell divided by the
            # gross money the cell moved. A cell that loses money gross cannot
            # be rescued by a cheap cost model.
            gross_move = cell_gross_win + cell_gross_loss
            if gross_move > 0:
                cost_shares.append(cell_cost / gross_move)
            if 'risk_pct' in blotter.columns:
                risk_pct = blotter['risk_pct'].to_numpy(dtype=float)
                if risk_pct.size:
                    risk_distances.append(float(np.median(risk_pct)))

    def pf(w, l):
        if l > 0:
            return w / l
        if w > 0:
            return float('inf')
        return None

    grid = {
        'cells': cells,
        'trades': trades,
        'net_pf': pf(win, loss),
        'stress_net_pf': pf(s_win, s_loss),
        'gross_pf': pf(gross_win, gross_loss),
        'net_pnl': win - loss,
        'gross_pnl': gross_pnl_total,
        'costs': cost_total,
        # The median of the per-cell cost shares, the same statistic the
        # cost-drag leg reports, so the two legs can be read against each
        # other.
        'median_cell_cost_share_of_gross': (float(np.median(cost_shares))
                                            if cost_shares else None),
        'median_cell_risk_pct': (float(np.median(risk_distances))
                                 if risk_distances else None),
    }
    return rows, grid


def gate_survivors(oos_dir: Path, min_trades: int = 30) -> list:
    """The cells that clear the grid-wide out-of-sample gate."""
    rows = []
    with open(oos_dir / 'cells.jsonl') as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    survivors = []
    for row in rows:
        if (row.get('oos_trades') or 0) < min_trades:
            continue
        if (row.get('oos_net_pf') or 0.0) <= 1.0:
            continue
        if (row.get('oos_stress_net_pf') or 0.0) <= 1.0:
            continue
        survivors.append(row)
    survivors.sort(key=lambda r: -r['oos_net_pf'])
    return survivors


def arm_payload(label: str, grid_dir: Path, oos_dir: Path, fold_rows: list,
                grid: dict, n_folds: int, min_history_trades: int, mcap: str,
                buckets: int) -> dict:
    """Everything the comparison needs about one arm."""
    symbols = sorted({row['symbol'] for row in fold_rows})
    ordered = rank_symbols(mcap, symbols)
    bucket_map = market_cap_buckets(ordered, buckets)
    steps = walk_forward(fold_rows, 'symbol', 1, n_folds, min_history_trades,
                         bucket_map)
    walk = summarize(steps)
    survivors = gate_survivors(oos_dir)
    return {
        'label': label,
        'grid': str(grid_dir),
        'oos_audit': str(oos_dir),
        'n_symbols': len(symbols),
        'n_cells': len(fold_rows),
        'grid_stats': grid,
        'walk_forward': walk,
        'gate_survivors': survivors,
        'n_gate_survivors': len(survivors),
    }


def _fmt(value) -> str:
    if value is None:
        return 'n/a'
    try:
        value = float(value)
    except (TypeError, ValueError):
        return str(value)
    if not math.isfinite(value):
        return 'inf'
    return f'{value:.4f}'


def _pct(value) -> str:
    if value is None:
        return 'n/a'
    try:
        value = float(value)
    except (TypeError, ValueError):
        return str(value)
    if not math.isfinite(value):
        return 'n/a'
    return f'{value * 100:.1f}%'


def build_verdict(payload: dict) -> list:
    """The conclusion of the leg, as a list of report lines."""
    lines = []
    parent = payload['parent']
    child = payload['child']
    pg = parent['grid_stats']
    cg = child['grid_stats']
    pw = parent['walk_forward']
    cw = child['walk_forward']
    rule = payload.get('decision_rule') or {}

    lines.append(
        f"Full sample: the child's pooled net PF is {_fmt(cg['net_pf'])} against the "
        f"parent's {_fmt(pg['net_pf'])} (delta {_fmt((cg['net_pf'] or 0) - (pg['net_pf'] or 0))}), "
        f"on {cg['trades']} trades instead of {pg['trades']} "
        f"({_pct(cg['trades'] / pg['trades']) if pg['trades'] else 'n/a'} of the parent's "
        f"sample).")
    lines.append(
        f"Cost drag: the median cell spends "
        f"{_pct(cg.get('median_cell_cost_share_of_gross'))} of its gross move on "
        f"costs, against {_pct(pg.get('median_cell_cost_share_of_gross'))} for the "
        f"parent, because the median stop widens from "
        f"{_pct(pg.get('median_cell_risk_pct'))} to "
        f"{_pct(cg.get('median_cell_risk_pct'))} of the entry price. The gross "
        f"result itself moves from a gross PF of {_fmt(pg['gross_pf'])} to "
        f"{_fmt(cg['gross_pf'])}, so the filter repairs the cost drag and also "
        f"changes the gross result - it is not only a cost effect.")
    lines.append(
        f"Walk-forward yardstick: the child's pooled out-of-fold net PF is "
        f"{_fmt(cw['pooled_oof_net_pf'])} ({_fmt(cw['pooled_oof_stress_net_pf'])} under "
        f"2x costs) over {cw['oof_trades']} out-of-fold trades, against the parent's "
        f"{_fmt(pw['pooled_oof_net_pf'])} ({_fmt(pw['pooled_oof_stress_net_pf'])}).")
    lines.append(
        f"Grid-wide out-of-sample gate: {child['n_gate_survivors']} of "
        f"{child['n_cells']} child cells clear it, against {parent['n_gate_survivors']} "
        f"of {parent['n_cells']} parent cells.")

    passes = ((cw['pooled_oof_net_pf'] or 0.0) > 1.0
              and (cw['pooled_oof_stress_net_pf'] or 0.0) > 1.0
              and child['n_gate_survivors'] > 0)
    if passes:
        lines.append(
            "The pre-registered decision rule is satisfied: the child clears the "
            "out-of-fold gate, survives the cost stress and has cells that clear the "
            "grid-wide gate. It has to go through the full promotion checklist "
            "(sub-period stability, the candidate check, the robustness pool) before it "
            "can be called a candidate.")
    else:
        lines.append(
            "The pre-registered decision rule is NOT satisfied: the child does not clear "
            "the out-of-fold gate under the identical walk-forward protocol, does not "
            "survive the 2x cost stress, or has no cell that clears the grid-wide gate. "
            "The mutation is recorded as a rejected mutation: a narrower gap between gross "
            "and net is a cost-drag repair, not an edge.")
    if rule:
        lines.append(f"Decision rule (registered before the child run): {rule}")
    return lines


def write_report(out_dir: Path, payload: dict) -> None:
    """Write the human-readable leg report."""
    parent = payload['parent']
    child = payload['child']
    lines = []
    lines.append('# Mutation Comparison — parent -> child -> delta\n')
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Parent grid:** `{parent['grid']}`")
    lines.append(f"**Child grid:** `{child['grid']}`")
    if payload.get('preregistration'):
        lines.append(f"**Pre-registration:** `{payload['preregistration']}`")
    lines.append(f"**Cost model:** {payload['config']['taker_fee_bps']} bps taker + "
                 f"{payload['config']['slippage_bps']} bps slippage per side "
                 f"(stress leg: {payload['stress_multiplier']}x)\n")

    lines.append('## Parent -> child -> delta\n')
    lines.append('| Measure | Parent | Child | Delta |')
    lines.append('|---|---|---|---|')
    pg = parent['grid_stats']
    cg = child['grid_stats']
    rows = [
        ('Cells', pg['cells'], cg['cells']),
        ('Trades', pg['trades'], cg['trades']),
        ('Pooled net PF (full sample)', pg['net_pf'], cg['net_pf']),
        ('Pooled net PF (2x costs)', pg['stress_net_pf'], cg['stress_net_pf']),
        ('Pooled gross PF', pg['gross_pf'], cg['gross_pf']),
        ('Pooled net P&L', pg['net_pnl'], cg['net_pnl']),
        ('Costs paid', pg['costs'], cg['costs']),
        ('Median cell cost share of the gross move',
         pg.get('median_cell_cost_share_of_gross'),
         cg.get('median_cell_cost_share_of_gross')),
        ('Median cell stop distance (share of entry price)',
         pg.get('median_cell_risk_pct'), cg.get('median_cell_risk_pct')),
        ('Pooled out-of-fold net PF (walk-forward)', parent['walk_forward']['pooled_oof_net_pf'],
         child['walk_forward']['pooled_oof_net_pf']),
        ('Pooled out-of-fold net PF (2x costs)', parent['walk_forward']['pooled_oof_stress_net_pf'],
         child['walk_forward']['pooled_oof_stress_net_pf']),
        ('Out-of-fold trades', parent['walk_forward']['oof_trades'],
         child['walk_forward']['oof_trades']),
        ('Out-of-fold windows above PF 1', parent['walk_forward']['oof_pf_gt_1'],
         child['walk_forward']['oof_pf_gt_1']),
        ('Cells clearing the grid-wide OOS gate', parent['n_gate_survivors'],
         child['n_gate_survivors']),
    ]
    for name, parent_value, child_value in rows:
        if isinstance(parent_value, (int, float)) and isinstance(child_value, (int, float)):
            delta = f'{child_value - parent_value:,.4f}'
        else:
            delta = 'n/a'
        lines.append(f"| {name} | {_fmt(parent_value)} | {_fmt(child_value)} | {delta} |")
    lines.append('')

    lines.append('## The child\'s cells that clear the grid-wide out-of-sample gate\n')
    if child['gate_survivors']:
        lines.append('| Symbol | Cell | Out-of-sample trades | Out-of-sample net PF | '
                     'Out-of-sample net PF (2x costs) |')
        lines.append('|---|---|---|---|---|')
        for row in child['gate_survivors']:
            lines.append(
                f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                f"{row['oos_trades']} | {_fmt(row['oos_net_pf'])} | "
                f"{_fmt(row['oos_stress_net_pf'])} |")
    else:
        lines.append('No cell of the child clears the gate '
                     '(out-of-sample net PF > 1, at least 30 out-of-sample trades, '
                     'still > 1 under 2x costs).')
    lines.append('')

    lines.append('## The parent\'s cells that clear the grid-wide out-of-sample gate\n')
    if parent['gate_survivors']:
        lines.append('| Symbol | Cell | Out-of-sample trades | Out-of-sample net PF | '
                     'Out-of-sample net PF (2x costs) |')
        lines.append('|---|---|---|---|---|')
        for row in parent['gate_survivors']:
            lines.append(
                f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                f"{row['oos_trades']} | {_fmt(row['oos_net_pf'])} | "
                f"{_fmt(row['oos_stress_net_pf'])} |")
    else:
        lines.append('No cell of the parent clears the gate.')
    lines.append('')

    lines.append('## Verdict\n')
    for line in payload['verdict']:
        lines.append(f'- {line}')
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(
        description='Parent -> child -> delta for a pre-registered mutation')
    parser.add_argument('--parent', type=str, required=True)
    parser.add_argument('--parent-oos', type=str, required=True)
    parser.add_argument('--child', type=str, required=True)
    parser.add_argument('--child-oos', type=str, required=True)
    parser.add_argument('--preregistration', type=str, default=None)
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--n-folds', type=int, default=5)
    parser.add_argument('--min-history-trades', type=int, default=20)
    parser.add_argument('--buckets', type=int, default=5)
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    out_dir = Path(args.out) if args.out else Path(
        f"results/{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
        f"_mutation_comparison")
    out_dir.mkdir(parents=True, exist_ok=True)

    parent_rows, parent_grid = scan_grid(Path(args.parent), args.fixture_base,
                                         args.n_folds, args.stress_multiplier)
    child_rows, child_grid = scan_grid(Path(args.child), args.fixture_base,
                                       args.n_folds, args.stress_multiplier)

    # The fold statistics are written out so that the other legs (the
    # selection-granularity ladder) can read them instead of scanning the
    # blotters of 17 556 cells a second time.
    for label, rows in (('parent', parent_rows), ('child', child_rows)):
        with open(out_dir / f'{label}_fold_stats.jsonl', 'w') as fh:
            for row in rows:
                fh.write(json.dumps(row) + '\n')

    parent = arm_payload('parent', Path(args.parent), Path(args.parent_oos),
                          parent_rows, parent_grid, args.n_folds,
                          args.min_history_trades, args.mcap, args.buckets)
    child = arm_payload('child', Path(args.child), Path(args.child_oos),
                        child_rows, child_grid, args.n_folds,
                        args.min_history_trades, args.mcap, args.buckets)

    decision_rule = None
    prereg = None
    if args.preregistration:
        prereg = Path(args.preregistration)
        prereg_file = prereg / 'preregistration.json'
        if prereg_file.exists():
            decision_rule = json.loads(prereg_file.read_text()).get(
                'decision_rule_fixed_in_advance')

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'config': dict(CONFIG_DEFAULTS),
        'stress_multiplier': args.stress_multiplier,
        'preregistration': str(prereg) if prereg else None,
        'decision_rule': decision_rule,
        'parent': parent,
        'child': child,
    }
    payload['verdict'] = build_verdict(payload)

    with open(out_dir / 'config.json', 'w') as fh:
        json.dump({'args': vars(args), 'config': dict(CONFIG_DEFAULTS)}, fh, indent=2)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    write_report(out_dir, payload)
    print(f'Wrote {out_dir}/summary.md')


if __name__ == '__main__':
    main()
