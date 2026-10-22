#!/usr/bin/env python3
"""Grid-wide out-of-sample audit of the EMA hourly continuation grid.

Why this harness exists
-----------------------
`scripts/candidate_check.py` applies the PROMPT.md §3.4 out-of-sample and
2x-cost gates to the cells whose *in-sample* net PF exceeded 1. In the
shipped run that is 36 of 17 556 cells. Every other cell was never looked at
out of sample, so the program decision rests on a selected subset: the cells
that already looked good in sample. A cell whose edge is real but whose
in-sample window was unlucky would never be examined, and a survivor hiding
there would be missed entirely.

This harness closes that gap. It applies an out-of-sample window to *every*
cell of the run and reports the whole distribution, not just the tail:

    stage 1 (screen)  every cell, computed from the trade blotters the grid
                      run already wrote. Trades are split at the same bar
                      boundary the grid runner uses for its OOS leg
                      (`entry_start_index = int(n_bars * (1 - oos_fraction))`)
                      and the OOS net PF, the OOS trade count and the OOS net
                      PF under 2x costs are recomputed from the blotter. No
                      backtest is re-run and no market data is fetched, so the
                      whole grid is screened in seconds.
    stage 2 (verify)  every cell the screen keeps is re-run through the real
                      backtest (`scripts.run_grid.run_cell`) with the OOS
                      window and with 2x costs. The PROMPT.md §3.4 gates are
                      then applied to the authoritative numbers.

The 2x-cost restatement is exact. The engine charges
`cost_per_side = (taker_fee_bps + slippage_bps) / 10000` on entry and again
on exit, so scaling the cost model by `m` subtracts `(m - 1) * (entry_cost +
exit_cost)` from every trade's net P&L.

The stage-1 screen is deliberately loose (`--screen-pf`, default 0.9) because
it is computed from a restricted subset of the full-sample blotter rather
than from a fresh backtest; the decision gate itself is only ever applied to
the stage-2 numbers.

Usage:
    python scripts/oos_grid_scan.py --run results/20261019_135940_grid
    python scripts/oos_grid_scan.py --run results/20261019_135940_grid \
        --oos-fraction 0.35 --min-trades 30
    python scripts/oos_grid_scan.py --run results/20261019_135940_grid \
        --cells "JASMY/USDT:20:200,BABYDOGE/USDT:50:89" --window-sensitivity
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from data.data_loader import load_ohlcv_csv
from scripts.run_grid import (CONFIG_DEFAULTS, load_run_config, read_artifact_csv,
                              run_cell)

# Trade blotter columns the screen needs. Reading only these keeps the
# grid-wide pass cheap: the run holds 17 556 blotters.
TRADE_COLUMNS = ['bar_index', 'pnl', 'pnl_net', 'entry_cost', 'exit_cost']

# The grid runner writes gzip-compressed blotters, but the five largest
# market-cap names still carry the legacy baseline-study layout.
TRADES_FILENAME = 'trades.csv.gz'
LEGACY_TRADES_FILENAME = 'trades.csv'

# Under a no-edge null roughly half of the cells should show a net PF above 1
# by chance alone; the observed fraction is compared against it.
NULL_FRAC_NET_PF_GT_1 = 0.5


def entry_start_index(n_bars: int, oos_fraction: float) -> int:
    """Bar index at which the out-of-sample window opens.

    Mirrors `scripts.run_grid.run_cell`: entries are allowed from this bar
    onwards, and the equity curve is trimmed to it.
    """
    if oos_fraction is None or not (0.0 < oos_fraction < 1.0):
        return 0
    return int(n_bars * (1.0 - oos_fraction))


def net_profit_factor(pnl) -> float:
    """Trade-level profit factor of a P&L series: wins / losses.

    Returns None for an empty series, where the ratio is undefined rather
    than zero - a cell with no trades in a window is missing evidence, not
    evidence of a loss.
    """
    arr = np.asarray(pnl, dtype=float)
    if arr.size == 0:
        return None
    wins = float(arr[arr > 0].sum())
    losses = float(-arr[arr < 0].sum())
    if losses > 0:
        return wins / losses
    if wins > 0:
        return float('inf')
    return 0.0


def stressed_pnl_net(pnl_net, entry_cost, exit_cost, multiplier: float = 2.0):
    """Net P&L per trade with the cost model scaled by `multiplier`.

    The engine charges the per-side cost on entry and on exit, so a
    multiplier `m` adds `(m - 1) * (entry_cost + exit_cost)` to the cost of
    every trade.
    """
    pnl_net = np.asarray(pnl_net, dtype=float)
    if pnl_net.size == 0:
        return pnl_net
    extra = (multiplier - 1.0) * (np.asarray(entry_cost, dtype=float)
                                  + np.asarray(exit_cost, dtype=float))
    return pnl_net - extra


def read_trades(cell_dir: Path) -> pd.DataFrame:
    """Read one cell's trade blotter (the columns the screen needs).

    The run is not uniform: the five largest market-cap names carry the
    legacy baseline-study layout (`trades.csv`), the rest carry the
    gzip-compressed layout (`trades.csv.gz`). `read_artifact_csv` handles
    both, so the screen does not silently skip the top of the universe.
    """
    path = Path(cell_dir) / TRADES_FILENAME
    if not path.exists():
        path = Path(cell_dir) / LEGACY_TRADES_FILENAME
    return read_artifact_csv(path)[TRADE_COLUMNS]


def win_loss_sums(pnl) -> tuple:
    """Trade-level (sum of wins, sum of losses) of a P&L series.

    Pooling cells has to use these sums, never the per-cell profit factors:
    cells carry very different trade counts, so a mean of ratios would give a
    thin cell the same weight as a thick one.
    """
    arr = np.asarray(pnl, dtype=float)
    if arr.size == 0:
        return 0.0, 0.0
    return float(arr[arr > 0].sum()), float(-arr[arr < 0].sum())


def screen_cell(trades: pd.DataFrame, entry_start: int, stress_multiplier: float = 2.0) -> dict:
    """Out-of-sample statistics of one cell, computed from its blotter.

    `entry_start` is the first bar of the out-of-sample window; a trade
    belongs to the window when it was *entered* on or after that bar.
    """
    oos = trades[trades['bar_index'] >= entry_start]
    base_pnl = oos['pnl_net'].to_numpy()
    stress_pnl = stressed_pnl_net(oos['pnl_net'], oos['entry_cost'], oos['exit_cost'],
                                   stress_multiplier)
    full_pnl = trades['pnl_net'].to_numpy()
    full_stress = stressed_pnl_net(trades['pnl_net'], trades['entry_cost'],
                                    trades['exit_cost'], stress_multiplier)
    oos_win, oos_loss = win_loss_sums(base_pnl)
    oos_stress_win, oos_stress_loss = win_loss_sums(stress_pnl)
    return {
        'trades': int(len(trades)),
        'oos_trades': int(len(oos)),
        'net_pf': net_profit_factor(full_pnl),
        'stress_net_pf': net_profit_factor(full_stress),
        'oos_net_pf': net_profit_factor(base_pnl),
        'oos_stress_net_pf': net_profit_factor(stress_pnl),
        'oos_net_pnl': float(base_pnl.sum()) if len(oos) else 0.0,
        'oos_stress_net_pnl': float(stress_pnl.sum()) if len(oos) else 0.0,
        'oos_win_sum': oos_win,
        'oos_loss_abs': oos_loss,
        'oos_stress_win_sum': oos_stress_win,
        'oos_stress_loss_abs': oos_stress_loss,
    }


def verdict(oos_metrics: dict, stress_oos_metrics: dict, full_stress_pf,
            min_trades: int) -> str:
    """PROMPT.md §3.4 label for one verified cell.

    The gates mirror `scripts/candidate_check.py` exactly:

        credible candidate : net OOS PF > 1, net OOS Sharpe > 0, at least
                             `min_trades` OOS trades, and net PF still > 1
                             under 2x cost stress in both the full sample and
                             the out-of-sample window
        exploratory signal : net OOS PF > 1 and at least `min_trades` OOS
                             trades, but one of the other gates fails
        rejected           : everything else
    """
    n_oos = int(oos_metrics.get('trade_count') or 0)
    oos_pf = oos_metrics.get('net_profit_factor') or 0.0
    oos_sharpe = oos_metrics.get('sharpe_ratio') or 0.0
    stress_oos_pf = stress_oos_metrics.get('net_profit_factor') or 0.0
    if n_oos < min_trades:
        return 'rejected'
    if (oos_pf > 1.0 and oos_sharpe > 0.0
            and (full_stress_pf or 0.0) > 1.0 and stress_oos_pf > 1.0):
        return 'credible candidate'
    if oos_pf > 1.0:
        return 'exploratory signal'
    return 'rejected'


def verify_cell(symbol: str, df: pd.DataFrame, fast: int, slow: int,
                oos_fraction: float, stress_multiplier: float, config: dict) -> dict:
    """Re-run one cell through the real backtest, in and out of sample.

    Returns the base-cost and stressed-cost out-of-sample metric sets.
    """
    legs = {}
    for name, taker, slip in (
            ('oos', config['taker_fee_bps'], config['slippage_bps']),
            ('stress_oos', config['taker_fee_bps'] * stress_multiplier,
             config['slippage_bps'] * stress_multiplier)):
        _, _, metrics = run_cell(
            symbol, df, fast, slow, taker, slip, config['rr'],
            config['stricter_trend'], config['min_risk_atr'], config['atr_threshold'],
            config['conservative_exit'], oos_fraction=oos_fraction,
            sizing=config['sizing'], risk_fraction=config['risk_fraction'],
            max_notional_multiple=config['max_notional_multiple'],
        )
        legs[name] = metrics
    return legs


def window_sensitivity(rows: list, fixture_base: str, fractions: list,
                       stress_multiplier: float, config: dict, min_trades: int) -> list:
    """Re-verify a set of cells at several out-of-sample window sizes.

    The out-of-sample window is a single choice (the trailing 35 % of the
    bars). A verdict that only holds at one window length is an artifact of
    that choice, so the closest survivors are re-run at every fraction.
    """
    out = []
    for row in rows:
        symbol = row['symbol']
        df = load_ohlcv_csv(str(Path(fixture_base) / f"{symbol.replace('/', '_')}.csv"))
        per_window = []
        for fraction in fractions:
            legs = verify_cell(symbol, df, row['P_fast'], row['P_slow'], fraction,
                               stress_multiplier, config)
            label = verdict(legs['oos'], legs['stress_oos'], row['stress_net_pf'], min_trades)
            per_window.append({
                'oos_fraction': fraction,
                'oos_trades': int(legs['oos'].get('trade_count') or 0),
                'oos_net_pf': legs['oos'].get('net_profit_factor'),
                'oos_sharpe': legs['oos'].get('sharpe_ratio'),
                'stress_oos_net_pf': legs['stress_oos'].get('net_profit_factor'),
                'decision_label': label,
            })
        out.append({
            'symbol': symbol,
            'P_fast': row['P_fast'],
            'P_slow': row['P_slow'],
            'full_sample_net_pf': row['in_sample_net_pf'],
            'full_sample_stress_net_pf': row['stress_net_pf'],
            'windows': per_window,
        })
    return out


def parse_cells(spec: str) -> list:
    """Parse a "SYMBOL/USDT:fast:slow,SYMBOL/USDT:fast:slow" cell list."""
    out = []
    for item in spec.split(','):
        symbol, fast, slow = item.strip().split(':')
        out.append((symbol.strip(), int(fast), int(slow)))
    return out


def compare_with_candidate_check(rows: list, candidate_check_dir: Path) -> dict:
    """Compare the blotter screen with an existing candidate-check artifact.

    `scripts/candidate_check.py` re-runs the named cells through the real
    backtest, so its out-of-sample numbers are authoritative. Comparing them
    with the blotter screen of the same cells measures how faithful the
    screen is, which is what licenses using the screen on the other 17 000+
    cells.
    """
    summary_path = Path(candidate_check_dir) / 'summary.json'
    if not summary_path.exists():
        return {'available': False}
    payload = json.loads(summary_path.read_text())
    index = {(r['symbol'], r['P_fast'], r['P_slow']): r for r in payload.get('cells', [])}
    compared = []
    for row in rows:
        key = (row['symbol'], row['P_fast'], row['P_slow'])
        if key not in index:
            continue
        exact = index[key]['legs']['oos']
        exact_pf = exact.get('net_profit_factor')
        screen_pf = row['oos_net_pf']
        compared.append({
            'symbol': key[0],
            'P_fast': key[1],
            'P_slow': key[2],
            'screen_oos_pf': screen_pf,
            'exact_oos_pf': exact_pf,
            'screen_oos_trades': row['oos_trades'],
            'exact_oos_trades': exact.get('trade_count'),
        })
    # Cells where both runs produced an out-of-sample profit factor are the
    # ones the screen can actually be scored on; a cell with no out-of-sample
    # trade in both runs agrees by construction and is counted separately.
    scored = [c for c in compared
              if c['screen_oos_pf'] is not None and c['exact_oos_pf'] is not None]
    pf_deltas = [abs(c['screen_oos_pf'] - c['exact_oos_pf']) for c in scored]
    trade_deltas = [abs(c['screen_oos_trades'] - c['exact_oos_trades'])
                    for c in compared if c['exact_oos_trades'] is not None]
    return {
        'available': True,
        'source': str(candidate_check_dir),
        'n_compared': len(compared),
        'n_with_oos_trades': len(scored),
        'n_both_without_oos_trades': sum(
            1 for c in compared
            if c['screen_oos_trades'] == 0 and c['exact_oos_trades'] == 0),
        'max_abs_pf_delta': max(pf_deltas) if pf_deltas else None,
        'mean_abs_pf_delta': (sum(pf_deltas) / len(pf_deltas)) if pf_deltas else None,
        'max_abs_trade_delta': max(trade_deltas) if trade_deltas else None,
        'sign_agreement': sum(1 for c in scored
                               if (c['screen_oos_pf'] > 1.0) == (c['exact_oos_pf'] > 1.0)),
        'cells': compared,
    }


def symbol_bars(fixture_base: str, symbol: str, cache: dict) -> int:
    """Number of bars of a symbol's fixture (cached per symbol)."""
    if symbol not in cache:
        path = Path(fixture_base) / f"{symbol.replace('/', '_')}.csv"
        cache[symbol] = len(load_ohlcv_csv(str(path)))
    return cache[symbol]


def screen_run(run_dir: Path, fixture_base: str, oos_fraction: float,
               stress_multiplier: float, screen_pf: float, min_trades: int) -> list:
    """Stage 1: out-of-sample screen for every cell of the run."""
    rows = []
    bars_cache = {}
    results_root = run_dir / 'results'
    for sym_dir in sorted(results_root.iterdir()):
        if not sym_dir.is_dir():
            continue
        symbol = sym_dir.name.replace('_', '/')
        n_bars = symbol_bars(fixture_base, symbol, bars_cache)
        entry_start = entry_start_index(n_bars, oos_fraction)
        for cell_dir in sorted(sym_dir.iterdir()):
            summary_path = cell_dir / 'summary.json'
            trades_path = cell_dir / TRADES_FILENAME
            legacy_trades_path = cell_dir / LEGACY_TRADES_FILENAME
            if not cell_dir.is_dir() or not summary_path.exists():
                continue
            if not trades_path.exists() and not legacy_trades_path.exists():
                continue
            summary = json.loads(summary_path.read_text())
            if summary.get('blocked'):
                continue
            stats = screen_cell(read_trades(cell_dir), entry_start, stress_multiplier)
            stored_pf = float(summary.get('net_profit_factor') or 0.0)
            # Self-check: the blotter-derived full-sample net PF must reproduce
            # the metric the grid run stored for the same cell. A mismatch
            # would mean the blotter and the summary disagree, which would
            # invalidate every out-of-sample number derived from the blotter.
            matches = (stats['net_pf'] is not None
                       and abs(stats['net_pf'] - stored_pf) <= 1e-9 * max(1.0, abs(stored_pf)))
            rows.append({
                'symbol': symbol,
                'P_fast': int(summary['P_fast']),
                'P_slow': int(summary['P_slow']),
                'n_bars': n_bars,
                'entry_start_index': entry_start,
                'artifact_layout': 'gzip' if trades_path.exists() else 'legacy-csv',
                **stats,
                'in_sample_net_pf': stored_pf,
                'full_sample_pf_matches_summary': bool(matches),
            })
    return rows


def screen_survivors(rows: list, screen_pf: float, min_trades: int) -> list:
    """Cells the loose screen keeps for exact verification."""
    return [r for r in rows
            if r['oos_trades'] >= min_trades and (r['oos_net_pf'] or 0.0) > screen_pf]


def describe_distribution(values: list) -> dict:
    """Summary statistics of a per-cell metric distribution."""
    arr = np.asarray([v for v in values if v is not None], dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size == 0:
        return {'n': 0}
    return {
        'n': int(arr.size),
        'mean': float(arr.mean()),
        'median': float(np.median(arr)),
        'p05': float(np.percentile(arr, 5)),
        'p25': float(np.percentile(arr, 25)),
        'p75': float(np.percentile(arr, 75)),
        'p95': float(np.percentile(arr, 95)),
        'max': float(arr.max()),
        'min': float(arr.min()),
    }


def write_report(out_dir: Path, payload: dict) -> None:
    """Write the human-readable audit report."""
    lines = []
    lines.append('# Grid-Wide Out-of-Sample Audit — EMA Hourly Continuation\n')
    lines.append(f"**Source run:** `{payload['source_run']}`")
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Universe:** {payload['n_symbols']} symbols, "
                 f"{payload['n_cells']} grid cells")
    lines.append(f"**OOS window:** trailing {payload['oos_fraction']:.0%} of each "
                 f"symbol's bars, entries restricted to the window")
    lines.append(f"**Cost stress:** {payload['stress_multiplier']:g}x fees and slippage "
                 f"(base {payload['base_costs_bps']['taker']:g} bps taker + "
                 f"{payload['base_costs_bps']['slippage']:g} bps slippage per side)\n")

    lines.append('## Why this leg exists\n')
    lines.append(f"The pipeline's OOS gate was only ever applied to the "
                 f"{payload['n_in_sample_winners']} cells whose *in-sample* net PF "
                 f"exceeded 1. This leg applies the same out-of-sample window to all "
                 f"{payload['n_cells']} cells, so a cell whose in-sample window was "
                 f"unlucky cannot hide a survivor from the program.\n")

    coverage = payload['oos_coverage']
    lines.append('## Leg 1 — Out-of-sample coverage\n')
    lines.append('| Metric | Value |')
    lines.append('|---|---|')
    lines.append(f"| Cells screened | {coverage['n_cells']} |")
    lines.append(f"| Cells with at least one out-of-sample trade | "
                 f"{coverage['n_cells_with_oos_trades']} |")
    lines.append(f"| Cells with no out-of-sample trade | "
                 f"{coverage['n_cells_without_oos_trades']} |")
    lines.append(f"| Cells with at least {payload['min_trades']} out-of-sample trades | "
                 f"{coverage['n_cells_with_enough_oos_trades']} |")
    lines.append(f"| Pooled out-of-sample net PF (all cells) | "
                 f"{fmt_pf(coverage['pooled_oos_net_pf'])} |")
    lines.append(f"| Pooled out-of-sample net PF under {payload['stress_multiplier']:g}x costs | "
                 f"{fmt_pf(coverage.get('pooled_oos_stress_net_pf'))} |")
    lines.append(f"| Pooled out-of-sample net P&L | "
                 f"{coverage['pooled_oos_net_pnl']:.0f} |")
    lines.append(f"| Cells whose blotter net PF disagrees with the stored summary | "
                 f"{payload['n_cells_full_sample_pf_mismatch']} |")
    lines.append(f"| Cells read from the legacy uncompressed blotter layout | "
                 f"{payload['n_cells_legacy_layout']} |")
    lines.append('')

    dist = payload['oos_net_pf_distribution']
    lines.append('## Leg 2 — Out-of-sample net PF across the whole grid\n')
    lines.append('| Statistic | Out-of-sample net PF | In-sample net PF |')
    lines.append('|---|---|---|')
    lines.append(f"| cells with a defined net PF | {dist.get('n', 0)} | "
                 f"{payload['in_sample_net_pf_distribution'].get('n', 0)} |")
    for key in ('mean', 'median', 'p05', 'p25', 'p75', 'p95', 'max'):
        if key not in dist:
            continue
        lines.append(f"| {key} | {dist[key]:.4f} | "
                     f"{payload['in_sample_net_pf_distribution'][key]:.4f} |")
    lines.append('')
    lines.append(f"The {payload['n_cells'] - dist.get('n', 0)} cells without a single "
                 f"out-of-sample trade are missing evidence, not a loss, and are excluded "
                 f"from the distribution.\n")
    lines.append(f"- Cells with out-of-sample net PF > 1: "
                 f"**{payload['n_cells_oos_pf_gt_1']}** of {payload['n_cells']} "
                 f"({payload['frac_cells_oos_pf_gt_1']:.2%}).")
    lines.append(f"- Expected under a no-edge null: ~{NULL_FRAC_NET_PF_GT_1:.0%} "
                 f"(excess {payload['excess_vs_null']:+.4f}).")
    lines.append(f"- Cells with out-of-sample net PF > 1 **and** at least "
                 f"{payload['min_trades']} out-of-sample trades: "
                 f"**{payload['n_cells_oos_pf_gt_1_with_trades']}**.")
    lines.append(f"- Cells with out-of-sample net PF > 1, at least "
                 f"{payload['min_trades']} out-of-sample trades, and out-of-sample "
                 f"net PF still > 1 under {payload['stress_multiplier']:g}x costs: "
                 f"**{payload['n_cells_oos_stress_pf_gt_1_with_trades']}**.")
    lines.append('')

    lines.append('## Leg 3 — Screen survivors (verified with a real backtest)\n')
    lines.append(f"Screen: out-of-sample net PF > {payload['screen_pf']} with at least "
                 f"{payload['min_trades']} out-of-sample trades. "
                 f"{payload['n_survivors']} cell(s) kept.\n")
    lines.append('| Symbol | Cell | OOS trades | Screen OOS PF | Screen OOS stress PF | '
                 'Exact OOS PF | Exact OOS Sharpe | Exact stress OOS PF | Label |')
    lines.append('|---|---|---|---|---|---|---|---|---|')
    for row in payload['verified']:
        exact_oos = row['legs']['oos']
        exact_stress = row['legs']['stress_oos']
        lines.append(
            f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
            f"{row['oos_trades']} | {fmt_pf(row['oos_net_pf'])} | "
            f"{fmt_pf(row['oos_stress_net_pf'])} | "
            f"{fmt_pf(exact_oos.get('net_profit_factor'))} | "
            f"{(exact_oos.get('sharpe_ratio') or 0.0):.4f} | "
            f"{fmt_pf(exact_stress.get('net_profit_factor'))} | "
            f"{row['decision_label']} |")
    lines.append('')

    closest = payload['closest_survivors']
    lines.append('## Leg 3b — The closest survivors: cells that also survive the cost stress\n')
    lines.append('These are the verified cells whose out-of-sample net PF is above 1 both '
                 'at the registered costs and at 2x costs. The last three columns are the '
                 'full-sample result, which is what a promotion would have to survive as '
                 'well.\n')
    lines.append('| Symbol | Cell | OOS trades | Exact OOS PF | Exact OOS Sharpe | '
                 'Exact stress OOS PF | Full-sample net PF | Full-sample stress PF | Label |')
    lines.append('|---|---|---|---|---|---|---|---|---|')
    for row in closest:
        exact_oos = row['legs']['oos']
        exact_stress = row['legs']['stress_oos']
        lines.append(
            f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
            f"{row['oos_trades']} | {fmt_pf(exact_oos.get('net_profit_factor'))} | "
            f"{(exact_oos.get('sharpe_ratio') or 0.0):.4f} | "
            f"{fmt_pf(exact_stress.get('net_profit_factor'))} | "
            f"{fmt_pf(row['in_sample_net_pf'])} | {fmt_pf(row['stress_net_pf'])} | "
            f"{row['decision_label']} |")
    lines.append('')
    if not closest:
        lines.append('No verified cell keeps an out-of-sample net PF above 1 at 2x costs.\n')

    reasons = payload['exploratory_reasons']
    lines.append('## Leg 3c — Why the exploratory signals did not promote\n')
    lines.append('| Blocking gate | Cells |')
    lines.append('|---|---|')
    for reason, count in reasons.items():
        lines.append(f'| {reason} | {count} |')
    lines.append('')

    sensitivity = payload.get('window_sensitivity') or []
    if sensitivity:
        lines.append('## Leg 3d — Does the verdict depend on the out-of-sample window?\n')
        lines.append('The closest survivors were re-verified at every window length. A cell '
                     'that only looks good at one window length is an artifact of that '
                     'choice.\n')
        fractions = payload.get('window_fractions') or []
        lines.append('| Symbol | Cell | ' + ' | '.join(
            f'OOS {f:.0%} PF / stress PF' for f in fractions) + ' |')
        lines.append('|---|---|' + '---|' * len(fractions))
        for row in sensitivity:
            cells_text = ' | '.join(
                f"{fmt_pf(w['oos_net_pf'])} / {fmt_pf(w['stress_oos_net_pf'])}"
                for w in row['windows'])
            lines.append(f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                         f"{cells_text} |")
        lines.append('')
        lines.append('| Symbol | Cell | ' + ' | '.join(
            f'OOS {f:.0%} trades' for f in fractions) + ' |')
        lines.append('|---|---|' + '---|' * len(fractions))
        for row in sensitivity:
            cells_text = ' | '.join(str(w['oos_trades']) for w in row['windows'])
            lines.append(f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                         f"{cells_text} |")
        lines.append('')

    lines.append('## Leg 4 — Selection-bias check against the in-sample winners\n')
    lines.append('| Population | Cells | Out-of-sample PF > 1 | With enough OOS trades | '
                 'Survive the full §3.4 gate |')
    lines.append('|---|---|---|---|---|')
    for row in payload['selection_bias']:
        lines.append(f"| {row['population']} | {row['cells']} | "
                     f"{row['oos_pf_gt_1']} | {row['oos_pf_gt_1_with_trades']} | "
                     f"{row['survive_gate']} |")
    lines.append('')

    fidelity = payload.get('screen_fidelity', {})
    if fidelity.get('available'):
        lines.append('## Leg 5 — Screen fidelity against the exact backtest\n')
        lines.append(f"The stage-1 screen was compared with the authoritative numbers of "
                     f"`{fidelity['source']}`, which re-ran the same cells through the "
                     f"real backtest.\n")
        lines.append('| Metric | Value |')
        lines.append('|---|---|')
        lines.append(f"| Cells compared | {fidelity['n_compared']} |")
        lines.append(f"| Cells with an out-of-sample profit factor in both runs | "
                     f"{fidelity['n_with_oos_trades']} |")
        lines.append(f"| Cells with no out-of-sample trade in either run (agree by "
                     f"construction) | {fidelity['n_both_without_oos_trades']} |")
        lines.append(f"| Mean absolute net PF difference (scored cells) | "
                     f"{fmt_pf(fidelity['mean_abs_pf_delta'])} |")
        lines.append(f"| Max absolute net PF difference (scored cells) | "
                     f"{fmt_pf(fidelity['max_abs_pf_delta'])} |")
        lines.append(f"| Max absolute trade-count difference | "
                     f"{fidelity['max_abs_trade_delta']} |")
        lines.append(f"| Scored cells where both put the net PF on the same side of 1.0 | "
                     f"{fidelity['sign_agreement']} of {fidelity['n_with_oos_trades']} |")
        lines.append('')
        lines.append('The screen can be optimistic: it reuses the full-sample trade blotter, '
                     'so the out-of-sample window inherits the in-sample equity path and the '
                     'position state at the boundary. That is why the screen threshold is loose '
                     'and every verdict is taken from the exact stage-2 numbers.\n')

    lines.append('## Gates (PROMPT.md §3.3, §3.4)\n')
    lines.append(f"- Grid cells evaluated out of sample: **{payload['n_cells']}** "
                 f"(the pipeline had only checked {payload['n_in_sample_winners']}).")
    lines.append(f"- Credible candidates found anywhere in the grid: "
                 f"**{payload['n_credible']}**.")
    lines.append(f"- Exploratory signals found anywhere in the grid: "
                 f"**{payload['n_exploratory']}**.")
    lines.append(f"- Screen survivors verified with a real backtest: "
                 f"**{len(payload['verified'])}**.")
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def fmt_pf(value) -> str:
    """Format a profit factor for the markdown report."""
    if value is None:
        return 'n/a'
    if value == float('inf'):
        return 'inf'
    return f'{value:.4f}'


def main():
    parser = argparse.ArgumentParser(
        description='Grid-wide out-of-sample and cost-stress audit')
    parser.add_argument('--run', type=str, required=True,
                        help='results/<RUNID>_grid directory')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--oos-fraction', type=float, default=0.35,
                        help='Trailing out-of-sample fraction of each symbol\'s bars')
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--min-trades', type=int, default=30,
                        help='Minimum out-of-sample trades for the §3.4 gates')
    parser.add_argument('--screen-pf', type=float, default=0.9,
                        help='Loose stage-1 out-of-sample PF threshold (default 0.9)')
    parser.add_argument('--max-verify', type=int, default=0,
                        help='Cap the number of exact re-runs (0 = no cap)')
    parser.add_argument('--cells', type=str, default=None,
                        help='Verify only these "SYMBOL/USDT:fast:slow" cells')
    parser.add_argument('--compare-candidate-check', type=str, default=None,
                        help='results/<TS>_candidate_check dir; the script measures how '
                             'faithful the blotter screen is against its exact numbers')
    parser.add_argument('--window-fractions', type=float, nargs='*',
                        default=[0.20, 0.35, 0.50],
                        help='Out-of-sample window lengths the closest survivors are '
                             're-verified at (empty list disables the leg)')
    parser.add_argument('--out', type=str, default=None,
                        help='Output dir (default results/<TS>_oos_grid_scan)')
    args = parser.parse_args()

    run_dir = Path(args.run)
    if not (run_dir / 'results').exists():
        raise SystemExit(f'no grid results found in {run_dir}')

    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    out_dir = Path(args.out) if args.out else Path('results') / f'{timestamp}_oos_grid_scan'
    out_dir.mkdir(parents=True, exist_ok=True)

    # The audit has to re-run the cells of the run it audits, so it uses the
    # run's own config: a mutation run's rule is not the baseline rule.
    config = load_run_config(run_dir)
    rows = screen_run(run_dir, args.fixture_base, args.oos_fraction,
                      args.stress_multiplier, args.screen_pf, args.min_trades)
    if not rows:
        raise SystemExit(f'no cells found in {run_dir}')

    survivors = screen_survivors(rows, args.screen_pf, args.min_trades)
    if args.cells:
        wanted = set(parse_cells(args.cells))
        survivors = [r for r in survivors
                     if (r['symbol'], r['P_fast'], r['P_slow']) in wanted]
    if args.max_verify:
        survivors = sorted(survivors, key=lambda r: -(r['oos_net_pf'] or 0.0))[:args.max_verify]

    # Stage 2: exact verification through the real backtest.
    bars_cache = {}
    verified = []
    for row in survivors:
        symbol = row['symbol']
        df = load_ohlcv_csv(str(Path(args.fixture_base) / f"{symbol.replace('/', '_')}.csv"))
        legs = verify_cell(symbol, df, row['P_fast'], row['P_slow'], args.oos_fraction,
                           args.stress_multiplier, config)
        label = verdict(legs['oos'], legs['stress_oos'], row['stress_net_pf'], args.min_trades)
        verified.append({**row, 'legs': legs, 'decision_label': label})
        print(f"{symbol} P{row['P_fast']}_{row['P_slow']}: screen oosPF="
              f"{fmt_pf(row['oos_net_pf'])} (n={row['oos_trades']}) -> "
              f"exact oosPF={fmt_pf(legs['oos'].get('net_profit_factor'))} -> {label}",
              flush=True)

    n_credible = sum(1 for r in verified if r['decision_label'] == 'credible candidate')
    n_exploratory = sum(1 for r in verified if r['decision_label'] == 'exploratory signal')

    # The cells that come closest to a promotion: a verified out-of-sample net
    # PF above 1 that also survives the 2x cost stress.
    closest = [r for r in verified
               if (r['legs']['oos'].get('net_profit_factor') or 0.0) > 1.0
               and (r['legs']['stress_oos'].get('net_profit_factor') or 0.0) > 1.0]

    # Why each exploratory signal was not promoted.
    reasons = {
        'out-of-sample net PF still > 1 under 2x costs': 0,
        'full-sample net PF still > 1 under 2x costs': 0,
        'out-of-sample Sharpe > 0': 0,
    }
    for r in verified:
        if r['decision_label'] != 'exploratory signal':
            continue
        if (r['legs']['stress_oos'].get('net_profit_factor') or 0.0) <= 1.0:
            reasons['out-of-sample net PF still > 1 under 2x costs'] += 1
        if (r['stress_net_pf'] or 0.0) <= 1.0:
            reasons['full-sample net PF still > 1 under 2x costs'] += 1
        if (r['legs']['oos'].get('sharpe_ratio') or 0.0) <= 0.0:
            reasons['out-of-sample Sharpe > 0'] += 1

    # Leg 3d: does the verdict depend on the length of the out-of-sample
    # window? The closest survivors are re-run at every window fraction.
    sensitivity = []
    if args.window_fractions:
        sensitivity = window_sensitivity(closest, args.fixture_base,
                                         args.window_fractions, args.stress_multiplier,
                                         config, args.min_trades)

    # Selection-bias comparison: the in-sample winners against the whole grid.
    in_sample_winners = [r for r in rows if r['in_sample_net_pf'] > 1.0]
    selection_bias = []
    for name, subset in (('in-sample net PF > 1 (checked by the pipeline)', in_sample_winners),
                          ('all cells', rows)):
        selection_bias.append({
            'population': name,
            'cells': len(subset),
            'oos_pf_gt_1': sum(1 for r in subset if (r['oos_net_pf'] or 0.0) > 1.0),
            'oos_pf_gt_1_with_trades': sum(
                1 for r in subset
                if (r['oos_net_pf'] or 0.0) > 1.0 and r['oos_trades'] >= args.min_trades),
            'survive_gate': sum(1 for r in verified
                                if (r['symbol'], r['P_fast'], r['P_slow']) in
                                {(v['symbol'], v['P_fast'], v['P_slow']) for v in subset}
                                and r['decision_label'] == 'credible candidate'),
        })

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_run': str(run_dir),
        'oos_fraction': args.oos_fraction,
        'stress_multiplier': args.stress_multiplier,
        'min_trades': args.min_trades,
        'screen_pf': args.screen_pf,
        'base_costs_bps': {'taker': config['taker_fee_bps'],
                           'slippage': config['slippage_bps']},
        'config': config,
        'n_symbols': len({r['symbol'] for r in rows}),
        'n_cells': len(rows),
        'n_in_sample_winners': len(in_sample_winners),
        'oos_coverage': {
            'n_cells': len(rows),
            'n_cells_with_oos_trades': sum(1 for r in rows if r['oos_trades'] > 0),
            'n_cells_without_oos_trades': sum(1 for r in rows if r['oos_trades'] == 0),
            'n_cells_with_enough_oos_trades': sum(
                1 for r in rows if r['oos_trades'] >= args.min_trades),
            'pooled_oos_net_pf': None,
            'pooled_oos_net_pnl': sum(r['oos_net_pnl'] for r in rows),
        },
        'oos_net_pf_distribution': describe_distribution([r['oos_net_pf'] for r in rows]),
        'in_sample_net_pf_distribution': describe_distribution(
            [r['in_sample_net_pf'] for r in rows]),
        'n_cells_oos_pf_gt_1': sum(1 for r in rows if (r['oos_net_pf'] or 0.0) > 1.0),
        'frac_cells_oos_pf_gt_1': sum(1 for r in rows
                                      if (r['oos_net_pf'] or 0.0) > 1.0) / len(rows),
        'excess_vs_null': sum(1 for r in rows if (r['oos_net_pf'] or 0.0) > 1.0) / len(rows)
                           - NULL_FRAC_NET_PF_GT_1,
        'n_cells_oos_pf_gt_1_with_trades': sum(
            1 for r in rows if (r['oos_net_pf'] or 0.0) > 1.0
            and r['oos_trades'] >= args.min_trades),
        'n_cells_oos_stress_pf_gt_1_with_trades': sum(
            1 for r in rows if (r['oos_stress_net_pf'] or 0.0) > 1.0
            and r['oos_trades'] >= args.min_trades),
        'n_survivors': len(survivors),
        'n_credible': n_credible,
        'n_exploratory': n_exploratory,
        'closest_survivors': closest,
        'exploratory_reasons': reasons,
        'window_sensitivity': sensitivity,
        'window_fractions': args.window_fractions,
        'selection_bias': selection_bias,
        'verified': verified,
        'n_cells_full_sample_pf_mismatch': sum(
            1 for r in rows if not r['full_sample_pf_matches_summary']),
        'n_cells_legacy_layout': sum(1 for r in rows
                                     if r['artifact_layout'] == 'legacy-csv'),
    }
    if args.compare_candidate_check:
        payload['screen_fidelity'] = compare_with_candidate_check(
            rows, Path(args.compare_candidate_check))
    else:
        payload['screen_fidelity'] = {'available': False}
    # Pooled out-of-sample net PF over the trade-level P&L of every cell.
    pooled_win = sum(r['oos_win_sum'] for r in rows)
    pooled_loss = sum(r['oos_loss_abs'] for r in rows)
    payload['oos_coverage']['pooled_oos_net_pf'] = (
        pooled_win / pooled_loss if pooled_loss > 0
        else (float('inf') if pooled_win > 0 else 0.0))
    pooled_stress_win = sum(r['oos_stress_win_sum'] for r in rows)
    pooled_stress_loss = sum(r['oos_stress_loss_abs'] for r in rows)
    payload['oos_coverage']['pooled_oos_stress_net_pf'] = (
        pooled_stress_win / pooled_stress_loss if pooled_stress_loss > 0
        else (float('inf') if pooled_stress_win > 0 else 0.0))

    with open(out_dir / 'cells.jsonl', 'w') as f:
        for row in rows:
            f.write(json.dumps(row, default=str) + '\n')
    with open(out_dir / 'summary.json', 'w') as f:
        json.dump(payload, f, indent=2, default=str)
    with open(out_dir / 'config.json', 'w') as f:
        json.dump({
            'timestamp': timestamp,
            'source_run': str(run_dir),
            'fixture_base': args.fixture_base,
            'oos_fraction': args.oos_fraction,
            'stress_multiplier': args.stress_multiplier,
            'min_trades': args.min_trades,
            'screen_pf': args.screen_pf,
            'max_verify': args.max_verify,
            'cells': args.cells,
            'config': config,
            'command': (f'PYTHONPATH=. python3 scripts/oos_grid_scan.py --run {run_dir} '
                        f'--oos-fraction {args.oos_fraction} --min-trades {args.min_trades} '
                        f'--screen-pf {args.screen_pf}'),
        }, f, indent=2)
    write_report(out_dir, payload)

    print(f'\nScreened {payload["n_cells"]} cells over {payload["n_symbols"]} symbols')
    print(f'Cells with OOS net PF > 1: {payload["n_cells_oos_pf_gt_1"]} '
          f'({payload["frac_cells_oos_pf_gt_1"]:.2%})')
    print(f'Cells with OOS net PF > 1 and >= {args.min_trades} OOS trades: '
          f'{payload["n_cells_oos_pf_gt_1_with_trades"]}')
    print(f'...and still > 1 under {args.stress_multiplier:g}x costs: '
          f'{payload["n_cells_oos_stress_pf_gt_1_with_trades"]}')
    print(f'Screen survivors verified: {len(verified)} '
          f'({n_credible} credible, {n_exploratory} exploratory)')
    print(f'Wrote {out_dir}/summary.md and summary.json')


if __name__ == '__main__':
    main()
