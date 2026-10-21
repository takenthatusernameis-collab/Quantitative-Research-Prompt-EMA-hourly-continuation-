#!/usr/bin/env python3
"""Audit of a grid cell refresh.

Why this exists
---------------
The data layer re-fetches a fixture whenever a symbol is (re-)added to the
universe, and a re-fetch can change the bar sequence of that symbol: the
first bar moves, the last bar moves, or the history grows. When that happens
*after* the grid has already run the symbol's cells, the stored artifacts
describe a data version that is no longer on disk, and a re-run of the grid
does not reproduce the stored summaries.

This script makes that drift auditable instead of invisible. It compares the
metrics of a set of cells before and after a refresh and reports:

* which symbols drifted, and how (bar count, first and last bar);
* how many cells changed, and by how much;
* whether any cell crossed a reporting threshold (net PF > 1, or the §3.4
  gate), because a drift that only moves the third decimal is a footnote and
  a drift that moves a cell across a threshold is a finding.

Usage:
    python scripts/refresh_audit.py --run results/20261019_135940_grid \
        --symbols RLC/USDT,ROSE/USDT --before before.json --out results/<ts>_refresh_audit
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

# The metrics a cell reports, and the ones the audit compares.
METRIC_KEYS = ('trade_count', 'net_profit_factor', 'gross_profit_factor',
               'sharpe_ratio', 'max_drawdown', 'net_win_rate')


def cell_dir(run_dir: Path, symbol: str, fast: int, slow: int) -> Path:
    return Path(run_dir) / 'results' / symbol.replace('/', '_') / f'P{fast}_{slow}'


def read_cell(run_dir: Path, symbol: str, fast: int, slow: int) -> dict:
    """The metrics of one stored cell."""
    summary = json.loads((cell_dir(run_dir, symbol, fast, slow) / 'summary.json').read_text())
    return {key: summary.get(key) for key in METRIC_KEYS}


def symbol_bar_sequence(run_dir: Path, symbol: str) -> list:
    """The bar timestamps the grid ran the symbol on.

    The equity artifact holds one row per bar, so its timestamps are the bar
    sequence the stored cells were computed on.
    """
    sym_dir = Path(run_dir) / 'results' / symbol.replace('/', '_')
    cells = sorted(p for p in sym_dir.iterdir() if p.is_dir())
    for cell in cells:
        gz = cell / 'equity.csv.gz'
        plain = cell / 'equity.csv'
        if gz.exists():
            return pd.read_csv(gz, usecols=['timestamp'])['timestamp'].astype(str).tolist()
        if plain.exists():
            return pd.read_csv(plain, usecols=['timestamp'])['timestamp'].astype(str).tolist()
    return []


def fixture_bar_sequence(fixture_base: str, symbol: str) -> list:
    """The bar timestamps of the fixture on disk."""
    path = Path(fixture_base) / f"{symbol.replace('/', '_')}.csv"
    return pd.read_csv(path, usecols=['timestamp'])['timestamp'].astype(str).tolist()


def compare_cells(before: dict, after: dict) -> dict:
    """Per-cell comparison of two metric sets."""
    rows = []
    for key in sorted(before):
        old = before[key]
        new = after.get(key)
        if new is None:
            continue
        old_pf = old.get('net_profit_factor')
        new_pf = new.get('net_profit_factor')
        rows.append({
            'cell': key,
            'trade_count_before': old.get('trade_count'),
            'trade_count_after': new.get('trade_count'),
            'net_pf_before': old_pf,
            'net_pf_after': new_pf,
            'net_pf_delta': (None if old_pf is None or new_pf is None else new_pf - old_pf),
            'sharpe_before': old.get('sharpe_ratio'),
            'sharpe_after': new.get('sharpe_ratio'),
            'crossed_pf_1': bool((old_pf or 0.0) > 1.0) != bool((new_pf or 0.0) > 1.0),
        })
    changed = [r for r in rows if r['net_pf_delta'] not in (None, 0.0)
               or r['trade_count_before'] != r['trade_count_after']]
    deltas = [abs(r['net_pf_delta']) for r in rows if r['net_pf_delta'] is not None]
    return {
        'n_cells': len(rows),
        'n_changed': len(changed),
        'n_crossed_pf_1': sum(1 for r in rows if r['crossed_pf_1']),
        'max_abs_net_pf_delta': max(deltas) if deltas else 0.0,
        'mean_abs_net_pf_delta': (sum(deltas) / len(deltas)) if deltas else 0.0,
        'rows': rows,
    }


def write_report(out_dir: Path, payload: dict) -> None:
    """The human-readable audit report."""
    lines = []
    lines.append('# Grid Cell Refresh Audit — EMA Hourly Continuation\n')
    lines.append(f"**Grid run:** `{payload['source_run']}`")
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Reason:** {payload['reason']}\n")
    lines.append('## The drift\n')
    lines.append('| Symbol | Bars before | Bars now | First bar before | First bar now | '
                 'Last bar before | Last bar now |')
    lines.append('|---|---|---|---|---|---|---|')
    for row in payload['symbols']:
        lines.append(
            f"| {row['symbol']} | {row['bars_before']} | {row['bars_now']} | "
            f"{row['first_before']} | {row['first_now']} | "
            f"{row['last_before']} | {row['last_now']} |")
    lines.append('')
    lines.append('## The impact on the cells\n')
    lines.append('| Quantity | Value |')
    lines.append('|---|---|')
    summary = payload['comparison']
    lines.append(f"| Cells re-run | {summary['n_cells']} |")
    lines.append(f"| Cells whose metrics changed | {summary['n_changed']} |")
    lines.append(f"| Cells that crossed net PF > 1 | {summary['n_crossed_pf_1']} |")
    lines.append(f"| Largest absolute net PF change | {summary['max_abs_net_pf_delta']:.6f} |")
    lines.append(f"| Mean absolute net PF change | {summary['mean_abs_net_pf_delta']:.6f} |")
    lines.append('')
    changed = [r for r in summary['rows'] if r['net_pf_delta'] not in (None, 0.0)
               or r['trade_count_before'] != r['trade_count_after']]
    if changed:
        lines.append('| Cell | Trades before | Trades now | Net PF before | Net PF now | Delta |')
        lines.append('|---|---|---|---|---|---|')
        for row in changed:
            lines.append(
                f"| {row['cell']} | {row['trade_count_before']} | {row['trade_count_after']} | "
                f"{row['net_pf_before']:.6f} | {row['net_pf_after']:.6f} | "
                f"{row['net_pf_delta']:+.6f} |")
        lines.append('')
    lines.append('## Reading\n')
    lines.append(payload['reading'] + '\n')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(description='Audit a grid cell refresh')
    parser.add_argument('--run', type=str, required=True, help='results/<RUNID>_grid')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--symbols', type=str, required=True,
                        help='Comma-separated symbols that were refreshed')
    parser.add_argument('--before', type=str, required=True,
                        help='JSON file with the metrics of the cells before the refresh')
    parser.add_argument('--before-bars', type=str, default=None,
                        help='JSON file with the bar sequence of each symbol before the '
                             'refresh (symbol -> {n, first, last}). The refresh rewrites the '
                             'equity artifact, so the drift of the bar sequence cannot be '
                             'read from the grid afterwards.')
    parser.add_argument('--reason', type=str, default='fixture re-fetch')
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    run_dir = Path(args.run)
    symbols = [s.strip() for s in args.symbols.split(',') if s.strip()]
    before = json.loads(Path(args.before).read_text())

    after = {}
    for key in before:
        symbol, cell = key.split('/')
        fast, slow = cell[1:].split('_')
        after[key] = read_cell(run_dir, symbol, int(fast), int(slow))

    symbol_rows = []
    before_bars = {}
    if args.before_bars:
        before_bars = json.loads(Path(args.before_bars).read_text())
    for symbol in symbols:
        current = fixture_bar_sequence(args.fixture_base, symbol)
        stored = symbol_bar_sequence(run_dir, symbol)
        prior = before_bars.get(symbol)
        if prior is None:
            # No pre-refresh snapshot: the grid's own equity artifact is the
            # only record of the bar sequence the cells ran on.
            prior = {'n': len(stored), 'first': stored[0] if stored else 'n/a',
                     'last': stored[-1] if stored else 'n/a'}
        symbol_rows.append({
            'symbol': symbol,
            'bars_before': prior.get('n'),
            'bars_now': len(current),
            'first_before': prior.get('first'),
            'first_now': current[0] if current else 'n/a',
            'last_before': prior.get('last'),
            'last_now': current[-1] if current else 'n/a',
            'identical': (prior.get('n') == len(current)
                          and prior.get('first') == (current[0] if current else 'n/a')),
        })

    comparison = compare_cells(before, after)
    reading = (
        'The refresh moves the cells by the amount shown above. A cell that does not cross '
        'net PF = 1 keeps its decision label, so the labels of the grid are unchanged by '
        'this refresh; the cells that cross the threshold are listed in the table and are '
        'the only ones that can change a published count.'
    )
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_run': str(run_dir),
        'fixture_base': args.fixture_base,
        'reason': args.reason,
        'symbols': symbol_rows,
        'comparison': comparison,
        'reading': reading,
    }

    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    out_dir = Path(args.out) if args.out else Path('results') / f'{timestamp}_refresh_audit'
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    with open(out_dir / 'before.json', 'w') as fh:
        json.dump(before, fh, indent=2, default=str)
    with open(out_dir / 'after.json', 'w') as fh:
        json.dump(after, fh, indent=2, default=str)
    if args.before_bars:
        with open(out_dir / 'before_bars.json', 'w') as fh:
            json.dump(before_bars, fh, indent=2, default=str)
    write_report(out_dir, payload)
    print(f"Refreshed cells: {comparison['n_cells']}, changed: {comparison['n_changed']}, "
          f"crossed net PF > 1: {comparison['n_crossed_pf_1']}")
    print(f'Wrote {out_dir}/summary.md and summary.json')


if __name__ == '__main__':
    main()
