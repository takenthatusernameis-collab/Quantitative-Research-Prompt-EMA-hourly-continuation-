#!/usr/bin/env python3
"""Full EMA period combination grid runner for EMA hourly continuation.

Iterates symbols (market-cap descending, from universe/mcap_rank.json) x all valid
(P_fast, P_slow) pairs from the registered period grid in PROMPT.md §1.1:

    P in {8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}, P_fast < P_slow

Persists one result artifact set per (symbol, P_fast, P_slow) under
results/<RUNID>_grid/<SYMBOL>/P{fast}_{slow}/:

    config.json   experiment config (symbol, P_fast, P_slow, costs, fill rule, ...)
    trades.csv.gz trade blotter (gzip-compressed CSV)
    equity.csv.gz equity curve (gzip-compressed CSV)
    summary.json  net/gross metrics
    summary.md    human-readable report

Also writes results/<RUNID>_grid/run_config.json (full grid config) and
results/<RUNID>_grid/progress.json (completed cells + next unprocessed cell) to
support resume and handoff.

Usage:
    python scripts/run_grid.py --n 5                    # first 5 symbols, full grid
    python scripts/run_grid.py --n 1 --max-cells 10     # smoke test: 10 cells
    python scripts/run_grid.py --resume results/<RUNID>_grid  # resume a prior run
"""
import argparse
import gzip
import io
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from data.data_loader import load_ohlcv_csv
from signals.signals import generate_signals
from universe.universe import load_mcap_ranking, load_mcap_snapshot
from backtest.backtest import backtest_symbol
from metrics.metrics import calculate_metrics

# Registered EMA period grid (PROMPT.md §1.1). P_fast < P_slow for every valid pair.
PERIOD_GRID = [8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200]

GRID_PAIRS = [(f, s) for f, s in itertools.permutations(PERIOD_GRID, 2) if f < s]

DEFAULT_TAKER_FEE_BPS = 10.0
DEFAULT_SLIPPAGE_BPS = 2.0
DEFAULT_RR = 1.0

# Position sizing (PROMPT.md §1.6 prefers risk-based sizing so the equity
# curve is in the strategy's own currency and is comparable across symbols).
# 'risk'         : risk `risk_fraction` of equity per trade
# 'unit_notional': legacy mode, one unit of the base asset per trade
DEFAULT_SIZING = 'risk'
DEFAULT_RISK_FRACTION = 0.01
DEFAULT_MAX_NOTIONAL_MULTIPLE = 10.0

# Bulk per-cell artifacts are gzip-compressed on disk. The raw trade blotter and
# hourly equity curve are ~2 MB per cell uncompressed; a 66-cell symbol grid is
# therefore ~130 MB of CSV. Compressed they are ~4.7x smaller, which keeps the
# per-checkpoint git push inside the remote persistence budget (the workflow
# controller aborts `git push` after 30s, and building the pack for ~450 MB of
# new content alone takes ~34s on a 4-core runner). `mtime=0` keeps the bytes
# deterministic so identical cells produce identical blobs and git can delta
# them efficiently.
TRADES_FILENAME = 'trades.csv.gz'
EQUITY_FILENAME = 'equity.csv.gz'
GZIP_LEVEL = 6

ARTIFACT_LAYOUT = {
    'config': 'config.json',
    'summary_json': 'summary.json',
    'summary_md': 'summary.md',
    'trades': TRADES_FILENAME,
    'equity': EQUITY_FILENAME,
    'compression': 'gzip',
    'note': 'bulk CSV artifacts are gzip-compressed; read with gzip -dc <file> or pandas.read_csv(file, compression="gzip")',
}

CONFIG_DEFAULTS = {
    'taker_fee_bps': DEFAULT_TAKER_FEE_BPS,
    'slippage_bps': DEFAULT_SLIPPAGE_BPS,
    'rr': DEFAULT_RR,
    'stricter_trend': False,
    'min_risk_atr': False,
    'atr_threshold': 1.0,
    'conservative_exit': True,
    'sizing': DEFAULT_SIZING,
    'risk_fraction': DEFAULT_RISK_FRACTION,
    'max_notional_multiple': DEFAULT_MAX_NOTIONAL_MULTIPLE,
}


def period_pairs():
    """Return all valid (P_fast, P_slow) pairs with P_fast < P_slow."""
    return list(GRID_PAIRS)


def symbol_dir_name(symbol: str) -> str:
    return symbol.replace('/', '_')


def write_csv_gz(df: pd.DataFrame, path: Path) -> Path:
    """Write a DataFrame as a deterministic gzip-compressed CSV.

    `mtime=0` and a fixed compression level make the output byte-identical for
    identical input, so re-running a cell does not create a new git blob.
    """
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    payload = buf.getvalue().encode('utf-8')
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as fh:
        with gzip.GzipFile(filename='', mode='wb', fileobj=fh,
                           compresslevel=GZIP_LEVEL, mtime=0) as gz:
            gz.write(payload)
    return path


def read_artifact_csv(path: str | Path) -> pd.DataFrame:
    """Read a bulk artifact, transparently handling .csv and .csv.gz."""
    path = Path(path)
    if path.suffix == '.gz':
        with gzip.open(path, 'rt', encoding='utf-8') as fh:
            return pd.read_csv(fh)
    return pd.read_csv(path)


def run_cell(symbol, df, fast, slow, taker_fee_bps, slippage_bps, rr,
             stricter_trend, min_risk_atr, atr_threshold, conservative_exit,
             oos_fraction=None, sizing=DEFAULT_SIZING,
             risk_fraction=DEFAULT_RISK_FRACTION,
             max_notional_multiple=DEFAULT_MAX_NOTIONAL_MULTIPLE):
    """Run a single (symbol, P_fast, P_slow) cell. Returns (trades, equity_df, metrics).

    When `oos_fraction` is set, entries are restricted to the trailing
    (1 - oos_fraction) window of the series and the equity curve is trimmed to
    that window, so the reported metrics are out-of-sample. EMAs are still
    computed on the full (causal) series so warm-up is not lost.
    """
    df_sig = generate_signals(
        df.copy(), ema_fast_period=fast, ema_slow_period=slow,
        stricter_trend=stricter_trend,
    )
    entry_start_index = 0
    if oos_fraction is not None and 0.0 < oos_fraction < 1.0:
        entry_start_index = int(len(df_sig) * (1.0 - oos_fraction))
    trades, equity_df = backtest_symbol(
        df_sig, symbol=symbol,
        taker_fee_bps=taker_fee_bps, slippage_bps=slippage_bps, rr=rr,
        min_risk_atr=min_risk_atr, atr_threshold=atr_threshold,
        entry_start_index=entry_start_index,
        conservative_exit=conservative_exit,
        sizing=sizing, risk_fraction=risk_fraction,
        max_notional_multiple=max_notional_multiple,
    )
    if entry_start_index:
        equity_df = equity_df.iloc[entry_start_index:].reset_index(drop=True)
    metrics = calculate_metrics(trades, equity_df, symbol=symbol)
    metrics['P_fast'] = fast
    metrics['P_slow'] = slow
    metrics['symbol'] = symbol
    metrics['oos_fraction'] = oos_fraction
    metrics['entry_start_index'] = entry_start_index
    metrics['sizing'] = sizing
    metrics['risk_fraction'] = risk_fraction
    # Reconciliation check: the equity curve must equal starting equity plus
    # the sum of net trade P&L.
    metrics['equity_reconciles'] = bool(
        len(equity_df) == 0
        or abs(equity_df['equity'].iloc[-1] - (10000.0 + sum(t.pnl_net for t in trades))) < 1e-6
    )
    return trades, equity_df, metrics


def save_cell(results_dir, symbol, fast, slow, trades, equity_df, metrics,
              config):
    """Persist one artifact set for a (symbol, P_fast, P_slow) cell."""
    cell_dir = results_dir / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'
    cell_dir.mkdir(parents=True, exist_ok=True)

    cell_config = dict(config)
    cell_config.update({
        'symbol': symbol,
        'P_fast': fast,
        'P_slow': slow,
        'ema_fast_period': fast,
        'ema_slow_period': slow,
        'artifacts': ARTIFACT_LAYOUT,
    })
    with open(cell_dir / 'config.json', 'w') as f:
        json.dump(cell_config, f, indent=2, default=str)

    trades_df = pd.DataFrame([t.__dict__ for t in trades])
    write_csv_gz(trades_df, cell_dir / TRADES_FILENAME)
    write_csv_gz(equity_df, cell_dir / EQUITY_FILENAME)

    with open(cell_dir / 'summary.json', 'w') as f:
        json.dump(metrics, f, indent=2, default=str)

    lines = []
    lines.append(f'# EMA Hourly Continuation — {symbol} P{fast}_{slow}\n')
    lines.append(f'**Symbol:** {symbol}  |  **P_fast:** {fast}  |  **P_slow:** {slow}\n')
    lines.append(f'**Costs:** {config["taker_fee_bps"]} bps taker + {config["slippage_bps"]} bps slippage per side\n')
    lines.append(f'**RR:** {config["rr"]}  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow\n')
    if config.get('sizing') == 'risk':
        lines.append(f'**Sizing:** risk-based, {config["risk_fraction"]:.2%} of equity per trade '
                     f'(notional cap {config["max_notional_multiple"]}x equity)\n')
    else:
        lines.append(f'**Sizing:** {config.get("sizing")} (one unit of base asset per trade)\n')
    if metrics.get('oos_fraction'):
        lines.append(f'**Evaluation:** out-of-sample (trailing {metrics["oos_fraction"]:.0%} of bars, '
                     f'entries restricted to test window)\n')
    lines.append('\n## Metrics (net of costs)\n')
    lines.append('| Metric | Value |\n|---|---|')
    for k in ['trade_count', 'net_profit_factor', 'net_win_rate', 'gross_profit_factor',
              'gross_win_rate', 'sharpe_ratio', 'sortino_ratio', 'max_drawdown', 'cagr',
              'net_avg_win', 'net_avg_loss', 'avg_hold_time_bars', 'exposure']:
        v = metrics.get(k)
        lines.append(f'| {k} | {v:.4f} |' if isinstance(v, float) else f'| {k} | {v} |')
    pf = metrics.get('net_profit_factor', 0) or 0.0
    n = metrics.get('trade_count', 0) or 0
    if n < 10:
        label = 'rejected'
    elif pf > 1.0 and (metrics.get('sharpe_ratio', 0) or 0.0) > 0.0 and n >= 30:
        label = 'exploratory signal'
    else:
        label = 'rejected'
    lines.append(f'\nDecision label: {label}\n')
    lines.append(f'\nBulk artifacts: `{TRADES_FILENAME}`, `{EQUITY_FILENAME}` (gzip-compressed CSV). '
                 f'Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.\n')
    with open(cell_dir / 'summary.md', 'w') as f:
        f.write('\n'.join(lines))

    return cell_dir


def main():
    parser = argparse.ArgumentParser(description='Run full EMA period grid per symbol')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--n', type=int, default=5, help='Number of symbols (mcap desc) to process')
    parser.add_argument('--taker-fee-bps', type=float, default=CONFIG_DEFAULTS['taker_fee_bps'])
    parser.add_argument('--slippage-bps', type=float, default=CONFIG_DEFAULTS['slippage_bps'])
    parser.add_argument('--rr', type=float, default=CONFIG_DEFAULTS['rr'])
    parser.add_argument('--stricter-trend', action='store_true', default=CONFIG_DEFAULTS['stricter_trend'])
    parser.add_argument('--min-risk-atr', action='store_true', default=CONFIG_DEFAULTS['min_risk_atr'])
    parser.add_argument('--atr-threshold', type=float, default=CONFIG_DEFAULTS['atr_threshold'])
    parser.add_argument('--aggressive-exit', action='store_true', default=False,
                        help='Same-bar SL/TP conflict: take TP instead of conservative SL')
    parser.add_argument('--max-cells', type=int, default=None,
                        help='Stop after N cells (smoke test / partial run)')
    parser.add_argument('--resume', type=str, default=None,
                        help='Path to a prior results/<RUNID>_grid dir to resume')
    parser.add_argument('--oos-fraction', type=float, default=None,
                        help='Trailing out-of-sample fraction (e.g. 0.35). '
                             'Entries restricted to the test window; default = full sample (in-sample)')
    parser.add_argument('--sizing', type=str, default=CONFIG_DEFAULTS['sizing'],
                        choices=['risk', 'unit_notional'],
                        help="'risk' (default) risks a fixed fraction of equity per trade; "
                             "'unit_notional' is the legacy one-unit-per-trade mode")
    parser.add_argument('--risk-fraction', type=float, default=CONFIG_DEFAULTS['risk_fraction'],
                        help='Fraction of equity risked per trade when sizing=risk')
    parser.add_argument('--max-notional-multiple', type=float,
                        default=CONFIG_DEFAULTS['max_notional_multiple'],
                        help='Cap on position notional as a multiple of equity')
    parser.add_argument('--note', type=str, default=None,
                        help='Free-form note recorded in run_config.json (e.g. the universe '
                             'expansion that triggered this invocation)')
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
    if args.resume:
        results_dir = Path(args.resume)
        if not results_dir.exists():
            raise FileNotFoundError(f"Resume dir not found: {results_dir}")
        run_id = results_dir.name
    else:
        results_dir = Path('results') / f'{timestamp}_grid'
        run_id = results_dir.name
    results_dir.mkdir(parents=True, exist_ok=True)

    # Keep an audit trail of every invocation against this run directory, so a
    # resumed/expanded run still records the previous N (symbols, universe).
    prior_configs = []
    run_config_path = results_dir / 'run_config.json'
    if run_config_path.exists():
        try:
            with open(run_config_path) as f:
                prev_cfg = json.load(f)
            prior_configs = list(prev_cfg.get('history', []))
            prior_configs.append({k: v for k, v in prev_cfg.items() if k != 'history'})
        except Exception:
            prior_configs = []

    run_config = {
        'run_id': run_id,
        'timestamp': timestamp,
        'strategy': 'ema_hourly_continuation',
        'mode': 'full_ema_grid',
        'period_grid': PERIOD_GRID,
        'grid_pairs': GRID_PAIRS,
        'n_pairs': len(GRID_PAIRS),
        'config': config,
        'mcap': args.mcap,
        'fixture_base': args.fixture_base,
        'max_cells': args.max_cells,
        'resume': args.resume,
        'oos_fraction': args.oos_fraction,
        'note': args.note,
        'artifact_layout': ARTIFACT_LAYOUT,
        'history': prior_configs,
    }
    with open(results_dir / 'run_config.json', 'w') as f:
        json.dump(run_config, f, indent=2, default=str)

    # Load progress if resuming
    progress_path = results_dir / 'progress.json'
    completed = set()
    next_cell = None
    if progress_path.exists():
        try:
            with open(progress_path) as f:
                prev = json.load(f)
            completed = {(c['symbol'], c['P_fast'], c['P_slow']) for c in prev.get('completed', [])}
            next_cell = tuple(prev.get('next_cell')) if prev.get('next_cell') else None
        except Exception:
            completed = set()

    symbols = load_mcap_ranking(args.mcap)[:args.n]
    run_config['symbols'] = symbols
    run_config['n_symbols'] = len(symbols)
    # Log the universe expansion in the experiment config (PROMPT.md §2.1):
    # previous N -> new N, ranks added, ranking source and timestamp.
    mcap_snapshot = load_mcap_snapshot(args.mcap)
    run_config['mcap_snapshot'] = {k: v for k, v in mcap_snapshot.items() if k != 'symbols'}
    with open(results_dir / 'run_config.json', 'w') as f:
        json.dump(run_config, f, indent=2, default=str)

    pairs = period_pairs()
    cells_processed = 0
    stopped = False
    stop_reason = None

    # Determine iteration start: if resuming with a next_cell, skip to it.
    start_symbol_idx = 0
    start_pair_idx = 0
    if next_cell:
        nsym, nfast, nslow = next_cell
        if nsym in symbols:
            start_symbol_idx = symbols.index(nsym)
            start_pair_idx = pairs.index((nfast, nslow)) if (nfast, nslow) in pairs else 0

    for si in range(start_symbol_idx, len(symbols)):
        symbol = symbols[si]
        sym_file = Path(args.fixture_base) / f'{symbol_dir_name(symbol)}.csv'
        if not sym_file.exists():
            print(f'SKIP {symbol}: no fixture {sym_file}')
            continue
        try:
            df = load_ohlcv_csv(str(sym_file))
        except Exception as e:
            print(f'SKIP {symbol}: failed to load fixture ({e})')
            continue
        if df.empty:
            print(f'SKIP {symbol}: empty fixture')
            continue

        pair_iter = pairs if si > start_symbol_idx else pairs[start_pair_idx:]
        for (fast, slow) in pair_iter:
            cell_key = (symbol, fast, slow)
            if cell_key in completed:
                continue
            if args.max_cells is not None and cells_processed >= args.max_cells:
                stopped = True
                stop_reason = 'max_cells_reached'
                next_cell = cell_key
                break
            print(f'[{run_id}] {symbol} P{fast}_{slow} ...', flush=True)
            try:
                trades, equity_df, metrics = run_cell(
                    symbol, df, fast, slow,
                    config['taker_fee_bps'], config['slippage_bps'], config['rr'],
                    config['stricter_trend'], config['min_risk_atr'], config['atr_threshold'],
                    config['conservative_exit'], oos_fraction=args.oos_fraction,
                    sizing=config['sizing'], risk_fraction=config['risk_fraction'],
                    max_notional_multiple=config['max_notional_multiple'],
                )
                save_cell(results_dir, symbol, fast, slow, trades, equity_df, metrics, config)
                completed.add(cell_key)
                cells_processed += 1
                next_cell = cell_key
                print(f'  -> trades={metrics["trade_count"]} netPF={metrics.get("net_profit_factor",0):.4f} '
                      f'netSharpe={metrics.get("sharpe_ratio",0):.4f}', flush=True)
            except Exception as e:
                print(f'  ERROR {symbol} P{fast}_{slow}: {e}', flush=True)
                # Record blocked cell
                blocked_dir = results_dir / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'
                blocked_dir.mkdir(parents=True, exist_ok=True)
                with open(blocked_dir / 'blocked.json', 'w') as f:
                    json.dump({'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                               'reason': str(e)}, f, indent=2)
                completed.add(cell_key)
                cells_processed += 1
                next_cell = cell_key
        if stopped:
            break

    # Write progress.json
    completed_list = [{'symbol': s, 'P_fast': f, 'P_slow': p} for (s, f, p) in sorted(completed)]
    # Determine next unprocessed cell for handoff
    unprocessed = None
    for si in range(len(symbols)):
        symbol = symbols[si]
        sym_file = Path(args.fixture_base) / f'{symbol_dir_name(symbol)}.csv'
        if not sym_file.exists():
            continue
        pair_iter = pairs
        for (fast, slow) in pair_iter:
            if (symbol, fast, slow) not in completed:
                unprocessed = [symbol, fast, slow]
                break
        if unprocessed:
            break

    progress = {
        'run_id': run_id,
        'timestamp': timestamp,
        'symbols': symbols,
        'n_pairs': len(pairs),
        'n_symbols': len(symbols),
        'completed_cells': len(completed),
        'completed': completed_list,
        'next_cell': unprocessed,  # [symbol, P_fast, P_slow] or None
        'stopped': stopped,
        'stop_reason': stop_reason,
        'all_symbols_processed': unprocessed is None,
    }
    with open(progress_path, 'w') as f:
        json.dump(progress, f, indent=2, default=str)

    print(f'\nGrid run {run_id} complete.')
    print(f'Results dir: {results_dir}')
    print(f'Completed cells: {len(completed)} / {len(symbols) * len(pairs)}')
    if unprocessed:
        print(f'Next unprocessed cell: {unprocessed[0]} P{unprocessed[1]}_{unprocessed[2]}')
    else:
        print('All symbols x pairs processed. Universe expansion is next (see PROMPT.md §2.1).')


if __name__ == '__main__':
    main()
