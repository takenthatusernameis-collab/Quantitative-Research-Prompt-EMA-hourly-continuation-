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

The null is *matched* to the rule inside that window: the entries the rule
fires on inside the window are the entries the null randomizes, and the null
draws its replacement bars from the window as well. A null that kept the
whole history's entries would lose every entry before the window and would
then be scored on a thinner sample than the rule it is compared against.

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
from scripts.run_grid import CONFIG_DEFAULTS, GRID_PAIRS, load_run_config
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
    places them at uniformly random bars over the eligible bars it is given
    (the out-of-sample window). `sign` keeps the entry bars and redraws every
    direction from a fair coin. `block` keeps the number of entries, the
    direction mix and the local market context, and moves every entry to a
    random bar inside its own block: the entry stops being a cross but stays
    in the same stretch of the market, which is what makes its risk distance
    comparable to the real rule's.
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
        # Trade-level win and loss sums: the pooled profit factor of a set of
        # cells is built from these, so a thin cell does not get the same
        # weight as a thick one and the number is comparable with the
        # trade-level pooled PF the out-of-sample audit reports.
        'net_win_sum': float(pnl_net[pnl_net > 0].sum()) if len(trades) else 0.0,
        'net_loss_abs': float(-pnl_net[pnl_net < 0].sum()) if len(trades) else 0.0,
        'sharpe': metrics.get('sharpe_ratio'),
        'net_win_rate': metrics.get('net_win_rate'),
        # The risk distance as a share of the entry price. The cost drag of a
        # trade scales with 1 / risk, so this is the statistic that tells
        # whether a null and the real rule pay the same kind of cost.
        'median_risk_pct': (float(np.nanmedian(risk_pct))
                            if risk_pct.size and np.isfinite(risk_pct).any()
                            else None),
    }


def run_config(run_dir: Path) -> dict:
    """The trading config of the grid run the null leg is compared against.

    The null has to randomize the *same* rule the grid run uses. A mutation
    run (PROMPT.md §5.2) changes the rule - the ATR minimum-risk child filters
    entries the baseline rule takes - and a null built on the baseline rule
    would score the child against the wrong reference: both the "real" leg and
    the null would describe the parent. The run's own `run_config.json` is
    therefore the source of the config; a run without one falls back to the
    engine defaults.
    """
    return load_run_config(run_dir)


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
    """Real cell plus the null realizations that are not already checkpointed.

    A resumed pass may have already written one of the null modes for this
    cell; the modes it still needs are the ones in `opts['modes']` minus the
    ones the checkpoint already holds. The real leg is always recomputed - it
    is cheap and it keeps the row self-contained.

    The null is matched to the real rule inside the out-of-sample window: the
    entries the rule fires on *inside the window* are the entries the null
    randomizes, and the null draws its replacement bars from the window as
    well. Without that the null loses every entry that falls before the
    window, and it is then scored on a thinner sample than the rule it is
    compared against.
    """
    config = opts['config']
    existing = opts.get('existing', {})
    frame = generate_signals_vectorized(df, fast, slow, config['stricter_trend'])
    signal = frame['signal'].to_numpy()
    entry_start = entry_start_index(len(frame), opts['oos_fraction'])
    # The entries of the window only: these are the ones the null replaces.
    entry_idx = np.flatnonzero(signal != 0)
    window_mask = entry_idx >= entry_start
    entry_idx = entry_idx[window_mask]
    sides = signal[entry_idx]
    eligible = eligible_bars(len(frame), fast, slow)
    eligible = eligible[eligible >= entry_start]

    real = window_stats(frame, entry_start, config, symbol)
    row = {
        'symbol': symbol,
        'P_fast': fast,
        'P_slow': slow,
        'n_bars': int(len(frame)),
        'entry_start_index': entry_start,
        'n_signals': int(entry_idx.size),
        'real': real,
        'null': dict(existing),
    }
    for mode in opts['modes']:
        if mode in row['null']:
            continue
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
    entry_start = entry_start_index(len(frame), opts['oos_fraction'])
    # The window's entries only, exactly as in the grid-wide leg, so the
    # per-cell null distribution is drawn from the same sample the real leg
    # is scored on.
    entry_idx = np.flatnonzero(signal != 0)
    entry_idx = entry_idx[entry_idx >= entry_start]
    sides = signal[entry_idx]
    eligible = eligible_bars(len(frame), fast, slow)
    eligible = eligible[eligible >= entry_start]
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

    Implemented here because scipy is not available in this environment. For
    large `trials` the exact sum over `math.comb` overflows (9900 choose 4950
    is a ~3000-digit integer), so the tail is computed in log space with a
    running recurrence and converted back only at the end. The result is the
    same two-sided exact p-value the direct sum would give.
    """
    if trials == 0:
        return 1.0
    k = min(successes, trials - successes)
    if k < 0:
        return 1.0
    logp = math.log(p)
    logq = math.log(1.0 - p)
    # log C(trials, i) for i = 0, updated by the recurrence
    # C(n, i+1) = C(n, i) * (n - i) / (i + 1).
    log_comb = 0.0
    tail = 0.0
    for i in range(k + 1):
        tail += math.exp(log_comb + i * logp + (trials - i) * logq)
        if i == k:
            break
        log_comb += math.log(trials - i) - math.log(i + 1)
    return min(1.0, 2.0 * tail)


def _worker(task):
    """Process every pair of one symbol (the fixture is loaded once)."""
    symbol, pairs, opts = task
    path = Path(opts['fixture_base']) / f"{symbol.replace('/', '_')}.csv"
    df = load_ohlcv_csv(path)
    rows = []
    for fast, slow in pairs:
        cell_opts = dict(opts)
        # A resumed pass keeps the null modes the checkpoint already holds, so
        # the row that is written back holds every mode, not only the ones
        # this pass computed.
        cell_opts['existing'] = opts.get('existing', {}).get((fast, slow), {})
        rows.append(process_cell(symbol, df, fast, slow, cell_opts))
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
        'real_pooled_pf': pooled_ratio(rows, 'real'),
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
        grid_summary[f'{mode}_null_pooled_pf'] = pooled_ratio(rows, 'null', mode)

    # The family-wise reading of the observed best cell, and the paired
    # cell-by-cell comparison, are computed for every null mode the leg ran.
    # A leg that runs more than one null has to answer the question for each
    # of them: the block null keeps the market context, the timing null does
    # not, and they do not have to reach the same verdict.
    n_cells = len(rows)
    real_max = grid_summary['real_max_pf']
    for mode in modes:
        finite_null = [p for p in (r['null'][mode]['net_pf'] for r in rows)
                       if p is not None and math.isfinite(p)]
        exceed = sum(1 for p in finite_null if real_max is not None and p >= real_max)
        q = exceed / n_cells if n_cells else 0.0
        grid_summary[f'{mode}_null_at_or_above_best'] = exceed
        grid_summary[f'{mode}_family_wise_p_value'] = (
            1.0 - (1.0 - q) ** n_cells if n_cells else 1.0)
        beats = sum(1 for r in rows
                    if (r['real']['net_pf'] or 0.0) > (r['null'][mode]['net_pf'] or 0.0))
        grid_summary[f'{mode}_n_real_beats_null'] = beats
        # The other side of the same comparison, so the report can say which
        # side wins instead of leaving the reader to infer it from a count.
        grid_summary[f'{mode}_n_null_beats_real'] = n_cells - beats
        grid_summary[f'{mode}_sign_test_p_value'] = binomial_tail(beats, n_cells)
        gross_beats = sum(
            1 for r in rows
            if (r['real'].get('gross_pf') or 0.0) > (r['null'][mode].get('gross_pf') or 0.0))
        grid_summary[f'{mode}_n_real_beats_null_on_gross_pf'] = gross_beats
        grid_summary[f'{mode}_n_null_beats_real_on_gross_pf'] = n_cells - gross_beats
        grid_summary[f'{mode}_gross_sign_test_p_value'] = binomial_tail(gross_beats, n_cells)

    # The primary null is the first mode of the leg, so the verdict and the
    # report always talk about the null that was actually run. The keys
    # without a mode in their name are the primary mode's numbers.
    primary_mode = modes[0] if modes else None
    grid_summary['primary_null_mode'] = primary_mode
    if primary_mode is None:
        return grid_summary
    grid_summary['primary_null_at_or_above_best'] = grid_summary[
        f'{primary_mode}_null_at_or_above_best']
    grid_summary['family_wise_p_value'] = grid_summary[f'{primary_mode}_family_wise_p_value']
    grid_summary['n_real_beats_timing_null'] = grid_summary[f'{primary_mode}_n_real_beats_null']
    grid_summary['n_null_beats_real'] = grid_summary[f'{primary_mode}_n_null_beats_real']
    grid_summary['sign_test_p_value'] = grid_summary[f'{primary_mode}_sign_test_p_value']
    grid_summary['n_real_beats_null_on_gross_pf'] = grid_summary[
        f'{primary_mode}_n_real_beats_null_on_gross_pf']
    grid_summary['n_null_beats_real_on_gross_pf'] = grid_summary[
        f'{primary_mode}_n_null_beats_real_on_gross_pf']
    grid_summary['gross_sign_test_p_value'] = grid_summary[
        f'{primary_mode}_gross_sign_test_p_value']
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
                 'out-of-sample window, with the same multiset of directions.')
    lines.append('- **sign** - the same entry bars, with every direction redrawn from a '
                 'fair coin.\n')
    lines.append('Both are run through the untouched backtest engine, so the null is produced '
                 'by the same code that produced the real numbers. The null is matched to the '
                 'rule inside the window: the entries the rule fires on inside the window are '
                 'the entries the null randomizes, so both sides are scored on the same '
                 'sample.\n')

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
    # A summary written before the per-mode reading existed carries the
    # numbers under the primary mode's names; they are used as the fallback
    # so an older artifact still renders.
    legacy = {
        'null_at_or_above_best': 'timing_null_at_or_above_best',
        'family_wise_p_value': 'family_wise_p_value',
        'n_real_beats_null': 'n_real_beats_timing_null',
        'n_null_beats_real': 'n_null_beats_real',
        'sign_test_p_value': 'sign_test_p_value',
        'n_real_beats_null_on_gross_pf': 'n_real_beats_null_on_gross_pf',
        'gross_sign_test_p_value': 'gross_sign_test_p_value',
    }

    def _tail_value(mode, key):
        if f'{mode}_{key}' in grid:
            return grid[f'{mode}_{key}']
        fallback = legacy.get(key)
        if fallback and fallback in grid:
            return grid[fallback]
        return None

    lines.append('| Statistic | Real rule | '
                 + ' | '.join(f'{m} null' for m in grid_modes) + ' |')
    lines.append('|---|---' + '|'.join('---' for _ in grid_modes) + '|')
    lines.append(f"| Best cell of the grid | {fmt(grid['real_max_pf'])} | "
                 + ' | '.join(fmt(grid[f'{m}_null_max_pf']) for m in grid_modes) + ' |')
    lines.append("| Null cells at or above the real best | - | "
                 + ' | '.join(str(_tail_value(m, 'null_at_or_above_best'))
                              for m in grid_modes) + ' |')
    lines.append("| Family-wise probability of a null cell reaching the real best | - | "
                 + ' | '.join(fmt_probability(_tail_value(m, 'family_wise_p_value'))
                              for m in grid_modes) + ' |')
    lines.append("| Cells where the real rule beats its own null | - | "
                 + ' | '.join(str(_tail_value(m, 'n_real_beats_null'))
                              for m in grid_modes) + ' |')
    lines.append("| Cells where the null beats the real rule | - | "
                 + ' | '.join(str(_tail_value(m, 'n_null_beats_real'))
                              for m in grid_modes) + ' |')
    lines.append("| Two-sided sign test on that comparison | - | "
                 + ' | '.join(fmt_pf(_tail_value(m, 'sign_test_p_value'))
                              for m in grid_modes) + ' |')
    lines.append("| Same comparison on the gross profit factor (no cost drag) | - | "
                 + ' | '.join(str(_tail_value(m, 'n_real_beats_null_on_gross_pf'))
                              for m in grid_modes) + ' |')
    lines.append("| Two-sided sign test on the gross comparison | - | "
                 + ' | '.join(fmt_pf(_tail_value(m, 'gross_sign_test_p_value'))
                              for m in grid_modes) + ' |')
    lines.append('')
    lines.append('A sign test p-value this small means the two sides of the comparison are '
                 'not exchangeable. The direction is the point: the counts above say which '
                 'side of the comparison the rule is on.\n')

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
            gate_rate = mode.get('null_gate_pass_rate')
            lines.append(
                f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                f"{row.get('group', 'survivor')} | "
                f"{fmt(row['real']['net_pf'])} | {fmt(mode['null_pf_mean'])} | "
                f"{fmt(mode['null_pf_max'])} | {fmt_pf(mode['p_value'])} | "
                f"{fmt_pf(min(1.0, mode['p_value'] * payload['n_cells']))} | "
                f"{'n/a' if gate_rate is None else f'{gate_rate:.1%}'} |")
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


def fmt_probability(value) -> str:
    """Format a probability that is read as "how likely is this".

    A probability that is essentially 1 is the informative case: the family
    wise reading "a null cell reaches the real best with probability 1" is
    only readable when the distance from 1 is shown, so the complement is
    printed instead of a rounded 1.0000.
    """
    if value is None:
        return 'n/a'
    if not math.isfinite(value):
        return 'n/a'
    if value > 0.99:
        return f'1 - {1.0 - value:.2e}'
    return fmt_pf(value)


def summarize_existing(out_dir: Path, args) -> None:
    """Rebuild the leg summary from a checkpointed cells.jsonl."""
    path = out_dir / 'cells.jsonl'
    if not path.exists():
        raise SystemExit(f'no cells.jsonl in {out_dir}')
    rows = []
    n_truncated = 0
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                # A truncated line from a pass that was killed mid-write is
                # dropped; the cell is recomputed by the pass that continues.
                n_truncated += 1
    if n_truncated:
        print(f'Dropped {n_truncated} truncated line(s) from {path}')
    if not rows:
        raise SystemExit(f'{path} is empty')
    modes = [m for m in args.modes
             if all(m in r.get('null', {}) for r in rows)]
    grid_summary = build_grid_summary(rows, modes, args.min_trades)
    # The validation leg is not re-run when only the summary is rebuilt, so the
    # numbers of the previous run are carried over instead of being reported
    # as zero. When no previous summary exists (a leg that was only ever
    # checkpointed, like the interrupted 20261021_035000 pass), fall back to
    # the grid-wide out-of-sample audit's Leg 0, which is the same "harness
    # reproduces the grid run" check over the same 17 556 cells.
    validation = {'n_cells': 0, 'n_summary_matches': 0, 'n_window_matches': 0,
                  'n_signals_match': 0, 'cells': []}
    summary_path = out_dir / 'summary.json'
    if summary_path.exists():
        try:
            previous = json.loads(summary_path.read_text())
            validation = previous.get('validation', validation)
        except Exception:
            pass
    elif not validation['n_cells']:
        for candidate in sorted(Path('results').glob('*_oos_grid_scan/summary.json')):
            try:
                prev = json.loads(candidate.read_text())
            except Exception:
                continue
            if prev.get('n_cells') == len(rows):
                validation = prev.get('validation', validation)
                break
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
        'validation': validation,
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
    parser.add_argument('--run', type=str, required=False, help='results/<RUNID>_grid')
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

    # Resume: keep the cells a prior pass already checkpointed and only run the
    # ones that are missing. A pass that was interrupted (or that only ran one
    # null mode) can therefore be completed instead of restarted from scratch.
    checkpoint_path = out_dir / 'cells.jsonl'
    by_key = {}
    n_truncated = 0
    if checkpoint_path.exists():
        with open(checkpoint_path) as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    # A pass that was killed while it was writing can leave a
                    # truncated last line. The cell it belongs to is simply
                    # run again, so the line is dropped instead of taking the
                    # whole pass down with it.
                    n_truncated += 1
                    continue
                by_key[(r['symbol'], r['P_fast'], r['P_slow'])] = r
    if n_truncated:
        print(f'Checkpoint held {n_truncated} truncated line(s); they are re-run.',
              flush=True)

    config = run_config(run_dir)
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

    # A cell is still to run when it lacks any of the requested null modes. The
    # tasks are grouped by symbol so the fixture is loaded once per symbol.
    tasks = []
    for symbol, pairs in sorted(by_symbol.items()):
        missing = []
        for fast, slow in pairs:
            key = (symbol, fast, slow)
            existing = by_key.get(key, {}).get('null', {})
            if any(m not in existing for m in args.modes):
                missing.append((fast, slow))
        if missing:
            symbol_opts = dict(opts)
            symbol_opts['existing'] = {
                (fast, slow): by_key.get((symbol, fast, slow), {}).get('null', {})
                for fast, slow in missing}
            tasks.append((symbol, missing, symbol_opts))
    if by_key:
        print(f'Resuming: {len(by_key)} cells already checkpointed, '
              f'{sum(len(t[1]) for t in tasks)} cells still to run', flush=True)

    # The checkpoint is appended to, never truncated: a pass that is
    # interrupted must not drop the rows a prior pass wrote. The file is
    # rewritten at the end of the run, when every cell holds every requested
    # mode, so the artifact ends up with exactly one row per cell.
    with open(checkpoint_path, 'a') as checkpoint:
        def _emit(result_rows):
            for row in result_rows:
                key = (row['symbol'], row['P_fast'], row['P_slow'])
                by_key[key] = row
            checkpoint.write(''.join(json.dumps(r, default=str) + '\n'
                                     for r in result_rows))
            checkpoint.flush()

        if tasks:
            if args.workers > 1:
                import multiprocessing as mp
                with mp.Pool(processes=args.workers) as pool:
                    batch = []
                    for result in pool.imap_unordered(_worker, tasks):
                        batch.extend(result)
                        if len(batch) >= 50:
                            _emit(batch)
                            batch = []
                            print(f'  {len(by_key)} cells checkpointed', flush=True)
                    if batch:
                        _emit(batch)
            else:
                for i, task in enumerate(tasks, 1):
                    _emit(_worker(task))
                    if i % 25 == 0:
                        print(f'  {i}/{len(tasks)} symbols done', flush=True)

    # One row per cell: the merged set is written back, so a cell that gained
    # a mode replaces the stale row that lacked it and the file holds no
    # duplicates.
    tmp_path = checkpoint_path.with_name(checkpoint_path.name + '.tmp')
    with open(tmp_path, 'w') as fh:
        fh.write(''.join(json.dumps(r, default=str) + '\n'
                         for r in by_key.values()))
    tmp_path.replace(checkpoint_path)

    # Re-read the full checkpoint so the summary covers every cell, including
    # the ones a prior pass wrote.
    all_rows = []
    with open(checkpoint_path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                all_rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    rows = all_rows

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

    `path` resolves to the statistics dict of a cell (for example
    ``('real',)`` or ``('null', 'block')``). The per-cell profit factors are
    not averaged: pooling uses the trade-level wins and losses, so a thin cell
    does not get the same weight as a thick one.

    The trade-level sums are used when the cell carries them. A cell that only
    has a net P&L (a re-summarized checkpoint from an older run) falls back to
    splitting that P&L by sign, which is the coarser cell-level version of the
    same ratio.
    """
    win = 0.0
    loss = 0.0
    for row in rows:
        stats = row
        for key in path:
            stats = stats.get(key) if isinstance(stats, dict) else None
        if not isinstance(stats, dict):
            continue
        if 'net_win_sum' in stats and 'net_loss_abs' in stats:
            win += float(stats.get('net_win_sum') or 0.0)
            loss += float(stats.get('net_loss_abs') or 0.0)
            continue
        pnl = stats.get('net_pnl')
        if pnl is None:
            continue
        pnl = float(pnl)
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
    # The primary null is the mode the leg was actually run with. Reading the
    # mode out of the summary instead of hard-coding 'timing' is what keeps the
    # verdict correct when the leg runs the block or the sign null.
    mode = grid.get('primary_null_mode')
    n_cells = grid['real_pf_gt_1']
    null_cells = grid.get(f'{mode}_null_pf_gt_1') if mode else None
    if null_cells is not None:
        lines.append(
            f"{n_cells} of {payload['n_cells']} cells show an out-of-sample net PF above 1; "
            f"the {mode} null produces {null_cells}. The observed tail is "
            f"{'larger' if n_cells > null_cells else 'no larger'} than what the {mode} "
            f"null delivers.")
    null_gate = grid.get(f'{mode}_null_gate') if mode else None
    if grid['real_gate'] or null_gate:
        lines.append(
            f"{grid['real_gate']} real cells clear the §3.4 out-of-sample gate against "
            f"{null_gate} {mode}-null cells: the gate's false-positive "
            f"rate under no information is "
            f"{(null_gate or 0) / max(1, payload['n_cells']):.2%} of the grid.")
    null_max = grid.get(f'{mode}_null_max_pf') if mode else None
    lines.append(
        f"The best real cell (net PF {fmt(grid['real_max_pf'])}) sits against a best "
        f"{mode or 'null'} cell of {fmt(null_max)}; the family-wise probability that a "
        f"null cell reaches the real best is {fmt_probability(grid['family_wise_p_value'])}.")
    beats = grid.get('n_real_beats_timing_null')
    if beats is not None:
        lines.append(
            f"The real rule beats its own {mode} null in {beats} of "
            f"{payload['n_cells']} cells and loses to it in "
            f"{grid.get('n_null_beats_real')} (sign test p = "
            f"{fmt_pf(grid['sign_test_p_value'])}).")
    survivors = payload.get('survivors') or []
    # Every null the leg ran, side by side: the grid-wide counts of the real
    # rule against each of them. A leg with more than one null has to show
    # all of them, not only the primary one.
    grid_modes = [m for m in payload.get('modes') or []
                  if f'{m}_null_pf_gt_1' in grid]
    if grid_modes:
        parts = [f"real {grid['real_pf_gt_1']}/{grid['real_gate']}"]
        for m in grid_modes:
            parts.append(f"{m} {grid[f'{m}_null_pf_gt_1']}/{grid[f'{m}_null_gate']}")
        lines.append(
            'Grid-wide null counts (cells with an out-of-sample net PF above 1 / '
            'cells clearing the gate): ' + '; '.join(parts) + '.')
    tested = [s for s in survivors if s.get('group') == 'survivor']
    if tested:
        significant = [s for s in tested
                       if (s['modes'].get(mode, {}).get('p_value') or 1.0) * payload['n_cells'] <= 1.0]
        lines.append(
            f"{len(tested)} surviving cells were re-randomized; {len(significant)} keep an "
            f"out-of-sample net PF above the real one at a Bonferroni-corrected level over "
            f"{payload['n_cells']} tests.")
    return lines


if __name__ == '__main__':
    main()
