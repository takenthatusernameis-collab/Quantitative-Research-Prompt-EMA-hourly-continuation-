#!/usr/bin/env python3
"""Parallel grid runner for a pre-registered mutation of the baseline grid.

Why this exists
---------------
PROMPT.md §5 allows ordered optional mutations, each of which has to be
recorded as *parent config -> child config -> delta metrics*. The ATR
minimum-risk mutation (PROMPT.md §5.2) is a rule change, so it needs the
whole 17 556-cell grid again, not a sample: a mutation that is only run on a
handful of symbols is a new in-sample search with a new multiple-testing
problem.

`scripts/run_grid.py` produces one symbol at a time, which needs about twelve
hours of wall clock for the full grid. This runner drives *the same engine*
(`scripts.run_grid.run_cell` and `scripts.run_grid.save_cell`) with a
process pool, so the cells it writes are the cells the serial runner writes:
same config, same artifacts, same summary metrics. It exists for mutation
runs only; the baseline grid is never re-run through it and is never
overwritten by it.

The run is durable and resumable:

* every finished cell leaves its artifact set on disk, and a cell whose
  `summary.json` already exists is skipped, so an interrupted run continues
  where it stopped;
* `progress.json` is rewritten after every symbol, in the same schema the
  serial runner uses, so the handoff can name the next unprocessed cell.

Usage:
    python scripts/run_mutation_grid.py --run results/<TS>_grid --min-risk-atr \
        --workers 4
    python scripts/run_mutation_grid.py --run results/<TS>_grid --min-risk-atr \
        --workers 4 --n 5          # first 5 symbols by market cap (smoke test)
"""
import argparse
import json
import multiprocessing as mp
import signal
import sys
from datetime import datetime, timezone
from pathlib import Path

from data.data_loader import load_ohlcv_csv
from scripts.run_grid import (CONFIG_DEFAULTS, period_pairs, run_cell, save_cell,
                              symbol_dir_name)
from universe.universe import load_mcap_ranking, load_mcap_snapshot


def cell_dir_for(results_dir: Path, symbol: str, fast: int, slow: int) -> Path:
    """Directory of one (symbol, P_fast, P_slow) cell of a run."""
    return results_dir / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'


def run_symbol(job: dict) -> dict:
    """Run the full period grid of one symbol.

    Cells whose `summary.json` already exists are skipped, which is what
    makes the run resumable. A cell that raises is recorded as blocked, the
    same way `scripts/run_grid.py` records it.
    """
    results_dir = Path(job['results_dir'])
    symbol = job['symbol']
    config = job['config']
    pairs = period_pairs()
    done = []
    errors = []

    sym_file = Path(job['fixture_base']) / f'{symbol_dir_name(symbol)}.csv'
    if not sym_file.exists():
        return {'symbol': symbol, 'cells': [], 'errors': [f'no fixture {sym_file}']}
    try:
        df = load_ohlcv_csv(str(sym_file))
    except Exception as exc:  # pragma: no cover - defensive
        return {'symbol': symbol, 'cells': [],
                'errors': [f'failed to load fixture ({exc})']}
    if df.empty:
        return {'symbol': symbol, 'cells': [], 'errors': ['empty fixture']}

    for fast, slow in pairs:
        cell_dir = cell_dir_for(results_dir, symbol, fast, slow)
        if (cell_dir / 'summary.json').exists():
            done.append((symbol, fast, slow))
            continue
        try:
            trades, equity_df, metrics = run_cell(
                symbol, df, fast, slow,
                config['taker_fee_bps'], config['slippage_bps'], config['rr'],
                config['stricter_trend'], config['min_risk_atr'],
                config['atr_threshold'], config['conservative_exit'],
                oos_fraction=None, sizing=config['sizing'],
                risk_fraction=config['risk_fraction'],
                max_notional_multiple=config['max_notional_multiple'],
            )
            save_cell(results_dir, symbol, fast, slow, trades, equity_df,
                      metrics, config)
            done.append((symbol, fast, slow))
        except Exception as exc:
            cell_dir.mkdir(parents=True, exist_ok=True)
            with open(cell_dir / 'blocked.json', 'w') as fh:
                json.dump({'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                           'reason': str(exc)}, fh, indent=2)
            done.append((symbol, fast, slow))
            errors.append(f'P{fast}_{slow}: {exc}')
    return {'symbol': symbol, 'cells': done, 'errors': errors}


def scan_completed(results_dir: Path, symbols: list) -> set:
    """Every cell of the run that already has a summary on disk."""
    completed = set()
    for symbol in symbols:
        for fast, slow in period_pairs():
            if (cell_dir_for(results_dir, symbol, fast, slow) / 'summary.json').exists():
                completed.add((symbol, fast, slow))
    return completed


def write_progress(results_dir: Path, run_id: str, timestamp: str,
                   covered: list, completed: set, n_pairs: int) -> dict:
    """Write `progress.json` in the schema `scripts/run_grid.py` uses."""
    pairs = period_pairs()
    unprocessed = None
    for symbol in covered:
        for fast, slow in pairs:
            if (symbol, fast, slow) not in completed:
                unprocessed = [symbol, fast, slow]
                break
        if unprocessed:
            break
    progress = {
        'run_id': run_id,
        'timestamp': timestamp,
        'symbols': covered,
        'invocation_symbols': covered,
        'n_pairs': n_pairs,
        'n_symbols': len(covered),
        'completed_cells': len(completed),
        'completed': [{'symbol': s, 'P_fast': f, 'P_slow': p}
                      for (s, f, p) in sorted(completed)],
        'next_cell': unprocessed,
        'stopped': unprocessed is not None,
        'stop_reason': None if unprocessed is None else 'in_progress',
        'all_symbols_processed': unprocessed is None,
    }
    with open(results_dir / 'progress.json', 'w') as fh:
        json.dump(progress, fh, indent=2)
    return progress


def main():
    parser = argparse.ArgumentParser(
        description='Parallel full-grid runner for a pre-registered mutation')
    parser.add_argument('--run', type=str, default=None,
                        help='results/<RUNID>_grid directory (default: new run)')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--n', type=int, default=0,
                        help='symbols to process, market-cap descending (0 = all)')
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--taker-fee-bps', type=float, default=CONFIG_DEFAULTS['taker_fee_bps'])
    parser.add_argument('--slippage-bps', type=float, default=CONFIG_DEFAULTS['slippage_bps'])
    parser.add_argument('--rr', type=float, default=CONFIG_DEFAULTS['rr'])
    parser.add_argument('--stricter-trend', action='store_true',
                        default=CONFIG_DEFAULTS['stricter_trend'])
    parser.add_argument('--min-risk-atr', action='store_true',
                        default=CONFIG_DEFAULTS['min_risk_atr'])
    parser.add_argument('--atr-threshold', type=float,
                        default=CONFIG_DEFAULTS['atr_threshold'])
    parser.add_argument('--aggressive-exit', action='store_true', default=False)
    parser.add_argument('--sizing', type=str, default=CONFIG_DEFAULTS['sizing'],
                        choices=['risk', 'unit_notional'])
    parser.add_argument('--risk-fraction', type=float,
                        default=CONFIG_DEFAULTS['risk_fraction'])
    parser.add_argument('--max-notional-multiple', type=float,
                        default=CONFIG_DEFAULTS['max_notional_multiple'])
    parser.add_argument('--note', type=str, default=None)
    parser.add_argument('--parent-run', type=str, default=None,
                        help='the baseline grid directory this run mutates; '
                             'recorded in run_config.json as parent -> child')
    args = parser.parse_args()

    config = dict(CONFIG_DEFAULTS)
    config.update({
        'taker_fee_bps': args.taker_fee_bps,
        'slippage_bps': args.slippage_bps,
        'rr': args.rr,
        'stricter_trend': args.stricter_trend,
        'min_risk_atr': args.min_risk_atr,
        'atr_threshold': args.atr_threshold,
        'conservative_exit': not args.aggressive_exit,
        'sizing': args.sizing,
        'risk_fraction': args.risk_fraction,
        'max_notional_multiple': args.max_notional_multiple,
    })

    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    if args.run:
        results_dir = Path(args.run)
        results_dir.mkdir(parents=True, exist_ok=True)
        run_id = results_dir.name
    else:
        results_dir = Path('results') / f'{timestamp}_grid'
        results_dir.mkdir(parents=True, exist_ok=True)
        run_id = results_dir.name

    symbols = load_mcap_ranking(args.mcap)
    if args.n:
        symbols = symbols[:args.n]
    pairs = period_pairs()

    run_config = {
        'run_id': run_id,
        'timestamp': timestamp,
        'strategy': 'ema_hourly_continuation',
        'mode': 'full_ema_grid_mutation',
        'runner': 'scripts/run_mutation_grid.py',
        'period_grid': [8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200],
        'n_pairs': len(pairs),
        'config': config,
        'mcap': args.mcap,
        'fixture_base': args.fixture_base,
        'symbols': symbols,
        'n_symbols': len(symbols),
        'workers': args.workers,
        'note': args.note,
        'parent_run': args.parent_run,
        'mcap_snapshot': {k: v for k, v in load_mcap_snapshot(args.mcap).items()
                          if k != 'symbols'},
    }
    with open(results_dir / 'run_config.json', 'w') as fh:
        json.dump(run_config, fh, indent=2, default=str)

    completed = scan_completed(results_dir, symbols)
    print(f'Run {run_id}: {len(symbols)} symbols x {len(pairs)} pairs, '
          f'{len(completed)} cell(s) already on disk, {args.workers} worker(s).',
          flush=True)

    stopping = {'flag': False}

    def _stop(signum, frame):  # pragma: no cover - signal path
        stopping['flag'] = True
        print('Signal received; finishing the running symbols and writing '
              'progress.json.', flush=True)

    signal.signal(signal.SIGTERM, _stop)
    signal.signal(signal.SIGINT, _stop)

    jobs = [{'results_dir': str(results_dir), 'symbol': symbol,
             'fixture_base': args.fixture_base, 'config': config}
            for symbol in symbols]
    errors = []
    if args.workers > 1:
        ctx = mp.get_context('fork')
        with ctx.Pool(processes=args.workers) as pool:
            for result in pool.imap_unordered(run_symbol, jobs):
                completed.update(result['cells'])
                errors.extend(f"{result['symbol']} {e}" for e in result['errors'])
                write_progress(results_dir, run_id, timestamp, symbols,
                               completed, len(pairs))
                print(f"[{run_id}] {result['symbol']}: "
                      f"{len(result['cells'])} cell(s) done, "
                      f"{len(completed)}/{len(symbols) * len(pairs)} total",
                      flush=True)
                if stopping['flag']:
                    pool.terminate()
                    break
    else:
        for job in jobs:
            if stopping['flag']:
                break
            result = run_symbol(job)
            completed.update(result['cells'])
            errors.extend(f"{result['symbol']} {e}" for e in result['errors'])
            write_progress(results_dir, run_id, timestamp, symbols, completed,
                           len(pairs))
            print(f"[{run_id}] {result['symbol']}: {len(result['cells'])} cell(s) done, "
                  f"{len(completed)}/{len(symbols) * len(pairs)} total", flush=True)

    progress = write_progress(results_dir, run_id, timestamp, symbols, completed,
                              len(pairs))
    if errors:
        with open(results_dir / 'errors.log', 'w') as fh:
            fh.write('\n'.join(errors) + '\n')
    print(f'Run {run_id} finished: {len(completed)}/{len(symbols) * len(pairs)} '
          f'cells, next_cell={progress["next_cell"]}', flush=True)


if __name__ == '__main__':
    main()
