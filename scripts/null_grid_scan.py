#!/usr/bin/env python3
"""Randomized-entry null for the EMA hourly continuation grid.

What this leg adds
------------------
The program now knows how many grid cells *look* good out of sample (77 of
17 556 in the last audit) and how many survive the 2x cost stress (6). What
it still does not know is how many cells would look good **if the entry rule
carried no information at all**. Without that reference point, "6 survivors
out of 17 556" cannot be read: it is only remarkable if random entry timing
produces far fewer.

This harness builds that reference point by *randomizing the rule itself* and
re-running the untouched backtest engine:

    timing null   the same number of entries, at uniformly random bars, with
                  the same multiset of directions. The market path, the EMA
                  geometry, the risk distances and the cost model are
                  unchanged; only *when* the rule fires is destroyed.
    sign null     the same entry bars, but every direction redrawn from a
                  fair coin. The timing, the entry prices and the risk
                  distances are unchanged; only *which way* the rule trades
                  is destroyed.

Each null realization is run through `backtest.backtest.backtest_symbol` with
the registered costs, so the null is produced by the same code that produced
the real numbers - a null computed by a different model would not be
comparable.

Why the out-of-sample window
-----------------------------
Every number here is computed on the same trailing 35 % out-of-sample window
the program uses as its final holdout, with entries restricted to the window.
A cell whose entry timing carries no information is exactly a cell that would
have been found by luck, and 17 556 lucky draws do not stay lucky.

What the leg reports
--------------------
1. The null distribution of the per-cell out-of-sample net PF, grid-wide, and
   the number of null cells that clear the PROMPT.md §3.4 gates. This is the
   false-positive rate of the gate itself.
2. The family-wise reading of the observed tail: the best cell of the grid
   against the best cell of the null grid, and the number of null cells that
   reach the observed best.
3. Per-cell empirical p-values for the cells that survived the audit, each
   tested against its own randomizations and corrected for the 17 556 tests
   the program ran.
4. A paired comparison, cell by cell: how often the real rule beats its own
   null realization.

Usage:
    python scripts/null_grid_scan.py --run results/20261019_135940_grid
    python scripts/null_grid_scan.py --run results/20261019_135940_grid \
        --survivors-from results/20261021_005234_oos_grid_scan \
        --survivor-replicates 50 --control-sample 100
    python scripts/null_grid_scan.py --run results/20261019_135940_grid \
        --limit-symbols 3 --workers 1          # smoke test
"""
import argparse
import json
import math
import os
import zlib
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from backtest.backtest import backtest_symbol
from data.data_loader import load_ohlcv_csv
from metrics.metrics import calculate_metrics
from scripts.oos_grid_scan import (describe_distribution, entry_start_index,
                                    net_profit_factor, stressed_pnl_net)
from scripts.run_grid import CONFIG_DEFAULTS, GRID_PAIRS
from signals.signals import generate_signals, generate_signals_vectorized

NULL_MODES = ('block', 'timing', 'sign')

# Length of the block the local null shuffles inside (240 hourly bars = 10
# days). The block keeps the null inside the same stretch of the market as
# the real entry, so the risk distance and the cost drag stay comparable.
DEFAULT_BLOCK_BARS = 240

# The §3.4 gate, restricted to the out-of-sample window. The full-sample leg
# of the real gate is reported from the stored grid summaries; the null has no
# stored summary, so the null is scored on the window leg alone. That makes
# the null's pass rate an upper bound on the null's full-gate pass rate.
GATE_DESCRIPTION = ('out-of-sample net PF > 1, out-of-sample Sharpe > 0, '
                    'at least min_trades out-of-sample trades, and out-of-sample '
                    'net PF still > 1 under the cost stress')


def cell_seed(*parts) -> int:
    """Deterministic per-cell seed.

    The seed is derived from the cell identity, never from the worker or the
    run order, so the artifact is reproducible no matter how the work was
    scheduled across processes.
    """
    key = '|'.join(str(p) for p in parts)
    return zlib.crc32(key.encode('utf-8')) & 0xFFFFFFFF


def eligible_bars(n_bars: int, fast: int, slow: int) -> np.ndarray:
    """Bars on which the rule is allowed to fire.

    The reference signal generator starts its loop at the warm-up bar
    `max(P_fast, P_slow)`, so a null entry can never be placed before it.
    """
    warmup = max(fast, slow)
    return np.arange(warmup, n_bars)


def null_entries(entry_idx: np.ndarray, sides: np.ndarray, eligible: np.ndarray,
                 rng: np.random.Generator, mode: str,
                 block_bars: int = 240) -> tuple:
    """Entry bars and directions of one null realization.

    `timing` keeps the number of entries and the multiset of directions but
    places them at uniformly random bars over the whole series. `sign` keeps
    the entry bars and redraws every direction from a fair coin. `block`
    keeps the number of entries, the direction mix and the local market
    context, and moves every entry to a random bar inside its own block: the
    entry stops being a cross but stays in the same stretch of the market,
    which is what makes its risk distance comparable to the real rule's.
    """
    if mode == 'timing':
        k = int(entry_idx.size)
        if k == 0:
            return np.array([], dtype=int), np.array([], dtype=float)
        if k > eligible.size:
            raise ValueError('more entries than eligible bars')
        positions = np.sort(rng.choice(eligible, size=k, replace=False))
        return positions, rng.permutation(sides)
    if mode == 'sign':
        if entry_idx.size == 0:
            return np.array([], dtype=int), np.array([], dtype=float)
        directions = np.where(rng.random(entry_idx.size) < 0.5, 1.0, -1.0)
        return entry_idx, directions
    if mode == 'block':
        if entry_idx.size == 0:
            return np.array([], dtype=int), np.array([], dtype=float)
        blocks = entry_idx // block_bars
        positions = np.empty(entry_idx.size, dtype=int)
        directions = np.empty(entry_idx.size, dtype=float)
        for block in np.unique(blocks):
            members = np.flatnonzero(blocks == block)
            start = int(block) * block_bars
            stop = min(start + block_bars, int(eligible[-1]) + 1)
            candidates = np.arange(max(start, int(eligible[0])), stop)
            k = int(members.size)
            if candidates.size < k:
                positions[members] = entry_idx[members]
                directions[members] = sides[members]
                continue
            positions[members] = np.sort(rng.choice(candidates, size=k, replace=False))
            directions[members] = rng.permutation(sides[members])
        order = np.argsort(positions, kind='stable')
        return positions[order], directions[order]
    raise ValueError(f'unknown null mode: {mode}')


def apply_entries(frame: pd.DataFrame, positions: np.ndarray,
                  directions: np.ndarray) -> pd.DataFrame:
    """Return a copy of the frame whose signal column is the null entry set."""
    null = frame.copy()
    null['signal'] = 0.0
    null['entry_price'] = np.nan
    if positions.size:
        null.loc[positions, 'signal'] = directions
        null.loc[positions, 'entry_price'] = null['close'].to_numpy()[positions]
    return null


def window_stats(frame: pd.DataFrame, entry_start: int, config: dict,
                 symbol: str) -> dict:
    """Out-of-sample statistics of one frame, on the trailing window only.

    The engine is given the window and asked for entries from its first bar.
    Restricting the data is equivalent to running the full series with
    `entry_start_index` set to the window start: entries before the window are
    gated in both cases, so the equity never moves before the window and the
    in-window trades are identical. `validate_window_equivalence` checks that
    claim on a sample of real cells.
    """
    window = frame.iloc[entry_start:].reset_index(drop=True)
    trades, equity_df = backtest_symbol(
        window, symbol=symbol,
        taker_fee_bps=config['taker_fee_bps'], slippage_bps=config['slippage_bps'],
        rr=config['rr'], min_risk_atr=config['min_risk_atr'],
        atr_threshold=config['atr_threshold'], entry_start_index=0,
        conservative_exit=config['conservative_exit'], sizing=config['sizing'],
        risk_fraction=config['risk_fraction'],
        max_notional_multiple=config['max_notional_multiple'],
    )
    metrics = calculate_metrics(trades, equity_df, symbol=symbol)
    return summarize_trades(trades, metrics, config['stress_multiplier'])


def summarize_trades(trades: list, metrics: dict, stress_multiplier: float) -> dict:
    """Net statistics of a trade list, with the cost stress applied."""
    pnl_net = np.array([t.pnl_net for t in trades], dtype=float)
    entry_cost = np.array([t.entry_cost for t in trades], dtype=float)
    exit_cost = np.array([t.exit_cost for t in trades], dtype=float)
    stress = stressed_pnl_net(pnl_net, entry_cost, exit_cost, stress_multiplier)
    risk_pct = np.array([getattr(t, 'risk_pct', np.nan) for t in trades], dtype=float)
    gross = np.array([t.pnl for t in trades], dtype=float)
    return {
        'trades': int(len(trades)),
        'net_pf': net_profit_factor(pnl_net),
        # The gross profit factor ignores the cost drag, so it separates the
        # question "does the entry timing carry information" from the question
        # "does this entry geometry pay more in fees than the null's".
        'gross_pf': net_profit_factor(gross),
        'stress_net_pf': net_profit_factor(stress),
        'net_pnl': float(pnl_net.sum()) if len(trades) else 0.0,
        'stress_net_pnl': float(stress.sum()) if len(trades) else 0.0,
        'sharpe': metrics.get('sharpe_ratio'),
        'net_win_rate': metrics.get('net_win_rate'),
        # The risk distance as a share of the entry price. The cost drag of a
        # trade scales with 1 / risk, so this is the statistic that tells
        # whether a null and the real rule pay the same kind of cost.
        'median_risk_pct': (float(np.nanmedian(risk_pct))
                            if risk_pct.size and np.isfinite(risk_pct).any()
                            else None),
    }


def passes_gate(stats: dict, min_trades: int) -> bool:
    """The out-of-sample leg of the PROMPT.md §3.4 gate."""
    return bool(
        (stats.get('trades') or 0) >= min_trades
        and (stats.get('net_pf') or 0.0) > 1.0
        and (stats.get('sharpe') or 0.0) > 0.0
        and (stats.get('stress_net_pf') or 0.0) > 1.0
    )


def process_cell(symbol: str, df: pd.DataFrame, fast: int, slow: int,
                 opts: dict) -> dict:
    """Real cell plus one null realization per mode."""
    config = opts['config']
    frame = generate_signals_vectorized(df, fast, slow, config['stricter_trend'])
    signal = frame['signal'].to_numpy()
    entry_idx = np.flatnonzero(signal != 0)
    sides = signal[entry_idx]
    entry_start = entry_start_index(len(frame), opts['oos_fraction'])
    eligible = eligible_bars(len(frame), fast, slow)

    real = window_stats(frame, entry_start, config, symbol)
    row = {
        'symbol': symbol,
        'P_fast': fast,
        'P_slow': slow,
        'n_bars': int(len(frame)),
        'entry_start_index': entry_start,
        'n_signals': int(entry_idx.size),
        'real': real,
        'null': {},
    }
    for mode in opts['modes']:
        rng = np.random.default_rng(cell_seed(symbol, fast, slow, mode, 0))
        positions, directions = null_entries(entry_idx, sides, eligible, rng, mode,
                                             opts.get('block_bars', DEFAULT_BLOCK_BARS))
        null_frame = apply_entries(frame, positions, directions)
        row['null'][mode] = window_stats(null_frame, entry_start, config, symbol)
    return row


def validate_window_equivalence(symbol: str, df: pd.DataFrame, fast: int, slow: int,
                                opts: dict) -> dict:
    """Check the window restriction against a full-history run of the same cell.

    The bulk of the leg runs on the trailing window only. This re-runs the
    cell three ways and compares them:

    * over the whole history, the way the grid runner ran it, to confirm the
      harness reproduces the stored grid summary;
    * over the whole history with the entries gated at the window start, which
      is the grid runner's own out-of-sample leg;
    * over the window only, which is what the bulk of this leg does.

    The last two must produce the same in-window trades.
    """
    config = opts['config']
    run_dir = Path(opts['run'])
    cell_dir = run_dir / 'results' / symbol.replace('/', '_') / f'P{fast}_{slow}'
    stored = json.loads((cell_dir / 'summary.json').read_text())

    def _run(frame, entry_index):
        trades, equity_df = backtest_symbol(
            frame, symbol=symbol,
            taker_fee_bps=config['taker_fee_bps'], slippage_bps=config['slippage_bps'],
            rr=config['rr'], min_risk_atr=config['min_risk_atr'],
            atr_threshold=config['atr_threshold'], entry_start_index=entry_index,
            conservative_exit=config['conservative_exit'], sizing=config['sizing'],
            risk_fraction=config['risk_fraction'],
            max_notional_multiple=config['max_notional_multiple'],
        )
        return trades, calculate_metrics(trades, equity_df, symbol=symbol)

    reference_frame = generate_signals(df.copy(), fast, slow, config['stricter_trend'])
    entry_start = entry_start_index(len(reference_frame), opts['oos_fraction'])

    # The grid runner's run: the whole history, every entry allowed.
    all_trades, all_metrics = _run(reference_frame, 0)
    # The grid runner's out-of-sample leg: entries gated at the window start.
    gated_trades, _ = _run(reference_frame, entry_start)
    in_window = [t for t in gated_trades if t.bar_index >= entry_start]
    # The windowed run the bulk of this leg uses.
    window = reference_frame.iloc[entry_start:].reset_index(drop=True)
    trades, window_metrics = _run(window, 0)

    vector_frame = generate_signals_vectorized(df.copy(), fast, slow,
                                                config['stricter_trend'])
    same_signals = bool(np.array_equal(vector_frame['signal'].to_numpy(),
                                       reference_frame['signal'].to_numpy()))

    def _pf(trades_list):
        pnl = np.array([t.pnl_net for t in trades_list], dtype=float)
        return net_profit_factor(pnl)

    return {
        'symbol': symbol,
        'P_fast': fast,
        'P_slow': slow,
        'stored_net_pf': stored.get('net_profit_factor'),
        'recomputed_full_net_pf': all_metrics.get('net_profit_factor'),
        'stored_trade_count': stored.get('trade_count'),
        'recomputed_full_trade_count': all_metrics.get('trade_count'),
        'windowed_oos_pf': _pf(trades),
        'full_history_oos_pf': _pf(in_window),
        'windowed_oos_trades': len(trades),
        'full_history_oos_trades': len(in_window),
        'vectorized_matches_reference': same_signals,
        'summary_matches': bool(
            abs(float(stored.get('net_profit_factor') or 0.0)
                - float(all_metrics.get('net_profit_factor') or 0.0)) <= 1e-9
            and int(stored.get('trade_count') or 0) == len(all_trades)),
        'window_matches': bool(
            abs((_pf(trades) or 0.0) - (_pf(in_window) or 0.0)) <= 1e-12
            and len(trades) == len(in_window)),
    }


def survivor_replicates(symbol: str, df: pd.DataFrame, fast: int, slow: int,
                         opts: dict, replicates: int) -> dict:
    """Per-cell null distribution: many randomizations of the same cell."""
    config = opts['config']
    frame = generate_signals_vectorized(df, fast, slow, config['stricter_trend'])
    signal = frame['signal'].to_numpy()
    entry_idx = np.flatnonzero(signal != 0)
    sides = signal[entry_idx]
    entry_start = entry_start_index(len(frame), opts['oos_fraction'])
    eligible = eligible_bars(len(frame), fast, slow)
    real = window_stats(frame, entry_start, config, symbol)

    out = {'symbol': symbol, 'P_fast': fast, 'P_slow': slow, 'real': real,
           'n_bars': int(len(frame)), 'replicates': replicates, 'modes': {}}
    for mode in opts['modes']:
        pfs = []
        stress_pfs = []
        trades = []
        gate_hits = 0
        for rep in range(replicates):
            rng = np.random.default_rng(cell_seed(symbol, fast, slow, mode, rep + 1))
            positions, directions = null_entries(entry_idx, sides, eligible, rng, mode,
                                                 opts.get('block_bars', DEFAULT_BLOCK_BARS))
            null_frame = apply_entries(frame, positions, directions)
            stats = window_stats(null_frame, entry_start, config, symbol)
            pfs.append(stats['net_pf'])
            stress_pfs.append(stats['stress_net_pf'])
            trades.append(stats['trades'])
            gate_hits += int(passes_gate(stats, opts['min_trades']))
        finite = [p for p in pfs if p is not None and math.isfinite(p)]
        observed = real['net_pf']
        exceed = sum(1 for p in pfs
                      if p is not None and observed is not None and math.isfinite(observed)
                      and p >= observed)
        stress_exceed = sum(1 for p in stress_pfs
                            if p is not None and observed is not None
                            and math.isfinite(observed) and p >= observed)
        out['modes'][mode] = {
            'null_pf_mean': float(np.mean(finite)) if finite else None,
            'null_pf_median': float(np.median(finite)) if finite else None,
            'null_pf_max': float(np.max(finite)) if finite else None,
            'null_pf_p95': float(np.percentile(finite, 95)) if finite else None,
            'null_trades_mean': float(np.mean(trades)) if trades else None,
            'null_gate_pass_rate': gate_hits / replicates if replicates else None,
            'exceed_observed': exceed,
            'exceed_observed_stress': stress_exceed,
            'p_value': (1.0 + exceed) / (replicates + 1.0),
            'p_value_stress': (1.0 + stress_exceed) / (replicates + 1.0),
            'null_pf': pfs,
            'null_stress_pf': stress_pfs,
            'null_trades': trades,
        }
    return out


def binomial_tail(successes: int, trials: int, p: float = 0.5) -> float:
    """Two-sided exact binomial p-value against a fair coin.

    Implemented here because scipy is not available in this environment.
    """
    if trials == 0:
        return 1.0
    k = min(successes, trials - successes)
    tail = 0.0
    for i in range(k + 1):
        tail += math.comb(trials, i) * (0.5 ** trials)
    return min(1.0, 2.0 * tail)


def _worker(task):
    """Process every pair of one symbol (the fixture is loaded once)."""
    symbol, pairs, opts = task
    path = Path(opts['fixture_base']) / f"{symbol.replace('/', '_')}.csv"
    df = load_ohlcv_csv(path)
    rows = []
    for fast, slow in pairs:
        rows.append(process_cell(symbol, df, fast, slow, opts))
    return rows


def _survivor_worker(task):
    symbol, pairs, opts, replicates = task
    path = Path(opts['fixture_base']) / f"{symbol.replace('/', '_')}.csv"
    df = load_ohlcv_csv(path)
    rows = []
    for fast, slow in pairs:
        rows.append(survivor_replicates(symbol, df, fast, slow, opts, replicates))
    return rows


def _validate_worker(task):
    symbol, pairs, opts = task
    path = Path(opts['fixture_base']) / f"{symbol.replace('/', '_')}.csv"
    df = load_ohlcv_csv(path)
    return [validate_window_equivalence(symbol, df, fast, slow, opts)
            for fast, slow in pairs]


def grid_cells(run_dir: Path) -> list:
    """The (symbol, P_fast, P_slow) cells of a grid run, in run order."""
    cells = []
    for sym_dir in sorted((run_dir / 'results').iterdir()):
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


def survivor_cells(audit_dir: Path, min_trades: int, min_pf: float) -> list:
    """Cells the out-of-sample audit kept, read from its artifact."""
    path = Path(audit_dir) / 'cells.jsonl'
    if not path.exists():
        return []
    out = []
    with open(path) as fh:
        for line in fh:
            row = json.loads(line)
            if (row.get('oos_trades') or 0) < min_trades:
                continue
            if (row.get('oos_net_pf') or 0.0) <= min_pf:
                continue
            out.append((row['symbol'], int(row['P_fast']), int(row['P_slow'])))
    return out


def build_grid_summary(rows: list, modes: list, min_trades: int) -> dict:
    """Aggregate the per-cell real and null results into the leg summary."""
    grid_summary = {
        'real_pf_distribution': describe_distribution([r['real']['net_pf'] for r in rows]),
        'real_pf_gt_1': sum(1 for r in rows if (r['real']['net_pf'] or 0.0) > 1.0),
        'real_gate': sum(1 for r in rows if passes_gate(r['real'], min_trades)),
        'real_max_pf': max((r['real']['net_pf'] for r in rows
                            if r['real']['net_pf'] is not None
                            and math.isfinite(r['real']['net_pf'])), default=None),
        'real_pooled_pf': pooled_ratio(rows, 'real', 'net_pf'),
        'real_gross_pf_distribution': describe_distribution(
            [r['real'].get('gross_pf') for r in rows]),
        'real_gross_pf_gt_1': sum(
            1 for r in rows if (r['real'].get('gross_pf') or 0.0) > 1.0),
        'real_median_risk_pct': median_of(
            [r['real'].get('median_risk_pct') for r in rows]),
        'real_median_trades': median_of([r['real'].get('trades') for r in rows]),
    }
    for mode in modes:
        grid_summary[f'{mode}_null_gross_pf_distribution'] = describe_distribution(
            [r['null'][mode].get('gross_pf') for r in rows])
        grid_summary[f'{mode}_null_gross_pf_gt_1'] = sum(
            1 for r in rows if (r['null'][mode].get('gross_pf') or 0.0) > 1.0)
        grid_summary[f'{mode}_null_median_risk_pct'] = median_of(
            [r['null'][mode].get('median_risk_pct') for r in rows])
        grid_summary[f'{mode}_null_median_trades'] = median_of(
            [r['null'][mode].get('trades') for r in rows])
        grid_summary[f'{mode}_null_pf_distribution'] = describe_distribution(
            [r['null'][mode]['net_pf'] for r in rows])
        grid_summary[f'{mode}_null_pf_gt_1'] = sum(
            1 for r in rows if (r['null'][mode]['net_pf'] or 0.0) > 1.0)
        grid_summary[f'{mode}_null_gate'] = sum(
            1 for r in rows if passes_gate(r['null'][mode], min_trades))
        grid_summary[f'{mode}_null_max_pf'] = max(
            (r['null'][mode]['net_pf'] for r in rows
             if r['null'][mode]['net_pf'] is not None
             and math.isfinite(r['null'][mode]['net_pf'])), default=None)
        grid_summary[f'{mode}_null_pooled_pf'] = pooled_ratio(rows, 'null', mode, 'net_pf')

    # Family-wise reading of the observed best cell, against the primary null.
    primary_mode = modes[0]
    grid_summary['primary_null_mode'] = primary_mode
    real_max = grid_summary['real_max_pf']
    primary_null = [r['null'][primary_mode]['net_pf'] for r in rows]
    finite_null = [p for p in primary_null if p is not None and math.isfinite(p)]
    n_cells = len(rows)
    exceed = sum(1 for p in finite_null if real_max is not None and p >= real_max)
    q = exceed / n_cells if n_cells else 0.0
    grid_summary['timing_null_at_or_above_best'] = exceed
    grid_summary['family_wise_p_value'] = 1.0 - (1.0 - q) ** n_cells if n_cells else 1.0

    beats = sum(1 for r in rows
                if (r['real']['net_pf'] or 0.0) > (r['null'][primary_mode]['net_pf'] or 0.0))
    grid_summary['n_real_beats_timing_null'] = beats
    grid_summary['sign_test_p_value'] = binomial_tail(beats, n_cells)
    gross_beats = sum(
        1 for r in rows
        if (r['real'].get('gross_pf') or 0.0) > (r['null'][primary_mode].get('gross_pf') or 0.0))
    grid_summary['n_real_beats_null_on_gross_pf'] = gross_beats
    grid_summary['gross_sign_test_p_value'] = binomial_tail(gross_beats, n_cells)
    return grid_summary


def write_report(out_dir: Path, payload: dict) -> None:
    """The human-readable leg report."""
    lines = []
    lines.append('# Randomized-Entry Null — EMA Hourly Continuation Grid\n')
    lines.append(f"**Source run:** `{payload['source_run']}`")
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Universe:** {payload['n_symbols']} symbols, {payload['n_cells']} grid cells")
    lines.append(f"**Out-of-sample window:** trailing {payload['oos_fraction']:.0%} of each "
                 f"symbol's bars, entries restricted to the window")
    lines.append(f"**Cost stress:** {payload['stress_multiplier']:g}x fees and slippage\n")

    lines.append('## What the leg asks\n')
    lines.append('How many of the 17 556 cells would clear the out-of-sample gates if the '
                 'entry rule carried no information? The null keeps the market path, the EMA '
                 'geometry, the risk distances and the cost model, and destroys only the '
                 'part of the rule under test:\n')
    lines.append(f"- **block** - the same number of entries, with the same direction mix, "
                 f"moved to random bars inside their own {payload.get('block_bars', 240)}-bar "
                 f"block. The entry stops being a cross but stays in the same stretch of "
                 f"the market, so the risk distance and the cost drag stay comparable.")
    lines.append('- **timing** - the same number of entries, at uniformly random bars over the '
                 'whole series, with the same multiset of directions.')
    lines.append('- **sign** - the same entry bars, with every direction redrawn from a '
                 'fair coin.\n')
    lines.append('Both are run through the untouched backtest engine, so the null is produced '
                 'by the same code that produced the real numbers.\n')

    validation = payload['validation']
    lines.append('## Leg 0 — The harness reproduces the grid run\n')
    lines.append('| Check | Result |')
    lines.append('|---|---|')
    lines.append(f"| Cells re-run on the full history | {validation['n_cells']} |")
    lines.append(f"| Recomputed full-sample net PF equals the stored grid summary | "
                 f"{validation['n_summary_matches']} of {validation['n_cells']} |")
    lines.append(f"| Windowed run equals the full-history in-window trades | "
                 f"{validation['n_window_matches']} of {validation['n_cells']} |")
    lines.append(f"| Vectorized signal generator equals the reference generator | "
                 f"{validation['n_signals_match']} of {validation['n_cells']} |")
    lines.append('')

    grid = payload['grid']
    grid_modes = [m for m in payload['modes'] if f'{m}_null_pf_distribution' in grid]
    survivor_modes = [m for m in payload['survivor_modes']]
    lines.append('## Leg 1 — The null grid\n')
    if grid_modes:
        header = ' | '.join(f'{m} null' for m in grid_modes)
        sep = '|'.join('---' for _ in grid_modes)
        lines.append(f'| Statistic | Real rule | {header} |')
        lines.append(f'|---|---|{sep}|')
        for label, key in (('mean out-of-sample net PF', 'mean'),
                           ('median out-of-sample net PF', 'median'),
                           ('p95 out-of-sample net PF', 'p95'),
                           ('max out-of-sample net PF', 'max')):
            real_v = grid['real_pf_distribution'].get(key)
            cells_text = ' | '.join(fmt(grid[f'{m}_null_pf_distribution'].get(key))
                                    for m in grid_modes)
            lines.append(f'| {label} | {fmt(real_v)} | {cells_text} |')
        lines.append('')
        lines.append(f'| Gate (out-of-sample leg) | Real rule | {header} |')
        lines.append(f'|---|---|{sep}|')
        lines.append(f"| Cells with out-of-sample net PF > 1 | {grid['real_pf_gt_1']} | "
                     + ' | '.join(str(grid[f'{m}_null_pf_gt_1']) for m in grid_modes) + ' |')
        lines.append(f"| Cells clearing the §3.4 out-of-sample gate | {grid['real_gate']} | "
                     + ' | '.join(str(grid[f'{m}_null_gate']) for m in grid_modes) + ' |')
        lines.append(f"| Pooled out-of-sample net PF | {fmt(grid['real_pooled_pf'])} | "
                     + ' | '.join(fmt(grid[f'{m}_null_pooled_pf']) for m in grid_modes) + ' |')
        lines.append(f"| Cells with gross out-of-sample PF > 1 | {grid['real_gross_pf_gt_1']} | "
                     + ' | '.join(str(grid[f'{m}_null_gross_pf_gt_1']) for m in grid_modes) + ' |')
        lines.append(f"| Median gross out-of-sample net PF | "
                     f"{fmt(grid['real_gross_pf_distribution'].get('median'))} | "
                     + ' | '.join(fmt(grid[f'{m}_null_gross_pf_distribution'].get('median'))
                                 for m in grid_modes) + ' |')
        lines.append(f"| Median out-of-sample trades per cell | "
                     f"{fmt(grid.get('real_median_trades'))} | "
                     + ' | '.join(fmt(grid.get(f'{m}_null_median_trades')) for m in grid_modes) + ' |')
        lines.append(f"| Median risk distance (share of entry price) | "
                     f"{fmt_pct(grid.get('real_median_risk_pct'))} | "
                     + ' | '.join(fmt_pct(grid.get(f'{m}_null_median_risk_pct')) for m in grid_modes) + ' |')
        lines.append('')
    lines.append(f"Gate: {GATE_DESCRIPTION}.\n")
    if len(grid_modes) < len(payload['survivor_modes']):
        missing = [m for m in payload['survivor_modes'] if m not in grid_modes]
        lines.append(f"The {', '.join(missing)} null was not run over the whole grid in this "
                     f"leg (compute budget); it was run on the surviving and the control cells "
                     f"in Leg 3.\n")

    lines.append('## Leg 2 — The observed tail against the null tail\n')
    lines.append('| Quantity | Value |')
    lines.append('|---|---|')
    lines.append(f"| Best cell of the grid (real) | {fmt(grid['real_max_pf'])} |")
    for mode in grid_modes:
        lines.append(f"| Best cell of the {mode} null | {fmt(grid[f'{mode}_null_max_pf'])} |")
    lines.append(f"| Null cells at or above the real best | {grid['timing_null_at_or_above_best']} |")
    lines.append(f"| Family-wise probability of a null cell reaching the real best | "
                 f"{fmt_pf(grid['family_wise_p_value'])} |")
    lines.append(f"| Cells where the real rule beats its own {grid['primary_null_mode']} null | "
                 f"{grid['n_real_beats_timing_null']} of {payload['n_cells']} |")
    lines.append(f"| Two-sided sign test on that comparison | {fmt_pf(grid['sign_test_p_value'])} |")
    lines.append(f"| Same comparison on the gross profit factor (no cost drag) | "
                 f"{grid['n_real_beats_null_on_gross_pf']} of {payload['n_cells']} |")
    lines.append(f"| Two-sided sign test on the gross comparison | "
                 f"{fmt_pf(grid['gross_sign_test_p_value'])} |")
    lines.append('')

    survivors = payload.get('survivors') or []
    if survivors:
        lines.append('## Leg 3 — The surviving cells against their own randomizations\n')
        lines.append('Each cell is re-randomized many times. The p-value is the share of '
                     'randomizations that reach the observed out-of-sample net PF, corrected '
                     'for the number of cells the program tested (Bonferroni over '
                     f"{payload['n_cells']} cells). The control cells are ordinary cells that "
                     'did not survive the audit; they show what the same test does on a cell '
                     'with no reason to look good.\n')
        lines.append('| Symbol | Cell | Group | OOS PF | Null mean PF | Null max PF | '
                     'p-value | p x grid | Null gate pass rate |')
        lines.append('|---|---|---|---|---|---|---|---|---|')
        for row in survivors:
            mode = row['modes'].get('timing') or next(iter(row['modes'].values()))
            lines.append(
                f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                f"{row.get('group', 'survivor')} | "
                f"{fmt(row['real']['net_pf'])} | {fmt(mode['null_pf_mean'])} | "
                f"{fmt(mode['null_pf_max'])} | {fmt_pf(mode['p_value'])} | "
                f"{fmt_pf(min(1.0, mode['p_value'] * payload['n_cells']))} | "
                f"{mode['null_gate_pass_rate']:.1%} |")
        lines.append('')
        lines.append(f'With {payload.get("survivor_replicates")} randomizations the smallest '
                     f'attainable p-value is 1/({payload.get("survivor_replicates")} + 1). '
                     f'The Bonferroni column can therefore not reach significance for a '
                     f'single cell: this leg can show that a surviving cell is '
                     f'*indistinguishable* from its own null, which is what it shows, but it '
                     f'cannot promote one.\n')
        if len(survivor_modes) > 1:
            lines.append('The same cells under the sign null (same entry bars, random '
                         'direction):\n')
            lines.append('| Symbol | Cell | OOS PF | Sign-null mean PF | Sign-null max PF | '
                         'p-value | p x grid |')
            lines.append('|---|---|---|---|---|---|---|')
            for row in survivors:
                mode = row['modes'].get('sign')
                if not mode:
                    continue
                lines.append(
                    f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                    f"{fmt(row['real']['net_pf'])} | {fmt(mode['null_pf_mean'])} | "
                    f"{fmt(mode['null_pf_max'])} | {fmt_pf(mode['p_value'])} | "
                    f"{fmt_pf(min(1.0, mode['p_value'] * payload['n_cells']))} |")
            lines.append('')

    lines.append('## Verdict\n')
    for line in payload['verdict_lines']:
        lines.append(f'- {line}')
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def fmt(value) -> str:
    """Format a number for the report."""
    if value is None:
        return 'n/a'
    if isinstance(value, float) and not math.isfinite(value):
        return 'inf' if value > 0 else '-inf'
    return f'{value:.4f}'


def fmt_pct(value) -> str:
    """Format a share of the entry price."""
    if value is None:
        return 'n/a'
    return f'{value:.4%}'


def fmt_pf(value) -> str:
    """Format a probability."""
    if value is None:
        return 'n/a'
    if value < 1e-4:
        return f'{value:.2e}'
    return f'{value:.4f}'


def summarize_existing(out_dir: Path, args) -> None:
    """Rebuild the leg summary from a checkpointed cells.jsonl."""
    path = out_dir / 'cells.jsonl'
    if not path.exists():
        raise SystemExit(f'no cells.jsonl in {out_dir}')
    rows = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if not rows:
        raise SystemExit(f'{path} is empty')
    modes = [m for m in args.modes
             if all(m in r.get('null', {}) for r in rows)]
    grid_summary = build_grid_summary(rows, modes, args.min_trades)
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_run': args.run,
        'oos_fraction': args.oos_fraction,
        'stress_multiplier': args.stress_multiplier,
        'min_trades': args.min_trades,
        'modes': modes,
        'survivor_modes': list(args.survivor_modes),
        'block_bars': args.block_bars,
        'n_symbols': len({r['symbol'] for r in rows}),
        'n_cells': len(rows),
        'grid': grid_summary,
        'validation': {'n_cells': 0, 'n_summary_matches': 0, 'n_window_matches': 0,
                       'n_signals_match': 0, 'cells': []},
        'survivors': [],
        'n_survivor_cells': 0,
        'n_control_cells': 0,
        'survivor_replicates': args.survivor_replicates,
        'partial': True,
    }
    payload['verdict_lines'] = build_verdict(payload)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    write_report(out_dir, payload)
    print(f'Summarized {len(rows)} cells from {path}')
    print(f"Wrote {out_dir}/summary.md and summary.json")


def main():
    parser = argparse.ArgumentParser(
        description='Randomized-entry null for the EMA hourly continuation grid')
    parser.add_argument('--run', type=str, required=True, help='results/<RUNID>_grid')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--oos-fraction', type=float, default=0.35)
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--min-trades', type=int, default=30)
    parser.add_argument('--modes', type=str, nargs='*', default=list(NULL_MODES),
                        help='Null modes run over the whole grid: timing, sign')
    parser.add_argument('--survivor-modes', type=str, nargs='*',
                        default=list(NULL_MODES),
                        help='Null modes run on the surviving and control cells')
    parser.add_argument('--block-bars', type=int, default=DEFAULT_BLOCK_BARS,
                        help='Length of the block the local null shuffles inside')
    parser.add_argument('--survivors-from', type=str, default=None,
                        help='results/<TS>_oos_grid_scan dir; the cells it kept are '
                             're-randomized many times')
    parser.add_argument('--survivor-replicates', type=int, default=50)
    parser.add_argument('--control-sample', type=int, default=0,
                        help='Random cells that did not survive, re-randomized as a control')
    parser.add_argument('--validate-sample', type=int, default=200,
                        help='Cells re-run on the full history to validate the harness')
    parser.add_argument('--limit-symbols', type=int, default=0,
                        help='Only the first N symbols (smoke test)')
    parser.add_argument('--workers', type=int, default=min(4, os.cpu_count() or 1))
    parser.add_argument('--seed', type=int, default=20261021)
    parser.add_argument('--out', type=str, default=None)
    parser.add_argument('--summarize-only', type=str, default=None,
                        help='Rebuild the summary and the report from an existing '
                             'cells.jsonl (used when a long grid pass was interrupted)')
    parser.add_argument('--render-only', type=str, default=None,
                        help='Re-render summary.md from an existing summary.json')
    args = parser.parse_args()

    if args.summarize_only:
        summarize_existing(Path(args.summarize_only), args)
        return

    if args.render_only:
        out_dir = Path(args.render_only)
        payload = json.loads((out_dir / 'summary.json').read_text())
        payload['verdict_lines'] = build_verdict(payload)
        write_report(out_dir, payload)
        print(f'Rendered {out_dir}/summary.md')
        return

    run_dir = Path(args.run)
    if not (run_dir / 'results').exists():
        raise SystemExit(f'no grid results found in {run_dir}')

    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    out_dir = Path(args.out) if args.out else Path('results') / f'{timestamp}_null_grid_scan'
    out_dir.mkdir(parents=True, exist_ok=True)

    config = dict(CONFIG_DEFAULTS)
    config['stress_multiplier'] = args.stress_multiplier
    opts = {
        'run': str(run_dir),
        'fixture_base': args.fixture_base,
        'oos_fraction': args.oos_fraction,
        'stress_multiplier': args.stress_multiplier,
        'min_trades': args.min_trades,
        'modes': list(args.modes),
        'block_bars': args.block_bars,
        'config': config,
    }

    cells = grid_cells(run_dir)
    symbols = sorted({c[0] for c in cells})
    if args.limit_symbols:
        keep = set(symbols[:args.limit_symbols])
        cells = [c for c in cells if c[0] in keep]
        symbols = sorted(keep)
    by_symbol = {}
    for symbol, fast, slow in cells:
        by_symbol.setdefault(symbol, []).append((fast, slow))
    tasks = [(symbol, pairs, opts) for symbol, pairs in sorted(by_symbol.items())]

    print(f'Screening {len(cells)} cells over {len(symbols)} symbols '
          f'(modes: {", ".join(args.modes)}) on {args.workers} workers', flush=True)

    rows = []
    # The per-cell results are checkpointed as they arrive, so a long grid
    # pass that is interrupted still leaves a usable artifact on disk.
    with open(out_dir / 'cells.jsonl', 'w') as checkpoint:
        if args.workers > 1:
            import multiprocessing as mp
            with mp.Pool(processes=args.workers) as pool:
                for i, result in enumerate(pool.imap_unordered(_worker, tasks), 1):
                    rows.extend(result)
                    for row in result:
                        checkpoint.write(json.dumps(row, default=str) + '\n')
                    checkpoint.flush()
                    if i % 25 == 0:
                        print(f'  {i}/{len(tasks)} symbols done ({len(rows)} cells)', flush=True)
        else:
            for i, task in enumerate(tasks, 1):
                result = _worker(task)
                rows.extend(result)
                for row in result:
                    checkpoint.write(json.dumps(row, default=str) + '\n')
                checkpoint.flush()
                if i % 25 == 0:
                    print(f'  {i}/{len(tasks)} symbols done ({len(rows)} cells)', flush=True)

    grid_summary = build_grid_summary(rows, args.modes, args.min_trades)
    n_cells = len(rows)

    # Survivors and control cells: many randomizations of the same cell.
    survivors = []
    if args.survivors_from:
        cells_to_test = survivor_cells(Path(args.survivors_from), args.min_trades, 1.0)
        if args.control_sample:
            rng = np.random.default_rng(args.seed)
            pool_cells = [c for c in cells if c not in set(cells_to_test)]
            pick = rng.choice(len(pool_cells), size=min(args.control_sample, len(pool_cells)),
                              replace=False)
            control = [pool_cells[i] for i in sorted(pick)]
        else:
            control = []
        for label, group in (('survivor', cells_to_test), ('control', control)):
            if not group:
                continue
            grouped = {}
            for symbol, fast, slow in group:
                grouped.setdefault(symbol, []).append((fast, slow))
            survivor_opts = dict(opts, modes=list(args.survivor_modes))
            tasks2 = [(symbol, pairs, survivor_opts, args.survivor_replicates)
                      for symbol, pairs in sorted(grouped.items())]
            print(f'Re-randomizing {len(group)} {label} cells '
                  f'({args.survivor_replicates} replicates each)', flush=True)
            if args.workers > 1:
                import multiprocessing as mp
                with mp.Pool(processes=args.workers) as pool:
                    for result in pool.imap_unordered(_survivor_worker, tasks2):
                        for row in result:
                            row['group'] = label
                            survivors.append(row)
            else:
                for task in tasks2:
                    for row in _survivor_worker(task):
                        row['group'] = label
                        survivors.append(row)

    # Validation sample: the harness against the stored grid run.
    validation_rows = []
    if args.validate_sample:
        rng = np.random.default_rng(args.seed + 1)
        pick = rng.choice(len(cells), size=min(args.validate_sample, len(cells)),
                          replace=False)
        sample = [cells[i] for i in sorted(pick)]
        grouped = {}
        for symbol, fast, slow in sample:
            grouped.setdefault(symbol, []).append((fast, slow))
        tasks3 = [(symbol, pairs, opts) for symbol, pairs in sorted(grouped.items())]
        print(f'Validating the harness on {len(sample)} cells', flush=True)
        if args.workers > 1:
            import multiprocessing as mp
            with mp.Pool(processes=args.workers) as pool:
                for result in pool.imap_unordered(_validate_worker, tasks3):
                    validation_rows.extend(result)
        else:
            for task in tasks3:
                validation_rows.extend(_validate_worker(task))

    validation = {
        'n_cells': len(validation_rows),
        'n_summary_matches': sum(1 for r in validation_rows if r['summary_matches']),
        'n_window_matches': sum(1 for r in validation_rows if r['window_matches']),
        'n_signals_match': sum(1 for r in validation_rows
                               if r['vectorized_matches_reference']),
        'cells': validation_rows,
    }

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_run': str(run_dir),
        'oos_fraction': args.oos_fraction,
        'stress_multiplier': args.stress_multiplier,
        'min_trades': args.min_trades,
        'modes': list(args.modes),
        'survivor_modes': list(args.survivor_modes),
        'config': config,
        'n_symbols': len(symbols),
        'n_cells': n_cells,
        'grid': grid_summary,
        'validation': validation,
        'survivors': survivors,
        'n_survivor_cells': sum(1 for s in survivors if s.get('group') == 'survivor'),
        'n_control_cells': sum(1 for s in survivors if s.get('group') == 'control'),
        'survivor_replicates': args.survivor_replicates,
    }
    payload['verdict_lines'] = build_verdict(payload)

    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    with open(out_dir / 'config.json', 'w') as fh:
        json.dump({
            'timestamp': timestamp,
            'source_run': str(run_dir),
            'fixture_base': args.fixture_base,
            'oos_fraction': args.oos_fraction,
            'stress_multiplier': args.stress_multiplier,
            'min_trades': args.min_trades,
            'modes': list(args.modes),
            'survivor_modes': list(args.survivor_modes),
            'block_bars': args.block_bars,
            'survivors_from': args.survivors_from,
            'survivor_replicates': args.survivor_replicates,
            'control_sample': args.control_sample,
            'validate_sample': args.validate_sample,
            'workers': args.workers,
            'seed': args.seed,
            'config': config,
            'command': (f'PYTHONPATH=. python3 scripts/null_grid_scan.py --run {run_dir} '
                        f'--modes {" ".join(args.modes)} '
                        f'--survivor-replicates {args.survivor_replicates}'),
        }, fh, indent=2)
    write_report(out_dir, payload)

    print(f'\nGrid: {n_cells} cells, {len(symbols)} symbols')
    print(f"Real: {grid_summary['real_pf_gt_1']} cells with OOS net PF > 1, "
          f"{grid_summary['real_gate']} clearing the §3.4 out-of-sample gate")
    for mode in args.modes:
        print(f"Null ({mode}): {grid_summary[f'{mode}_null_pf_gt_1']} cells with OOS net PF > 1, "
              f"{grid_summary[f'{mode}_null_gate']} clearing the gate, "
              f"best {fmt(grid_summary[f'{mode}_null_max_pf'])}")
    print(f"Family-wise p-value for the observed best cell: "
          f"{fmt_pf(grid_summary['family_wise_p_value'])}")
    print(f'Validation: {validation["n_summary_matches"]}/{validation["n_cells"]} cells '
          f'reproduce the stored grid summary, '
          f'{validation["n_window_matches"]}/{validation["n_cells"]} match the '
          f'windowed run')
    print(f'Wrote {out_dir}/summary.md and summary.json')


def median_of(values: list):
    """Median of a list that may contain None entries."""
    clean = [v for v in values if v is not None and math.isfinite(float(v))]
    return float(np.median(clean)) if clean else None


def pooled_ratio(rows: list, *path) -> float:
    """Pooled net PF over the trade P&L of a set of cells.

    The per-cell profit factors are not averaged: pooling uses the trade-level
    wins and losses, so a thin cell does not get the same weight as a thick
    one.
    """
    win = 0.0
    loss = 0.0
    for row in rows:
        stats = row
        for key in path:
            stats = stats.get(key) if isinstance(stats, dict) else None
        if not isinstance(stats, dict):
            continue
        pf = stats.get('net_pf')
        if pf is None or not math.isfinite(pf):
            continue
        pnl = stats.get('net_pnl', 0.0)
        if pnl > 0:
            win += pnl
        else:
            loss += -pnl
    if loss > 0:
        return win / loss
    return float('inf') if win > 0 else 0.0


def build_verdict(payload: dict) -> list:
    """The decision lines of the leg."""
    grid = payload['grid']
    lines = []
    n_cells = grid['real_pf_gt_1']
    null_cells = grid.get('timing_null_pf_gt_1')
    if null_cells is not None:
        lines.append(
            f"{n_cells} of {payload['n_cells']} cells show an out-of-sample net PF above 1; "
            f"the timing null produces {null_cells}. The observed tail is "
            f"{'larger' if n_cells > null_cells else 'no larger'} than what random entry "
            f"timing delivers.")
    if grid['real_gate'] or grid.get('timing_null_gate'):
        lines.append(
            f"{grid['real_gate']} real cells clear the §3.4 out-of-sample gate against "
            f"{grid.get('timing_null_gate')} timing-null cells: the gate's false-positive "
            f"rate under no information is "
            f"{(grid.get('timing_null_gate') or 0) / max(1, payload['n_cells']):.2%} of the grid.")
    lines.append(
        f"The best real cell (net PF {fmt(grid['real_max_pf'])}) sits against a best null "
        f"cell of {fmt(grid.get('timing_null_max_pf'))}; the family-wise probability that a "
        f"null cell reaches the real best is {fmt_pf(grid['family_wise_p_value'])}.")
    lines.append(
        f"The real rule beats its own timing null in {grid['n_real_beats_timing_null']} of "
        f"{payload['n_cells']} cells (sign test p = {fmt_pf(grid['sign_test_p_value'])}).")
    survivors = payload.get('survivors') or []
    tested = [s for s in survivors if s.get('group') == 'survivor']
    if tested:
        significant = [s for s in tested
                       if (s['modes'].get('timing', {}).get('p_value') or 1.0) * payload['n_cells'] <= 1.0]
        lines.append(
            f"{len(tested)} surviving cells were re-randomized; {len(significant)} keep an "
            f"out-of-sample net PF above the real one at a Bonferroni-corrected level over "
            f"{payload['n_cells']} tests.")
    return lines


if __name__ == '__main__':
    main()
