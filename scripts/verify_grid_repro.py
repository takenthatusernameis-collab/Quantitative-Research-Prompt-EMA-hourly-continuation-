#!/usr/bin/env python3
"""Reproducibility check of a grid run against the data on disk.

Why this exists
---------------
A stored cell is only reproducible if the fixture it was computed on is still
the fixture on disk. The data layer re-fetches a symbol's fixture whenever the
symbol is (re-)added to the universe, and a re-fetch can move the first bar,
move the last bar or extend the history. When that happens *after* the grid
has already run the symbol, the stored artifacts describe a data version that
no longer exists and a re-run of the grid does not reproduce them.

This check re-runs a set of cells through the grid runner's own `run_cell`
and compares the result with the stored `summary.json`. A cell that does not
reproduce is a cell whose artifact is stale.

The check is the pre-flight of an expansion: run it after a batch is fetched
and before the batch's cells are trusted, and run it again on the cells of
the previous batch, whose fixtures the new fetch may have disturbed.

Usage:
    python scripts/verify_grid_repro.py --run results/20261019_135940_grid \
        --symbols RLC/USDT,ROSE/USDT --workers 4
    python scripts/verify_grid_repro.py --run results/20261019_135940_grid \
        --sample 200 --workers 4
"""
import argparse
import json
import random
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from data.data_loader import load_ohlcv_csv
from scripts.run_grid import run_cell, run_config


def cell_metrics(run_dir: Path, symbol: str, fast: int, slow: int) -> dict:
    """The metrics of one stored cell."""
    cell = Path(run_dir) / 'results' / symbol.replace('/', '_') / f'P{fast}_{slow}'
    summary = json.loads((cell / 'summary.json').read_text())
    return {
        'stored_trade_count': summary.get('trade_count'),
        'stored_net_profit_factor': summary.get('net_profit_factor'),
        'stored_sharpe_ratio': summary.get('sharpe_ratio'),
    }


def check_cell(task) -> dict:
    """Re-run one cell and compare it with the stored summary.

    The re-run uses the config of the run being checked, not the default
    config: a pre-registered mutation run (e.g. the ATR minimum-risk filter)
    stores its own config, and re-running its cells with the default config
    would measure the parent rule instead of the child.
    """
    run_dir, symbol, fast, slow, fixture_base, engine = task
    cell = Path(run_dir) / 'results' / symbol.replace('/', '_') / f'P{fast}_{slow}'
    stored = cell_metrics(run_dir, symbol, fast, slow)
    config = run_config(run_dir)
    df = load_ohlcv_csv(str(Path(fixture_base) / f"{symbol.replace('/', '_')}.csv"))
    _, _, metrics = run_cell(
        symbol, df, fast, slow,
        config['taker_fee_bps'], config['slippage_bps'],
        config['rr'], config['stricter_trend'],
        config['min_risk_atr'], config['atr_threshold'],
        config['conservative_exit'], oos_fraction=None, sizing=config['sizing'],
        risk_fraction=config['risk_fraction'],
        max_notional_multiple=config['max_notional_multiple'],
        engine=engine,
    )
    same_trades = stored['stored_trade_count'] == metrics.get('trade_count')
    stored_pf = stored['stored_net_profit_factor']
    new_pf = metrics.get('net_profit_factor')
    same_pf = (stored_pf is None and new_pf is None) or (
        stored_pf is not None and new_pf is not None
        and abs(float(stored_pf) - float(new_pf)) <= 1e-12)
    return {
        'symbol': symbol,
        'P_fast': fast,
        'P_slow': slow,
        'reproduces': bool(same_trades and same_pf),
        'trade_count_before': stored['stored_trade_count'],
        'trade_count_after': metrics.get('trade_count'),
        'net_pf_before': stored_pf,
        'net_pf_after': new_pf,
    }


def grid_cells(run_dir: Path) -> list:
    """Every (symbol, P_fast, P_slow) cell of a grid run."""
    cells = []
    for sym_dir in sorted((Path(run_dir) / 'results').iterdir()):
        if not sym_dir.is_dir():
            continue
        symbol = sym_dir.name.replace('_', '/')
        for cell_dir in sorted(sym_dir.iterdir()):
            if not cell_dir.is_dir() or not (cell_dir / 'summary.json').exists():
                continue
            summary = json.loads((cell_dir / 'summary.json').read_text())
            if summary.get('blocked'):
                continue
            cells.append((symbol, int(summary['P_fast']), int(summary['P_slow'])))
    return cells


def write_report(out_dir: Path, payload: dict) -> None:
    """The human-readable report of the check."""
    lines = []
    lines.append('# Grid Reproducibility Check — EMA Hourly Continuation\n')
    lines.append(f"**Grid run:** `{payload['source_run']}`")
    lines.append(f"**Engine:** `{payload.get('engine', 'reference')}`")
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Fixture base:** `{payload['fixture_base']}`\n")
    lines.append('## Result\n')
    lines.append('| Quantity | Value |')
    lines.append('|---|---|')
    lines.append(f"| Cells checked | {payload['n_cells']} |")
    lines.append(f"| Cells that reproduce exactly | {payload['n_reproducing']} |")
    lines.append(f"| Cells that do NOT reproduce | {payload['n_stale']} |")
    lines.append('')
    if payload['stale']:
        lines.append('## Stale cells\n')
        lines.append('| Symbol | Cell | Trades before | Trades now | Net PF before | Net PF now |')
        lines.append('|---|---|---|---|---|---|')
        for row in payload['stale']:
            lines.append(
                f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                f"{row['trade_count_before']} | {row['trade_count_after']} | "
                f"{row['net_pf_before']} | {row['net_pf_after']} |")
        lines.append('')
        lines.append('A stale cell is a cell whose fixture changed after the grid ran it. '
                     'Re-run those cells with `scripts/run_grid.py --resume` and audit the '
                     'change with `scripts/refresh_audit.py`.\n')
    else:
        lines.append('Every checked cell reproduces exactly from the fixture on disk.\n')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(description='Check that the grid reproduces from the data')
    parser.add_argument('--run', type=str, required=True, help='results/<RUNID>_grid')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--symbols', type=str, default=None,
                        help='Comma-separated symbols to check (default: a random sample)')
    parser.add_argument('--sample', type=int, default=200,
                        help='Number of random cells to check when --symbols is not given')
    parser.add_argument('--seed', type=int, default=20261021)
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--engine', type=str, default='reference',
                        choices=['reference', 'fast'],
                        help="Engine used for the re-run: 'reference' (bar-by-bar research "
                             "path) or 'fast' (its array twin, used to prove that the twin "
                             "reproduces the stored grid)")
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    run_dir = Path(args.run)
    cells = grid_cells(run_dir)
    if not cells:
        raise SystemExit(f'no grid cells found in {run_dir}')

    if args.symbols:
        wanted = {s.strip() for s in args.symbols.split(',') if s.strip()}
        selected = [c for c in cells if c[0] in wanted]
    else:
        rng = random.Random(args.seed)
        size = min(args.sample, len(cells))
        selected = rng.sample(cells, size)

    tasks = [(str(run_dir), symbol, fast, slow, args.fixture_base, args.engine)
             for symbol, fast, slow in selected]
    if args.workers > 1:
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            rows = list(pool.map(check_cell, tasks, chunksize=8))
    else:
        rows = [check_cell(task) for task in tasks]

    stale = [r for r in rows if not r['reproduces']]
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_run': str(run_dir),
        'fixture_base': args.fixture_base,
        'engine': args.engine,
        'n_cells': len(rows),
        'n_reproducing': len(rows) - len(stale),
        'n_stale': len(stale),
        'stale': stale,
    }

    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    out_dir = Path(args.out) if args.out else Path('results') / f'{timestamp}_grid_repro'
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    write_report(out_dir, payload)
    print(f"Checked {len(rows)} cells: {len(rows) - len(stale)} reproduce, "
          f"{len(stale)} stale")
    print(f'Wrote {out_dir}/summary.md and summary.json')


if __name__ == '__main__':
    main()
