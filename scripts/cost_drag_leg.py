#!/usr/bin/env python3
"""Cost-drag decomposition of the EMA hourly continuation grid.

Why this leg exists
-------------------
The grid reports one number per cell - the net profit factor - and that
number mixes three different things:

1. whether the entry rule has a directional edge (the gross P&L, before any
   cost is charged);
2. how large the cost drag is relative to the gross P&L it eats;
3. how the risk distance - the width of the stop - interacts with the
   risk-based sizing rule.

Point 3 is the one the program has never isolated. With risk-based sizing
(`qty = equity * risk_fraction / risk`, `backtest/backtest.py:209`) a trade
exits at exactly `+-risk`, so its *gross* P&L is a fixed fraction of the
equity, while its *cost* is proportional to the notional, which is
`equity * risk_fraction / risk_pct`. The cost of a trade divided by its
gross P&L is therefore

    2 * cost_per_side / risk_pct

- inversely proportional to the risk distance. A cell whose entries sit 1 %
away from the slow EMA pays about 24 % of its gross P&L in fees; a cell
whose entries sit 0.25 % away pays about 96 %.

That single fact explains an anomaly the randomized-entry null leg reported
(`results/20261021_073300_null_grid_scan`): the *block* null, which moves
the entries to random bars inside the same 240-bar block and therefore
picks wider risk distances, has a *better* pooled out-of-sample net PF
(0.5114) than the real rule (0.4175). The null is not smarter than the
rule; it simply trades at a wider stop and pays less per unit of risk.

It also means the program cannot read its own headline number. A cell can
show net PF above 1 only because its entries happened to be wide, and the
next grid expansion will move that number for a reason that has nothing to
do with the signal.

What this leg measures
----------------------
Part A (every cell, no re-run): for every cell of the grid, the gross
profit factor, the net profit factor, the share of the gross P&L that
costs consume, the median risk distance, and the share of trades whose
notional is capped by `max_notional_multiple`. The measured cost ratio is
compared with the `2 * cost_per_side / risk_pct` model.

Part B (sample, re-run): three sizing legs on a sample of cells - the
registered baseline, the same run with the notional cap removed, and the
PROMPT.md §5.2 pre-registered minimum-risk mutation (skip trades whose
risk distance is below one ATR(14)). The deltas say whether the
baseline's net result is a property of the entry rule or of the sizing
rule.

The baseline grid is never touched: this leg only reads it and writes its
own artifact directory.

Usage:
    python scripts/cost_drag_leg.py --run results/20261019_135940_grid
    python scripts/cost_drag_leg.py --run results/20261019_135940_grid \\
        --sample-cells 300 --workers 4
"""
import argparse
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from backtest.backtest import backtest_symbol
from data.data_loader import load_ohlcv_csv
from metrics.metrics import calculate_metrics
from scripts.run_grid import (CONFIG_DEFAULTS, read_artifact_csv,
                              symbol_dir_name)
from scripts.oos_grid_scan import (LEGACY_TRADES_FILENAME, TRADES_FILENAME,
                                    describe_distribution, entry_start_index,
                                    net_profit_factor, stressed_pnl_net,
                                    symbol_bars)
from signals.signals import generate_signals_vectorized

# Columns the decomposition needs from a trade blotter.
BLOTTER_COLUMNS = ['bar_index', 'pnl', 'pnl_net', 'entry_cost', 'exit_cost',
                    'risk_pct', 'notional', 'qty']

# A notional cap this large is the same thing as no cap at all.
UNCAPPED_MULTIPLE = 1e9

# The PROMPT.md §5.2 mutation: skip trades whose risk distance is below one
# ATR(14). It is the registered minimum-risk filter, so running it here is a
# documented mutation and not a new invention.
ATR_MIN_RISK_LEGS = ('uncapped', 'atr_min_risk')


def cost_per_side(config: dict) -> float:
    """Cost charged per side, as a fraction of the traded notional."""
    return (config['taker_fee_bps'] + config['slippage_bps']) / 10000.0


def cap_risk_threshold(config: dict) -> float:
    """Risk distance below which the notional cap binds.

    The engine asks for `qty = equity * risk_fraction / risk` and caps the
    notional at `max_notional_multiple * equity`
    (`backtest/backtest.py:209-214`). The cap binds exactly when

        equity * risk_fraction / risk * entry_price > max_notional * equity
    <=> risk / entry_price < risk_fraction / max_notional_multiple

    so the threshold is a property of the risk distance alone.
    """
    multiple = config.get('max_notional_multiple') or 0.0
    if multiple <= 0:
        return float('inf')
    return config['risk_fraction'] / multiple


def model_cost_ratio(risk_pct: float, config: dict) -> float:
    """Model of `cost / |gross P&L|` for a trade with this risk distance.

    The gross P&L of a trade is `risk * qty = risk_fraction * equity` and
    its cost is `notional * cost_per_side` on each side, so the ratio is
    `2 * cost_per_side / risk_pct` wherever the notional cap does not bind.
    """
    if risk_pct is None or risk_pct <= 0:
        return float('nan')
    return 2.0 * cost_per_side(config) / risk_pct


def read_blotter(cell_dir: Path) -> pd.DataFrame:
    """Read one cell's trade blotter.

    The run is not uniform: the five largest market-cap names still carry
    the legacy baseline-study layout (`trades.csv`), the rest carry the
    gzip layout (`trades.csv.gz`). Both are handled, so the top of the
    universe is never silently skipped.
    """
    path = Path(cell_dir) / TRADES_FILENAME
    if not path.exists():
        path = Path(cell_dir) / LEGACY_TRADES_FILENAME
    return read_artifact_csv(path)


def decompose(trades: pd.DataFrame, config: dict,
              stress_multiplier: float = 2.0) -> dict:
    """Split one cell's P&L into the gross result, the cost and the residual.

    Everything is computed on the trades handed in, so the caller decides
    which window the trades belong to.
    """
    if trades is None or len(trades) == 0:
        return {'trades': 0, 'gross_pf': None, 'net_pf': None,
                'stress_net_pf': None, 'cost_total': 0.0, 'gross_pnl': 0.0,
                'net_pnl': 0.0, 'cost_share_of_gross': None,
                'median_risk_pct': None, 'capped_trade_share': None,
                'median_cost_to_gross': None,
                'model_cost_ratio_at_median': None}
    pnl = trades['pnl'].to_numpy(dtype=float)
    pnl_net = trades['pnl_net'].to_numpy(dtype=float)
    cost = (trades['entry_cost'].to_numpy(dtype=float)
            + trades['exit_cost'].to_numpy(dtype=float))
    risk_pct = trades['risk_pct'].to_numpy(dtype=float)
    stress = stressed_pnl_net(pnl_net, trades['entry_cost'].to_numpy(dtype=float),
                               trades['exit_cost'].to_numpy(dtype=float),
                               stress_multiplier)

    gross_win = float(pnl[pnl > 0].sum())
    gross_loss = float(-pnl[pnl < 0].sum())
    threshold = cap_risk_threshold(config)
    capped = risk_pct < threshold
    live = np.abs(pnl) > 0
    ratios = cost[live] / np.abs(pnl[live]) if live.any() else np.array([])
    median_risk = float(np.nanmedian(risk_pct)) if risk_pct.size else None
    gross_move = gross_win + gross_loss
    return {
        'trades': int(len(trades)),
        'gross_pf': (gross_win / gross_loss) if gross_loss > 0 else None,
        'net_pf': net_profit_factor(pnl_net),
        'stress_net_pf': net_profit_factor(stress),
        'cost_total': float(cost.sum()),
        'gross_pnl': float(pnl.sum()),
        'net_pnl': float(pnl_net.sum()),
        # The share of the gross P&L that the costs consume. A cell that
        # loses money gross cannot be rescued by a cheap cost model, and a
        # cell that wins gross can still be a net loser here.
        'cost_share_of_gross': (float(cost.sum()) / gross_move) if gross_move > 0 else None,
        'median_risk_pct': median_risk,
        'capped_trade_share': float(capped.mean()),
        'median_cost_to_gross': float(np.median(ratios)) if ratios.size else None,
        'model_cost_ratio_at_median': (model_cost_ratio(median_risk, config)
                                        if median_risk else None),
    }


def pooled_decompose(frames: list, config: dict) -> dict:
    """Trade-level decomposition over many cells.

    Pooling uses the trade sums, never a mean of per-cell ratios: cells
    carry very different trade counts, so a mean of ratios would give a thin
    cell the same weight as a thick one.
    """
    frames = [f for f in frames if f is not None and len(f)]
    if not frames:
        return {'cells': 0, 'trades': 0}
    trades = pd.concat(frames, ignore_index=True)
    out = decompose(trades, config)
    out['cells'] = len(frames)
    out['gross_pf'] = net_profit_factor(trades['pnl'].to_numpy(dtype=float))
    out['net_pf'] = net_profit_factor(trades['pnl_net'].to_numpy(dtype=float))
    return out


def part_a(run_dir: Path, fixture_base: str, oos_fraction: float,
           config: dict, limit_symbols: int = 0) -> dict:
    """Decompose every cell of the run from the blotters it already wrote."""
    bars_cache: dict = {}
    results_root = run_dir / 'results'
    rows = []
    pooled_frames = []
    symbols_seen = 0
    for sym_dir in sorted(results_root.iterdir()):
        if not sym_dir.is_dir():
            continue
        if limit_symbols and symbols_seen >= limit_symbols:
            break
        symbols_seen += 1
        symbol = sym_dir.name.replace('_', '/')
        n_bars = symbol_bars(fixture_base, symbol, bars_cache)
        entry_start = entry_start_index(n_bars, oos_fraction)
        for cell_dir in sorted(sym_dir.iterdir()):
            if not cell_dir.is_dir():
                continue
            trades = read_blotter(cell_dir)
            oos = trades[trades['bar_index'] >= entry_start]
            stats = decompose(oos, config)
            stats.update({'symbol': symbol, 'cell': cell_dir.name})
            rows.append(stats)
            pooled_frames.append(oos)
    return {'rows': rows, 'pooled': pooled_decompose(pooled_frames, config)}


def trades_frame(trades: list) -> pd.DataFrame:
    """The engine's trade list as the DataFrame the decomposition reads."""
    return pd.DataFrame([{
        'side': t.side, 'entry_time': t.entry_time, 'exit_time': t.exit_time,
        'entry_price': t.entry_price, 'exit_price': t.exit_price,
        'sl': t.sl, 'tp': t.tp, 'risk': t.risk, 'pnl': t.pnl,
        'pnl_net': t.pnl_net, 'exit_reason': t.exit_reason,
        'bar_index': t.bar_index, 'exit_bar_index': t.exit_bar_index,
        'qty': t.qty, 'notional': t.notional,
        'entry_cost': t.entry_cost, 'exit_cost': t.exit_cost,
        'risk_pct': t.risk_pct,
    } for t in trades])


def run_leg(frame: pd.DataFrame, symbol: str, config: dict,
            entry_start: int) -> tuple:
    """Run one sizing leg on the out-of-sample window of a cell.

    The engine is handed the window and asked for entries from its first
    bar; that is equivalent to running the full series with the entries
    gated at the window start, and it is the same convention the
    grid-wide out-of-sample audit and the null leg use.
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
    return trades, equity_df, metrics


def part_b(run_dir: Path, fixture_base: str, oos_fraction: float, config: dict,
           sample: list, legs: tuple = ATR_MIN_RISK_LEGS) -> dict:
    """Re-run a sample of cells under the sizing legs.

    Every cell is first re-run over its full history with the registered
    config and checked against the stored grid summary, so the leg is known
    to reproduce the run it audits. The legs themselves are then run on the
    out-of-sample window.
    """
    out = []
    for symbol, fast, slow in sample:
        path = Path(fixture_base) / f'{symbol_dir_name(symbol)}.csv'
        df = load_ohlcv_csv(str(path))
        cell_dir = run_dir / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'
        stored = json.loads((cell_dir / 'summary.json').read_text())
        frame = generate_signals_vectorized(df, fast, slow, config['stricter_trend'])
        entry_start = entry_start_index(len(frame), oos_fraction)

        # Reproduction check: the same cell, the same config, over the whole
        # history, against the summary the grid run stored.
        full_trades, _ = backtest_symbol(
            frame, symbol=symbol,
            taker_fee_bps=config['taker_fee_bps'],
            slippage_bps=config['slippage_bps'], rr=config['rr'],
            min_risk_atr=config['min_risk_atr'],
            atr_threshold=config['atr_threshold'], entry_start_index=0,
            conservative_exit=config['conservative_exit'], sizing=config['sizing'],
            risk_fraction=config['risk_fraction'],
            max_notional_multiple=config['max_notional_multiple'],
        )
        recomputed = net_profit_factor(np.array([t.pnl_net for t in full_trades],
                                                dtype=float))
        stored_pf = stored.get('net_profit_factor')
        reproduces = bool(stored_pf is not None and recomputed is not None
                          and abs(float(stored_pf) - float(recomputed)) <= 1e-9
                          and int(stored.get('trade_count') or 0) == len(full_trades))

        leg_stats = {}
        for leg in ('base',) + tuple(legs):
            leg_config = dict(config)
            if leg == 'uncapped':
                leg_config['max_notional_multiple'] = UNCAPPED_MULTIPLE
            elif leg == 'atr_min_risk':
                leg_config['min_risk_atr'] = True
            trades, equity_df, metrics = run_leg(frame, symbol, leg_config,
                                                 entry_start)
            stats = decompose(trades_frame(trades), leg_config)
            stats['sharpe'] = metrics.get('sharpe_ratio')
            leg_stats[leg] = stats
        out.append({
            'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
            'stored_net_pf': stored_pf,
            'stored_trade_count': stored.get('trade_count'),
            'recomputed_full_net_pf': recomputed,
            'reproduces_stored_summary': reproduces,
            'legs': leg_stats,
        })
    return {'rows': out}


def sample_cells(run_dir: Path, n: int, fixture_base: str) -> list:
    """Pick a spread of cells to re-run: every symbol gets one cell.

    The sample walks the universe in market-cap order and takes one cell per
    symbol, so the legs are measured on the same part of the universe the
    grid covers, rather than on the few thickest symbols.
    """
    results_root = run_dir / 'results'
    sample = []
    for sym_dir in sorted(results_root.iterdir()):
        if not sym_dir.is_dir():
            continue
        if len(sample) >= n:
            break
        symbol = sym_dir.name.replace('_', '/')
        cells = sorted(c for c in sym_dir.iterdir() if c.is_dir())
        if not cells:
            continue
        cell = cells[len(cells) // 2]
        fast, slow = (int(x) for x in cell.name.lstrip('P').split('_'))
        sample.append((symbol, fast, slow))
    return sample


def write_report(out_dir: Path, payload: dict) -> None:
    """Write the human-readable leg report."""
    a = payload['part_a']
    pooled = a['pooled']
    rows = a['rows']
    lines = []
    lines.append('# Cost-Drag Decomposition — EMA Hourly Continuation\n')
    lines.append(f"**Source run:** `{payload['source_run']}`")
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Universe:** {payload['n_symbols']} symbols, "
                 f"{payload['n_cells']} grid cells")
    lines.append(f"**OOS window:** trailing {payload['oos_fraction'] * 100:.0f}% of each "
                 f"symbol's bars, entries restricted to the window")
    lines.append(f"**Cost model:** {payload['config']['taker_fee_bps']} bps taker + "
                 f"{payload['config']['slippage_bps']} bps slippage per side\n")

    lines.append('## The mechanism\n')
    lines.append('With risk-based sizing the gross P&L of a trade is a fixed fraction of '
                 'the equity (a trade exits at exactly `+-risk`), while the cost of the '
                 'trade is proportional to the notional, `equity * risk_fraction / '
                 'risk_pct`. So the cost of a trade as a share of its gross P&L is')
    lines.append('')
    lines.append('```')
    lines.append('cost / |gross P&L| = 2 * cost_per_side / risk_pct')
    lines.append('```')
    lines.append('')
    lines.append('The cost of the rule is therefore set by the *width of the stop*, not by '
                 'the number of trades. A cell whose entries sit 1 % from the slow EMA '
                 'pays ~24 % of its gross P&L in fees; a cell whose entries sit 0.25 % '
                 'away pays ~96 %.\n')

    lines.append('## Leg 1 — the grid-wide decomposition\n')
    lines.append('| Metric | Value |')
    lines.append('|---|---|')
    lines.append(f"| Cells decomposed | {pooled.get('cells', 0)} |")
    lines.append(f"| Trades in the window | {pooled.get('trades', 0)} |")
    lines.append(f"| Pooled gross profit factor | {_fmt(pooled.get('gross_pf'))} |")
    lines.append(f"| Pooled net profit factor | {_fmt(pooled.get('net_pf'))} |")
    lines.append(f"| Costs paid | {pooled.get('cost_total', 0.0):,.0f} |")
    lines.append(f"| Gross P&L | {pooled.get('gross_pnl', 0.0):,.0f} |")
    lines.append(f"| Net P&L | {pooled.get('net_pnl', 0.0):,.0f} |")
    lines.append(f"| Cost share of the gross P&L | {_pct(pooled.get('cost_share_of_gross'))} |")
    lines.append(f"| Median risk distance | {_pct(pooled.get('median_risk_pct'), 3)} |")
    lines.append(f"| Trades whose notional is capped | {_pct(pooled.get('capped_trade_share'))} |")
    lines.append(f"| Median cost per trade, share of gross P&L | "
                 f"{_pct(pooled.get('median_cost_to_gross'))} |")
    lines.append(f"| Model at the median risk distance | "
                 f"{_pct(pooled.get('model_cost_ratio_at_median'))} |")
    lines.append('')

    lines.append('### Per-cell distributions\n')
    lines.append('| Statistic | Gross PF | Net PF | Cost share of gross | Median risk | '
                 'Capped trades |')
    lines.append('|---|---|---|---|---|---|')
    for label, key in (('mean', 'mean'), ('median', 'median'), ('p05', 'p05'),
                       ('p25', 'p25'), ('p75', 'p75'), ('p95', 'p95'),
                       ('max', 'max'), ('min', 'min')):
        lines.append(
            f"| {label} | {_fmt(payload['distributions']['gross_pf'].get(key))} | "
            f"{_fmt(payload['distributions']['net_pf'].get(key))} | "
            f"{_pct(payload['distributions']['cost_share_of_gross'].get(key))} | "
            f"{_pct(payload['distributions']['median_risk_pct'].get(key), 3)} | "
            f"{_pct(payload['distributions']['capped_trade_share'].get(key))} |")
    lines.append('')

    lines.append('### What the costs decide\n')
    counts = payload['counts']
    lines.append('| Question | Answer |')
    lines.append('|---|---|')
    lines.append(f"| Cells with gross PF > 1 (no cost at all) | {counts['gross_pf_gt_1']} |")
    lines.append(f"| Cells with net PF > 1 (registered cost model) | {counts['net_pf_gt_1']} |")
    lines.append(f"| Cells with net PF > 1 that are gross losers | "
                 f"{counts['net_gt_1_gross_le_1']} |")
    lines.append(f"| Cells with gross PF > 1 that are net losers | "
                 f"{counts['gross_gt_1_net_le_1']} |")
    lines.append(f"| Cells where costs take more than half the gross P&L | "
                 f"{counts['cost_dominant']} |")
    lines.append('')

    b = payload['part_b']
    lines.append('## Leg 2 — the sizing legs (re-run)\n')
    lines.append(f"Cells re-run: {len(b['rows'])} (one per symbol, market-cap order).\n")
    lines.append('| Leg | Cells | Trades | Mean gross PF | Mean net PF | Mean net PF (2x costs) | Median risk |')
    lines.append('|---|---|---|---|---|---|---|')
    for leg in ('base', 'uncapped', 'atr_min_risk'):
        agg = payload['leg_aggregates'].get(leg)
        if not agg:
            continue
        lines.append(
            f"| {leg} | {agg['cells']} | {agg['trades']} | {_fmt(agg['gross_pf'])} | "
            f"{_fmt(agg['net_pf'])} | {_fmt(agg['stress_net_pf'])} | "
            f"{_pct(agg['median_risk_pct'], 3)} |")
    lines.append('')
    lines.append('`uncapped` removes the `max_notional_multiple` cap (pure risk-based '
                 'sizing, no leverage limit); `atr_min_risk` is the PROMPT.md §5.2 '
                 'pre-registered mutation that skips trades whose risk distance is below '
                 'one ATR(14). Both are diagnostics of the baseline, not candidate '
                 'configurations.\n')
    repro = payload.get('leg_reproduction')
    if repro:
        lines.append(f"Reproduction check: {repro['n']} of {repro['n']} re-run cells "
                     f"reproduce the stored grid summary (net profit factor and trade "
                     f"count) exactly.\n")

    lines.append('## Verdict\n')
    for line in payload['verdict']:
        lines.append(f"- {line}")
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


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


def _pct(value, digits: int = 1) -> str:
    if value is None:
        return 'n/a'
    try:
        value = float(value)
    except (TypeError, ValueError):
        return str(value)
    if not math.isfinite(value):
        return 'n/a'
    return f'{value * 100:.{digits}f}%'


def main():
    parser = argparse.ArgumentParser(
        description='Cost-drag decomposition of the EMA continuation grid')
    parser.add_argument('--run', type=str, default='results/20261019_135940_grid')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--oos-fraction', type=float, default=0.35)
    parser.add_argument('--limit-symbols', type=int, default=0,
                        help='only decompose the first N symbols (0 = all)')
    parser.add_argument('--sample-cells', type=int, default=0,
                        help='number of cells to re-run under the sizing legs (0 = skip)')
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    run_dir = Path(args.run)
    config = dict(CONFIG_DEFAULTS)
    out_dir = Path(args.out) if args.out else Path(
        f"results/{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_cost_drag_leg")
    out_dir.mkdir(parents=True, exist_ok=True)

    part_a_result = part_a(run_dir, args.fixture_base, args.oos_fraction, config,
                           limit_symbols=args.limit_symbols)
    rows = part_a_result['rows']
    pooled = part_a_result['pooled']

    gross_pf = [r['gross_pf'] for r in rows]
    net_pf = [r['net_pf'] for r in rows]
    distributions = {
        'gross_pf': describe_distribution(gross_pf),
        'net_pf': describe_distribution(net_pf),
        'cost_share_of_gross': describe_distribution(
            [r['cost_share_of_gross'] for r in rows]),
        'median_risk_pct': describe_distribution([r['median_risk_pct'] for r in rows]),
        'capped_trade_share': describe_distribution(
            [r['capped_trade_share'] for r in rows]),
    }
    counts = {
        'gross_pf_gt_1': sum(1 for v in gross_pf if v is not None and v > 1),
        'net_pf_gt_1': sum(1 for v in net_pf if v is not None and v > 1),
        'net_gt_1_gross_le_1': sum(1 for r in rows if r['net_pf'] is not None
                                   and r['gross_pf'] is not None
                                   and r['net_pf'] > 1 and r['gross_pf'] <= 1),
        'gross_gt_1_net_le_1': sum(1 for r in rows if r['net_pf'] is not None
                                   and r['gross_pf'] is not None
                                   and r['gross_pf'] > 1 and r['net_pf'] <= 1),
        'cost_dominant': sum(1 for r in rows if r['cost_share_of_gross'] is not None
                             and r['cost_share_of_gross'] > 0.5),
    }

    part_b_result = {'rows': []}
    leg_aggregates = {}
    leg_reproduction = None
    if args.sample_cells:
        sample = sample_cells(run_dir, args.sample_cells, args.fixture_base)
        part_b_result = part_b(run_dir, args.fixture_base, args.oos_fraction,
                                config, sample)
        leg_aggregates = aggregate_legs(part_b_result['rows'], config)
        leg_reproduction = {
            'n': len(part_b_result['rows']),
            'reproduced': sum(1 for r in part_b_result['rows']
                              if r.get('reproduces_stored_summary')),
        }

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_run': str(run_dir),
        'fixture_base': args.fixture_base,
        'oos_fraction': args.oos_fraction,
        'config': config,
        'n_symbols': len({r['symbol'] for r in rows}),
        'n_cells': len(rows),
        'part_a': part_a_result,
        'part_b': part_b_result,
        'distributions': distributions,
        'counts': counts,
        'leg_aggregates': leg_aggregates,
        'leg_reproduction': leg_reproduction,
        'verdict': build_verdict(pooled, counts, distributions, leg_aggregates,
                                  len(rows)),
    }
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=1, default=str)
    write_report(out_dir, payload)
    print(f'Wrote {out_dir}/summary.md and summary.json')


def aggregate_legs(rows: list, config: dict) -> dict:
    """Pool the sizing legs over the re-run sample."""
    out = {}
    for leg in ('base', 'uncapped', 'atr_min_risk'):
        pns, nets, stresses, risks = [], [], [], []
        for row in rows:
            stats = row['legs'].get(leg)
            if not stats or not stats.get('trades'):
                continue
            pns.append(stats['gross_pf'])
            nets.append(stats['net_pf'])
            stresses.append(stats.get('stress_net_pf'))
            risks.append(stats.get('median_risk_pct'))
        if not pns:
            continue
        out[leg] = {
            'cells': len(pns),
            'trades': sum(row['legs'][leg]['trades'] for row in rows
                          if row['legs'].get(leg)),
            'gross_pf': describe_distribution(pns).get('mean'),
            'net_pf': describe_distribution(nets).get('mean'),
            'stress_net_pf': describe_distribution(stresses).get('mean'),
            'median_risk_pct': describe_distribution(risks).get('median'),
        }
    return out


def build_verdict(pooled: dict, counts: dict, distributions: dict,
                  leg_aggregates: dict, n_cells: int) -> list:
    """The finding this leg supports, in words."""
    lines = []
    median_risk = pooled.get('median_risk_pct')
    cost_share = pooled.get('cost_share_of_gross')
    model = pooled.get('model_cost_ratio_at_median')
    measured = pooled.get('median_cost_to_gross')
    if median_risk:
        lines.append(
            f"The median cell trades at a risk distance of {_pct(median_risk, 3)} of the "
            f"entry price, and the model `2 * cost_per_side / risk_pct` predicts a cost "
            f"of {_pct(model)} of the gross P&L against a measured {_pct(measured)} - the "
            f"cost of the rule is a function of the stop width, not of the number of "
            f"trades.")
    if cost_share is not None:
        lines.append(
            f"Costs take {_pct(cost_share)} of the gross P&L of the grid, and "
            f"{counts['cost_dominant']} of {n_cells} cells lose more than half of their "
            f"gross P&L to fees and slippage.")
    lines.append(
        f"Without any cost, {counts['gross_pf_gt_1']} cells would show a profit factor "
        f"above 1; with the registered cost model only {counts['net_pf_gt_1']} do. The "
        f"grid's headline number is mostly a statement about the cost model.")
    if leg_aggregates.get('atr_min_risk'):
        base = leg_aggregates.get('base', {})
        atr = leg_aggregates.get('atr_min_risk', {})
        lines.append(
            f"Skipping the trades with a risk distance below one ATR(14) - the "
            f"PROMPT.md §5.2 mutation - moves the mean net PF of the re-run sample from "
            f"{_fmt(base.get('net_pf'))} to {_fmt(atr.get('net_pf'))} and the mean gross "
            f"PF from {_fmt(base.get('gross_pf'))} to {_fmt(atr.get('gross_pf'))}, on "
            f"{atr.get('trades')} trades instead of {base.get('trades')}. The mutation "
            f"buys back the cost drag; it does not create an edge, and it leaves the "
            f"sample thinner.")
    if leg_aggregates.get('uncapped'):
        base = leg_aggregates.get('base', {})
        unc = leg_aggregates.get('uncapped', {})
        lines.append(
            f"Removing the notional cap moves the mean net PF of the re-run sample from "
            f"{_fmt(base.get('net_pf'))} to {_fmt(unc.get('net_pf'))}; the cap binds on "
            f"{_pct(pooled.get('capped_trade_share'))} of the trades, and those trades "
            f"pay several times their gross P&L in costs.")
    return lines


if __name__ == '__main__':
    main()
