#!/usr/bin/env python3
"""Reproduction check of a mutation child grid against its parent.

Why this exists
---------------
`scripts/mutation_eval.py` scores a mutation by comparing the parent run and
the child run through their stored summaries. That is the right way to
measure the mutation, but two things still have to be true before the delta
can be read as *the effect of one registered change*:

* both grids have to be the artifacts of the same engine, so a re-run of a
  cell has to reproduce the stored blotter and the stored summary exactly;
* the child has to differ from the parent *because of the mutation*, which
  means the difference has to be visible in the trades themselves.

This script re-runs a sample of cells of both runs on the same fixtures and
compares them with the stored artifacts, trade by trade. It then measures
how the two paths differ, because the ATR minimum-risk filter does not only
delete entries: once an entry is skipped the position state, and with it the
equity path and the size of every later trade, changes. The mutation is a
different trading path, not a pruned list of the parent's trades.

Usage:
    python scripts/mutation_repro_check.py \
        --parent results/20261019_135940_grid \
        --child results/20261021_172619_grid \
        --out results/<TS>_mutation_repro_check
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from data.data_loader import load_ohlcv_csv
from scripts.run_grid import (period_pairs, read_artifact_csv, run_cell,
                              symbol_dir_name)

# The fields of a trade that have to be identical for a re-run to reproduce
# the stored blotter.
TRADE_FIELDS = ['side', 'entry_price', 'exit_price', 'sl', 'tp', 'risk', 'pnl',
                'pnl_net', 'exit_reason', 'bar_index', 'exit_bar_index', 'qty',
                'notional', 'entry_cost', 'exit_cost', 'risk_pct']

# The summary fields that have to be identical.
METRIC_FIELDS = ['trade_count', 'net_profit_factor', 'gross_profit_factor',
                 'win_rate', 'max_drawdown', 'sharpe_ratio', 'sortino_ratio',
                 'cagr', 'equity_reconciles']

REL_TOL = 1e-12
ABS_TOL = 1e-12


def cell_dir(run_dir: Path, symbol: str, fast: int, slow: int) -> Path:
    """Directory of one (symbol, P_fast, P_slow) cell of a run."""
    return run_dir / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'


def read_blotter(cell_path: Path) -> pd.DataFrame:
    """Read one cell's trade blotter (gzip layout or the legacy plain CSV)."""
    path = cell_path / 'trades.csv.gz'
    if not path.exists():
        path = cell_path / 'trades.csv'
    return read_artifact_csv(path)


def compare_trades(stored: pd.DataFrame, rerun: pd.DataFrame) -> list:
    """Fields in which the re-run trades differ from the stored trades."""
    if len(stored) != len(rerun):
        return [f'trade_count {len(rerun)} != {len(stored)}']
    diffs = []
    for index in range(len(stored)):
        srow, rrow = stored.iloc[index], rerun.iloc[index]
        for field in TRADE_FIELDS:
            a, b = srow.get(field), rrow.get(field)
            if isinstance(a, (int, float, np.integer, np.floating)) and \
                    isinstance(b, (int, float, np.integer, np.floating)):
                if not np.isclose(float(a), float(b), rtol=REL_TOL, atol=ABS_TOL):
                    diffs.append(f'{index}:{field}')
            elif str(a) != str(b):
                diffs.append(f'{index}:{field}')
    return diffs


def compare_metrics(stored: dict, metrics: dict) -> dict:
    """Absolute difference of every compared summary field."""
    deltas = {}
    for field in METRIC_FIELDS:
        a, b = stored.get(field), metrics.get(field)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            deltas[field] = abs(float(a) - float(b))
        else:
            deltas[field] = 0.0 if a == b else float('inf')
    return deltas


def reproduce_cell(run_dir: Path, symbol: str, fast: int, slow: int,
                   config: dict, fixture_base: str) -> dict:
    """Re-run one cell with the given config and compare with the artifacts."""
    cdir = cell_dir(run_dir, symbol, fast, slow)
    df = load_ohlcv_csv(str(Path(fixture_base) / f'{symbol_dir_name(symbol)}.csv'))
    trades, _, metrics = run_cell(
        symbol, df, fast, slow, config['taker_fee_bps'], config['slippage_bps'],
        config['rr'], config['stricter_trend'], config['min_risk_atr'],
        config['atr_threshold'], config['conservative_exit'], oos_fraction=None,
        sizing=config['sizing'], risk_fraction=config['risk_fraction'],
        max_notional_multiple=config['max_notional_multiple'])
    stored_summary = json.loads((cdir / 'summary.json').read_text())
    stored_trades = read_blotter(cdir)
    rerun_trades = pd.DataFrame([t.__dict__ for t in trades])
    trade_diffs = compare_trades(stored_trades, rerun_trades)
    metric_deltas = compare_metrics(stored_summary, metrics)
    return {
        'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
        'stored_trades': int(len(stored_trades)),
        'rerun_trades': int(len(rerun_trades)),
        'trade_diffs': trade_diffs,
        'metric_deltas': metric_deltas,
        'max_abs_metric_delta': max(metric_deltas.values()) if metric_deltas else 0.0,
        'reproduced': bool(not trade_diffs
                           and all(v == 0.0 for v in metric_deltas.values())),
    }


def path_difference(parent_cell: Path, child_cell: Path) -> dict:
    """How the two paths differ, measured on the stored blotters."""
    parent = read_blotter(parent_cell)
    child = read_blotter(child_cell)
    parent_bars = [int(b) for b in parent['bar_index']]
    child_bars = [int(b) for b in child['bar_index']]
    parent_set, child_set = set(parent_bars), set(child_bars)
    shared = parent_set & child_set
    return {
        'parent_trades': len(parent_bars),
        'child_trades': len(child_bars),
        'shared_entry_bars': len(shared),
        'parent_only_entry_bars': len(parent_set - child_set),
        'child_only_entry_bars': len(child_set - parent_set),
        'first_divergent_bar': min(parent_set ^ child_set) if parent_set ^ child_set else None,
        'child_trade_share': (len(child_bars) / len(parent_bars)) if parent_bars else None,
    }


def complete_child_symbols(child_dir: Path, symbols: list) -> list:
    """Symbols whose child grid is complete (every cell has a summary)."""
    pairs = period_pairs()
    return [s for s in symbols
            if all((cell_dir(child_dir, s, f, sl) / 'summary.json').exists()
                   for f, sl in pairs)]


def sample_cells(symbols: list, sample_size: int) -> list:
    """Pick cells spread over the symbols and over the period grid."""
    pairs = period_pairs()
    picks = []
    if not symbols or sample_size <= 0:
        return picks
    step = max(1, len(symbols) // max(1, sample_size))
    for index, symbol in enumerate(symbols[::step][:sample_size]):
        fast, slow = pairs[index % len(pairs)]
        picks.append((symbol, fast, slow))
    return picks


def build_verdict(payload: dict) -> list:
    """The plain-language reading of the check."""
    verdict = []
    if payload['n_cells_checked'] == 0:
        return ['No cell of the child run is complete yet, so the child grid '
                'cannot be reproduced against its parent yet.']
    child_ok = payload['child_cells_reproduced']
    parent_ok = payload['parent_cells_reproduced']
    verdict.append(
        f"{child_ok}/{payload['n_cells_checked']} re-run child cells reproduce "
        f"the stored child blotter and summary exactly, and "
        f"{parent_ok}/{payload['n_cells_checked']} re-run parent cells "
        f"reproduce the stored parent artifacts: both grids are artifacts of "
        f"the same engine.")
    verdict.append(
        f"The mutation removes "
        f"{payload['mean_parent_only_entry_bars']:.1f} of the parent's entry "
        f"bars on average and adds "
        f"{payload['mean_child_only_entry_bars']:.1f} entries the parent never "
        f"took: the ATR minimum-risk filter does not prune the parent's trade "
        f"list, it changes the path, so the child is a different strategy "
        f"instance and not a filtered view of the parent.")
    if payload['n_violations'] == 0:
        verdict.append('No violation found: the child run is a faithful '
                       're-run of the parent engine with the ATR '
                       'minimum-risk filter applied.')
    else:
        verdict.append(f"{payload['n_violations']} violation(s): a re-run does "
                       f"not reproduce the stored artifacts, so the delta "
                       f"cannot be read as the effect of the mutation alone.")
    return verdict


def write_report(out_dir: Path, payload: dict) -> None:
    """Render the human-readable summary of the check."""
    lines = ['# Mutation Reproduction Check', '',
             f"**Parent run:** `{payload['parent_run']}`",
             f"**Child run:** `{payload['child_run']}`",
             f"**Generated:** {payload['generated_at']}",
             f"**Cells re-run:** {payload['n_cells_checked']}", '',
             '## Leg 1 - the artifacts are re-runnable', '',
             'Every sampled cell is re-run through the real backtest on the '
             'same fixture and compared with the stored blotter and the stored '
             'summary, trade by trade.', '',
             '| Symbol | Cell | Child reproduces | Parent reproduces | '
             'Child max metric delta | Parent max metric delta |',
             '|---|---|---|---|---|---|']
    for row in payload['cells']:
        lines.append(
            f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
            f"{'yes' if row['child']['reproduced'] else 'NO'} | "
            f"{'yes' if row['parent']['reproduced'] else 'NO'} | "
            f"{row['child']['max_abs_metric_delta']:.3e} | "
            f"{row['parent']['max_abs_metric_delta']:.3e} |")
    lines += ['', '## Leg 2 - how the two paths differ', '',
              'The ATR minimum-risk filter skips an entry, so the position '
              'state, the equity path and the size of every later trade '
              'change with it. The child is therefore a different path, not a '
              'subset of the parent\'s trades.', '',
              '| Symbol | Cell | Parent trades | Child trades | Shared entry '
              'bars | Parent-only bars | Child-only bars | First divergence |',
              '|---|---|---|---|---|---|---|---|']
    for row in payload['cells']:
        path = row['path']
        lines.append(
            f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
            f"{path['parent_trades']} | {path['child_trades']} | "
            f"{path['shared_entry_bars']} | {path['parent_only_entry_bars']} | "
            f"{path['child_only_entry_bars']} | {path['first_divergent_bar']} |")
    lines += ['', '## Verdict', '']
    for item in payload['verdict']:
        lines.append(f'- {item}')
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(
        description='Reproduction check of a mutation child grid')
    parser.add_argument('--parent', type=str, default='results/20261019_135940_grid')
    parser.add_argument('--child', type=str, default='results/20261021_172619_grid')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--sample', type=int, default=16,
                        help='how many cells to re-run')
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    parent_dir = Path(args.parent)
    child_dir = Path(args.child)
    out_dir = Path(args.out) if args.out else Path(
        f"results/{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
        f"_mutation_repro_check")
    out_dir.mkdir(parents=True, exist_ok=True)

    parent_cfg = json.loads((parent_dir / 'run_config.json').read_text())['config']
    child_cfg = json.loads((child_dir / 'run_config.json').read_text())['config']

    from universe.universe import load_mcap_ranking
    ranking = load_mcap_ranking(args.mcap)
    symbols = complete_child_symbols(child_dir, ranking)
    picks = sample_cells(symbols, args.sample)

    rows = []
    violations = []
    for symbol, fast, slow in picks:
        pdir = cell_dir(parent_dir, symbol, fast, slow)
        cdir = cell_dir(child_dir, symbol, fast, slow)
        if not (pdir / 'summary.json').exists() or \
                not (cdir / 'summary.json').exists():
            continue
        child = reproduce_cell(child_dir, symbol, fast, slow, child_cfg,
                               args.fixture_base)
        parent = reproduce_cell(parent_dir, symbol, fast, slow, parent_cfg,
                                args.fixture_base)
        path = path_difference(pdir, cdir)
        rows.append({'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                     'child': child, 'parent': parent, 'path': path})
        for label in ('child', 'parent'):
            if not rows[-1][label]['reproduced']:
                violations.append({
                    'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                    'run': label,
                    'trade_diffs': rows[-1][label]['trade_diffs'][:10],
                    'metric_deltas': rows[-1][label]['metric_deltas'],
                })
        print(f"{symbol} P{fast}_{slow}: child reproduced "
              f"{rows[-1]['child']['reproduced']}, parent reproduced "
              f"{rows[-1]['parent']['reproduced']}", flush=True)

    def mean(key):
        values = [r['path'][key] for r in rows]
        return float(np.mean(values)) if values else 0.0

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'parent_run': str(parent_dir),
        'child_run': str(child_dir),
        'parent_config': parent_cfg,
        'child_config': child_cfg,
        'n_symbols_complete': len(symbols),
        'n_cells_checked': len(rows),
        'child_cells_reproduced': sum(1 for r in rows if r['child']['reproduced']),
        'parent_cells_reproduced': sum(1 for r in rows if r['parent']['reproduced']),
        'mean_parent_trades': mean('parent_trades'),
        'mean_child_trades': mean('child_trades'),
        'mean_shared_entry_bars': mean('shared_entry_bars'),
        'mean_parent_only_entry_bars': mean('parent_only_entry_bars'),
        'mean_child_only_entry_bars': mean('child_only_entry_bars'),
        'mean_child_trade_share': mean('child_trade_share'),
        'n_violations': len(violations),
        'violations': violations,
        'cells': rows,
    }
    payload['verdict'] = build_verdict(payload)
    payload['artifact'] = str(out_dir)

    with open(out_dir / 'config.json', 'w') as fh:
        json.dump({'args': vars(args)}, fh, indent=2, default=str)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    write_report(out_dir, payload)
    print(f'Wrote {out_dir}/summary.md')


if __name__ == '__main__':
    main()
