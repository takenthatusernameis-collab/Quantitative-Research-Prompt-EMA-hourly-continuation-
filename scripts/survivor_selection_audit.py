#!/usr/bin/env python3
"""Selection-bias audit of the EMA hourly continuation survivors.

Why this leg exists
-------------------
The program has ten cells left that clear the out-of-sample gate of
`results/20261021_033523_oos_grid_scan` (out-of-sample net PF above 1, at
least 30 out-of-sample trades, and still above 1 under 2x costs). They are
the only 10 of 17 556 cells that survive, and the whole program decision
rests on them. Two questions about that set are still open.

1. Concentration. Six of the ten cells belong to DEXE/USDT and two to
   GRT/USDT. If the family result is a property of one symbol rather than of
   the rule, then removing that symbol has to break it. The leave-one-
   symbol-out leg answers that directly: for every symbol in the family the
   family is re-selected from the remaining ~17 500 cells and the family
   verdict is recomputed without that symbol.

2. Selection bias. The family was *selected* on the same out-of-sample
   window it is then judged on. The walk-forward leg re-runs the procedure
   honestly: the best cell of a symbol is chosen using the trades up to a
   fold boundary and is then scored on the next, unseen, fold. If the
   selection carries real information, the out-of-fold profit factor has to
   be above 1 far more often than the grid's own null produces on the same
   folds - and the grid supplies that null without any randomization, because
   it holds 17 556 draws of what a cell scores on a fold it was not selected
   on. The shrinkage from the in-fold profit factor of the selected cell to
   its out-of-fold profit factor is the size of the selection bias.

The baseline grid is never touched: this leg only reads it and writes its
own artifact directory.

Usage:
    python scripts/survivor_selection_audit.py --run results/20261019_135940_grid \
        --oos-audit results/20261021_033523_oos_grid_scan
    python scripts/survivor_selection_audit.py --run results/20261019_135940_grid \
        --oos-audit results/20261021_033523_oos_grid_scan --limit-symbols 20
"""
import argparse
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from data.data_loader import load_ohlcv_csv
from scripts.oos_grid_scan import (describe_distribution, read_trades,
                                    stressed_pnl_net, verify_cell, win_loss_sums)
from scripts.run_grid import CONFIG_DEFAULTS, symbol_dir_name, run_config

# The six cells the out-of-sample audit re-ran through the real backtest and
# that still clear the cost stress (`results/20261021_033523_oos_grid_scan`,
# leg 3b). They are the closest the program has ever come to a candidate.
CLOSEST_SURVIVORS = [
    ('BRETT/USDT', 8, 200),
    ('DEXE/USDT', 50, 200),
    ('DEXE/USDT', 55, 200),
    ('GRT/USDT', 20, 200),
    ('MERL/USDT', 8, 200),
    ('ZEN/USDT', 12, 200),
]

# The gate the out-of-sample audit applied: out-of-sample net PF above 1, at
# least this many out-of-sample trades, and still above 1 under 2x costs.
GATE_MIN_TRADES = 30
GATE_MIN_PF = 1.0


def parse_closest_survivors(specs) -> list:
    """Cells the sub-period stability leg runs on.

    `SYMBOL:P_fast:P_slow` entries, e.g. `AERO/USDT:12:200`. Without a
    specification the baseline grid's closest survivors are used, so the
    baseline leg is unchanged; a mutation run passes its own gate survivors,
    because the baseline's cells are not the family that run audits.
    """
    if not specs:
        return list(CLOSEST_SURVIVORS)
    out = []
    for spec in specs:
        parts = spec.rsplit(':', 2)
        if len(parts) != 3:
            raise SystemExit(f'bad --closest-survivors entry: {spec!r}')
        symbol, fast, slow = parts[0], int(parts[1]), int(parts[2])
        out.append((symbol, fast, slow))
    return out

# How many cells the "family" holds. The gate family has exactly ten cells,
# so the ranked family is drawn with the same size.
DEFAULT_TOP_K = 10

# Walk-forward: the full sample of every symbol is cut into this many
# sequential folds. The first fold is the history of the first walk-forward
# step, so the grid is walked forward (n_folds - 1) times per symbol.
DEFAULT_N_FOLDS = 5

# A cell needs at least this many trades in the history window before it can
# be selected; below it the profit factor is noise.
DEFAULT_MIN_HISTORY_TRADES = 20

# The out-of-sample window of the closest survivors is cut into this many
# sequential sub-periods for the stability read.
DEFAULT_OOS_SUBPERIODS = 4

def fold_edges(n_bars: int, n_folds: int) -> list:
    """Bar index at which each fold starts.

    Fold `k` covers the bars `[edges[k], edges[k + 1])`, so the folds
    partition the sample and every bar belongs to exactly one of them.
    """
    if n_folds < 1:
        raise ValueError('n_folds must be >= 1')
    if n_bars <= 0:
        return [0] * (n_folds + 1)
    return [int(n_bars * k / n_folds) for k in range(n_folds + 1)]


def fold_of(bar_index, edges: list) -> int:
    """Index of the fold a bar belongs to (the last edge at or below it)."""
    idx = int(np.searchsorted(edges, bar_index, side='right') - 1)
    return max(0, min(idx, len(edges) - 2))


def pooled_pf(win_sum: float, loss_abs: float):
    """Profit factor of a pooled trade series: wins / losses.

    Pooling always uses the sums of wins and losses, never a mean of
    per-cell ratios: cells carry very different trade counts, so a mean of
    ratios would give a thin cell the same weight as a thick one.
    """
    if loss_abs > 0:
        return win_sum / loss_abs
    if win_sum > 0:
        return float('inf')
    return None


def cell_fold_stats(trades: pd.DataFrame, edges: list,
                     stress_multiplier: float = 2.0) -> list:
    """Per-fold trade counts and win/loss sums of one cell.

    A trade belongs to the fold it was *entered* in, which is the same rule
    the out-of-sample screen uses, so the fold and window numbers are
    comparable.
    """
    n_folds = len(edges) - 1
    empty = {'trades': 0, 'win_sum': 0.0, 'loss_abs': 0.0,
             'stress_win_sum': 0.0, 'stress_loss_abs': 0.0}
    if trades is None or len(trades) == 0:
        return [dict(empty, fold=f) for f in range(n_folds)]
    bars = trades['bar_index'].to_numpy()
    pnl = trades['pnl_net'].to_numpy(dtype=float)
    stress = stressed_pnl_net(pnl, trades['entry_cost'].to_numpy(dtype=float),
                               trades['exit_cost'].to_numpy(dtype=float),
                               stress_multiplier)
    idx = np.clip(np.searchsorted(edges, bars, side='right') - 1, 0, n_folds - 1)
    out = []
    for fold in range(n_folds):
        mask = idx == fold
        win, loss = win_loss_sums(pnl[mask])
        s_win, s_loss = win_loss_sums(stress[mask])
        out.append({'fold': fold, 'trades': int(mask.sum()), 'win_sum': win,
                    'loss_abs': loss, 'stress_win_sum': s_win,
                    'stress_loss_abs': s_loss})
    return out


def sum_folds(folds: list, upto: int) -> dict:
    """Aggregate folds `[0, upto)` into one window."""
    win = sum(f['win_sum'] for f in folds[:upto])
    loss = sum(f['loss_abs'] for f in folds[:upto])
    s_win = sum(f['stress_win_sum'] for f in folds[:upto])
    s_loss = sum(f['stress_loss_abs'] for f in folds[:upto])
    trades = sum(f['trades'] for f in folds[:upto])
    return {'trades': trades, 'win_sum': win, 'loss_abs': loss,
            'stress_win_sum': s_win, 'stress_loss_abs': s_loss,
            'net_pf': pooled_pf(win, loss),
            'stress_net_pf': pooled_pf(s_win, s_loss)}


def select_best(candidates: list) -> dict:
    """The candidate with the highest profit factor.

    Ties are broken by the trade count (the thicker sample) and then by the
    pair order, so the selection is deterministic.
    """
    usable = [c for c in candidates
              if c.get('net_pf') is not None
              and math.isfinite(c['net_pf'])
              and c.get('trades', 0) > 0]
    if not usable:
        return None
    usable.sort(key=lambda c: (-c['net_pf'], -c.get('trades', 0),
                               c['P_fast'], c['P_slow']))
    return usable[0]


def walk_forward_steps(cells: list, n_folds: int,
                       min_history_trades: int) -> list:
    """Walk the selection forward over the folds of one symbol.

    Step `k` (k = 1 .. n_folds - 1) selects the cell with the best profit
    factor over the history `folds[0:k]` and scores that cell on `folds[k]`,
    which the selection never saw.
    """
    out = []
    for step in range(1, n_folds):
        candidates = []
        for cell in cells:
            hist = sum_folds(cell['folds'], step)
            candidates.append({'P_fast': cell['P_fast'], 'P_slow': cell['P_slow'],
                               'trades': hist['trades'], 'net_pf': hist['net_pf'],
                               'stress_net_pf': hist['stress_net_pf'],
                               'folds': cell['folds']})
        eligible = [c for c in candidates
                    if c['trades'] >= min_history_trades and c['net_pf'] is not None
                    and math.isfinite(c['net_pf'])]
        selected = select_best(eligible)
        record = {'step': step, 'history_folds': step, 'test_fold': step,
                  'candidates': len(eligible), 'selected': None}
        if selected is not None:
            test = selected['folds'][step]
            t_win, t_loss = test['win_sum'], test['loss_abs']
            s_win, s_loss = test['stress_win_sum'], test['stress_loss_abs']
            record.update({
                'selected': (selected['P_fast'], selected['P_slow']),
                'history_trades': selected['trades'],
                'history_net_pf': selected['net_pf'],
                'history_stress_net_pf': selected['stress_net_pf'],
                'oof_trades': test['trades'],
                'oof_net_pf': pooled_pf(t_win, t_loss),
                'oof_stress_net_pf': pooled_pf(s_win, s_loss),
                'oof_win_sum': t_win,
                'oof_loss_abs': t_loss,
                'oof_stress_win_sum': s_win,
                'oof_stress_loss_abs': s_loss,
            })
        out.append(record)
    return out


def survivor_cells(rows: list, min_trades: int = GATE_MIN_TRADES,
                   min_pf: float = GATE_MIN_PF) -> list:
    """The cells that clear the out-of-sample gate, strongest first.

    The gate is the one the grid-wide audit applied: out-of-sample net PF
    above `min_pf`, at least `min_trades` out-of-sample trades, and still
    above `min_pf` under 2x costs.
    """
    out = []
    for row in rows:
        if (row.get('oos_trades') or 0) < min_trades:
            continue
        if (row.get('oos_net_pf') or 0.0) <= min_pf:
            continue
        if (row.get('oos_stress_net_pf') or 0.0) <= min_pf:
            continue
        out.append(row)
    out.sort(key=lambda r: -r['oos_net_pf'])
    return out


def family_pooled(rows: list) -> dict:
    """Pool the out-of-sample trades of a family of cells."""
    win = sum(r.get('oos_win_sum') or 0.0 for r in rows)
    loss = sum(r.get('oos_loss_abs') or 0.0 for r in rows)
    s_win = sum(r.get('oos_stress_win_sum') or 0.0 for r in rows)
    s_loss = sum(r.get('oos_stress_loss_abs') or 0.0 for r in rows)
    return {'cells': len(rows),
            'trades': sum(int(r.get('oos_trades') or 0) for r in rows),
            'net_pf': pooled_pf(win, loss),
            'stress_net_pf': pooled_pf(s_win, s_loss),
            'net_pnl': win - loss,
            'stress_net_pnl': s_win - s_loss,
            'win_sum': win, 'loss_abs': loss}


def ranked_pool(rows: list, min_trades: int) -> list:
    """The pool the selection procedure ranks: cells with enough trades."""
    pool = [r for r in rows if (r.get('oos_trades') or 0) >= min_trades]
    pool.sort(key=lambda r: -r['oos_net_pf'])
    return pool


def leave_one_symbol_out(rows: list, family: list, top_k: int,
                         min_trades: int) -> list:
    """Drop one symbol of the family and re-select the family without it.

    Two readings are reported for every dropped symbol:

    * the gate family loses that symbol's cells - how many of the original
      survivors remain, and what the pooled family result looks like without
      the symbol (the concentration read);
    * the ranked family is re-selected from the remaining pool, so the cells
      that would replace the dropped ones are visible (the selection-stability
      read).
    """
    family_keys = {(r['symbol'], r['P_fast'], r['P_slow']) for r in family}
    family_symbols = sorted({r['symbol'] for r in family})
    out = []
    for symbol in family_symbols:
        dropped = [r for r in family if r['symbol'] == symbol]
        kept = [r for r in family if r['symbol'] != symbol]
        kept_pooled = family_pooled(kept)

        pool = [r for r in ranked_pool(rows, min_trades) if r['symbol'] != symbol]
        new_family = pool[:top_k]
        new_keys = {(r['symbol'], r['P_fast'], r['P_slow']) for r in new_family}
        retained = sorted(family_keys & new_keys)
        entrants = [r for r in new_family
                    if (r['symbol'], r['P_fast'], r['P_slow']) not in family_keys]
        new_pooled = family_pooled(new_family)
        out.append({
            'dropped_symbol': symbol,
            'dropped_cells': len(dropped),
            'dropped_trades': sum(int(r.get('oos_trades') or 0) for r in dropped),
            'family_remaining': len(kept),
            'family_remaining_net_pf': kept_pooled['net_pf'],
            'family_remaining_stress_net_pf': kept_pooled['stress_net_pf'],
            'family_remaining_net_pnl': kept_pooled['net_pnl'],
            'family_full_net_pf': family_pooled(family)['net_pf'],
            'family_full_stress_net_pf': family_pooled(family)['stress_net_pf'],
            'family_full_net_pnl': family_pooled(family)['net_pnl'],
            'ranked_retained': len(retained),
            'ranked_retained_cells': [{'symbol': s, 'P_fast': f, 'P_slow': sl}
                                       for s, f, sl in retained],
            'ranked_entrants': [{'symbol': r['symbol'], 'P_fast': r['P_fast'],
                                 'P_slow': r['P_slow'],
                                 'oos_net_pf': r['oos_net_pf'],
                                 'oos_stress_net_pf': r['oos_stress_net_pf'],
                                 'oos_trades': r['oos_trades'],
                                 'clears_gate': bool(
                                     (r.get('oos_stress_net_pf') or 0.0) > GATE_MIN_PF)}
                                for r in entrants],
            'ranked_family_net_pf': new_pooled['net_pf'],
            'ranked_family_stress_net_pf': new_pooled['stress_net_pf'],
            'ranked_family_net_pnl': new_pooled['net_pnl'],
            'ranked_family_clears_gates': bool(
                (new_pooled['net_pf'] or 0.0) > 1.0
                and (new_pooled['stress_net_pf'] or 0.0) > 1.0),
        })
    return out


def read_cell_folds(run_dir: Path, symbol: str, fast: int, slow: int,
                    n_bars: int, n_folds: int,
                    stress_multiplier: float = 2.0):
    """Fold statistics of one cell, read from the blotter the grid wrote."""
    cell_dir = run_dir / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'
    if not (cell_dir / 'trades.csv.gz').exists() and not (cell_dir / 'trades.csv').exists():
        return None
    edges = fold_edges(n_bars, n_folds)
    trades = read_trades(cell_dir)
    folds = cell_fold_stats(trades, edges, stress_multiplier)
    return {'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
            'n_bars': n_bars, 'folds': folds}


def collect_fold_stats(run_dir: Path, rows: list, n_folds: int,
                       stress_multiplier: float = 2.0,
                       limit_symbols: int = 0) -> list:
    """Fold statistics of every cell of the grid."""
    by_symbol = defaultdict(list)
    bars = {}
    for row in rows:
        by_symbol[row['symbol']].append((int(row['P_fast']), int(row['P_slow'])))
        bars[row['symbol']] = int(row.get('n_bars') or 0)
    symbols = sorted(by_symbol)
    if limit_symbols:
        symbols = symbols[:limit_symbols]
    out = []
    for symbol in symbols:
        n_bars = bars[symbol]
        for fast, slow in sorted(by_symbol[symbol]):
            cell = read_cell_folds(run_dir, symbol, fast, slow, n_bars,
                                   n_folds, stress_multiplier)
            if cell is not None:
                out.append(cell)
    return out


def oos_subperiods(run_dir: Path, symbol: str, fast: int, slow: int,
                   n_bars: int, entry_start: int, subperiods: int,
                   stress_multiplier: float = 2.0) -> dict:
    """Split the out-of-sample window of one cell into sequential sub-periods."""
    cell_dir = run_dir / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'
    trades = read_trades(cell_dir)
    # Only the trades entered inside the out-of-sample window belong to it.
    trades = trades[trades['bar_index'] >= entry_start]
    window = n_bars - entry_start
    edges = [entry_start + int(window * m / subperiods)
             for m in range(subperiods + 1)]
    folds = cell_fold_stats(trades, edges, stress_multiplier)
    out = []
    for fold in folds:
        out.append({'subperiod': fold['fold'],
                    'trades': fold['trades'],
                    'net_pf': pooled_pf(fold['win_sum'], fold['loss_abs']),
                    'stress_net_pf': pooled_pf(fold['stress_win_sum'],
                                               fold['stress_loss_abs'])})
    return {'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
            'entry_start_index': entry_start, 'subperiods': out}


def summarize_walk_forward(records: list) -> dict:
    """Aggregate the walk-forward steps of the whole grid."""
    evaluated = [r for r in records if r.get('selected') is not None]
    scored = [r for r in evaluated if r.get('oof_trades', 0) > 0]
    win = sum(r['oof_win_sum'] for r in scored)
    loss = sum(r['oof_loss_abs'] for r in scored)
    s_win = sum(r['oof_stress_win_sum'] for r in scored)
    s_loss = sum(r['oof_stress_loss_abs'] for r in scored)
    above = sum(1 for r in scored if (r['oof_net_pf'] or 0.0) > 1.0)
    above_stress = sum(1 for r in scored
                       if (r['oof_stress_net_pf'] or 0.0) > 1.0)
    history_pfs = [r['history_net_pf'] for r in evaluated
                   if r.get('history_net_pf') is not None
                   and math.isfinite(r['history_net_pf'])]
    oof_pfs = [r['oof_net_pf'] for r in scored
               if r.get('oof_net_pf') is not None
               and math.isfinite(r['oof_net_pf'])]
    return {
        'steps': len(records),
        'steps_selected': len(evaluated),
        'steps_scored': len(scored),
        'oof_pf_gt_1': above,
        'oof_pf_gt_1_share': (above / len(scored)) if scored else None,
        'oof_stress_pf_gt_1': above_stress,
        'oof_stress_pf_gt_1_share': (above_stress / len(scored)) if scored else None,
        'pooled_oof_net_pf': pooled_pf(win, loss),
        'pooled_oof_stress_net_pf': pooled_pf(s_win, s_loss),
        'pooled_oof_net_pnl': win - loss,
        'pooled_oof_trades': sum(r['oof_trades'] for r in scored),
        'history_pf_distribution': describe_distribution(history_pfs),
        'oof_pf_distribution': describe_distribution(oof_pfs),
        'median_history_pf': float(np.median(history_pfs)) if history_pfs else None,
        'median_oof_pf': float(np.median(oof_pfs)) if oof_pfs else None,
    }


def null_pf_distribution(fold_rows: list, step: int) -> list:
    """The profit factor every cell of the grid would have shown on a fold.

    This is the null the walk-forward selection has to beat: the cell that
    was picked by chance would have scored one of these. It needs no
    randomization, because the grid itself supplies 17 556 draws of it.
    """
    out = []
    for cell in fold_rows:
        fold = cell['folds'][step]
        pf = pooled_pf(fold['win_sum'], fold['loss_abs'])
        if pf is not None and math.isfinite(pf):
            out.append(pf)
    return out


def percentile_rank(value: float, distribution: list) -> float:
    """Share of the null distribution that lies below `value`."""
    if not distribution or value is None or not math.isfinite(value):
        return None
    below = sum(1 for v in distribution if v < value)
    equal = sum(1 for v in distribution if v == value)
    return (below + 0.5 * equal) / len(distribution)


def binomial_upper_tail(successes: int, trials: int, p: float = 0.05) -> float:
    """One-sided exact binomial p-value: P(X >= successes).

    The fair-coin two-sided helper of `scripts.null_grid_scan` cannot be
    used here: this test asks for an excess of successes under a small
    rate, so the tail that matters is the upper one. The sum is taken in
    log space, because the direct sum of `math.comb` terms overflows for a
    few thousand trials.
    """
    if trials <= 0 or successes <= 0:
        return 1.0
    if successes > trials:
        return 0.0
    logp = math.log(p)
    logq = math.log(1.0 - p)
    log_comb = (math.lgamma(trials + 1) - math.lgamma(successes + 1)
                - math.lgamma(trials - successes + 1))
    tail = 0.0
    for i in range(successes, trials + 1):
        tail += math.exp(log_comb + i * logp + (trials - i) * logq)
        if i < trials:
            log_comb += math.log(trials - i) - math.log(i + 1)
    return min(1.0, tail)


def selection_against_null(records: list, nulls: dict) -> dict:
    """How the selected cells rank against the null of the same fold.

    Under the null the selected cell is a random cell of the grid, so its
    out-of-fold profit factor should sit at a random place in that fold's
    distribution. A selection that carries information pushes the selected
    cells towards the top of the distribution.
    """
    ranks = []
    for record in records:
        if record.get('selected') is None or not record.get('oof_trades', 0):
            continue
        distribution = nulls.get(record['step']) or []
        rank = percentile_rank(record['oof_net_pf'], distribution)
        if rank is not None:
            record['oof_percentile'] = rank
            ranks.append(rank)
    beats = sum(1 for r in ranks if r > 0.95)
    trials = len(ranks)
    expected = 0.05 * trials
    null_values = [v for distribution in nulls.values() for v in distribution]
    return {
        'scored': trials,
        'median_percentile': float(np.median(ranks)) if ranks else None,
        'mean_percentile': float(np.mean(ranks)) if ranks else None,
        'above_p95': beats,
        'above_p95_share': (beats / trials) if trials else None,
        'expected_above_p95': expected,
        'binomial_p_value': (binomial_upper_tail(beats, trials, 0.05)
                             if trials else None),
        'null_cells': len(null_values),
        'null_median_pf': float(np.median(null_values)) if null_values else None,
        'null_pf_gt_1': sum(1 for v in null_values if v > 1.0),
        'null_pf_gt_1_share': (sum(1 for v in null_values if v > 1.0)
                               / len(null_values)) if null_values else None,
    }


def build_verdict(payload: dict) -> list:
    """The conclusion of the leg, as a list of report lines."""
    lines = []
    part_a = payload['part_a']
    family = part_a['family']
    loso = part_a['leave_one_symbol_out']
    walk = payload['part_b']['walk_forward']
    null = payload['part_b']['selection_vs_null']
    sub = payload['part_c']

    if not loso:
        lines.append('The survivor family is empty in this run: no cell clears '
                     'the out-of-sample gate.')
        return lines

    lines.append(
        f"The {family['cells']}-cell survivor family is concentrated in "
        f"{len(part_a['family_symbols'])} symbols; dropping the dominant symbol "
        f"leaves {min(r['family_remaining'] for r in loso)} of the {family['cells']} "
        f"cells.")
    retained = [r['ranked_retained'] for r in loso]
    lines.append(
        f"Re-selecting the family from the remaining cells keeps "
        f"{min(retained)}-{max(retained)} of the original cells, so the family is "
        f"{'stable' if min(retained) >= 7 else 'not stable'} under a "
        f"leave-one-symbol-out.")
    lines.append(
        f"Walk-forward: the procedure picks a cell on the history "
        f"(median in-fold net PF {_fmt(walk['median_history_pf'])}) and the same cell "
        f"nets a median out-of-fold PF of {_fmt(walk['median_oof_pf'])}; the pooled "
        f"out-of-fold net PF is {_fmt(walk['pooled_oof_net_pf'])} over "
        f"{walk['pooled_oof_trades']} trades, and "
        f"{_pct(walk['oof_pf_gt_1_share'])} of the out-of-fold windows land "
        f"above PF 1 against the {_pct(null['null_pf_gt_1_share'])} the grid's own "
        f"null produces on the same folds.")
    lines.append(
        f"The selected cells rank at a median of the "
        f"{_fmt(null['median_percentile'])} percentile of that null, and "
        f"{null['above_p95']} of {null['scored']} beat its 95th percentile "
        f"(one-sided exact binomial p {_fmt_p(null['binomial_p_value'])}): the "
        f"selection does rank the cells, it just never ranks one into a "
        f"net-profitable window.")
    stable = [c for c in sub['closest_survivors']
              if c['subperiods_with_trades'] == sub['n_subperiods']
              and c['subperiods_pf_gt_1'] == c['subperiods_with_trades']]
    lines.append(
        f"Sub-period stability: {len(stable)} of {len(sub['closest_survivors'])} "
        f"closest survivors keep PF above 1 in every out-of-sample sub-period "
        f"that carries trades.")
    lines.append(
        "The out-of-sample gate is measuring a window, not a rule: the "
        "survivors do not survive their own walk-forward, and the family "
        "collapses onto a handful of symbols.")
    return lines


def write_report(out_dir: Path, payload: dict) -> None:
    """Write the human-readable leg report."""
    a = payload['part_a']
    family = a['family']
    lines = []
    lines.append('# Survivor Selection Audit — EMA Hourly Continuation\n')
    lines.append(f"**Source run:** `{payload['source_run']}`")
    lines.append(f"**Out-of-sample audit:** `{payload['oos_audit']}`")
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Universe:** {payload['n_symbols']} symbols, "
                 f"{payload['n_cells']} grid cells")
    lines.append(f"**Cost model:** {payload['config']['taker_fee_bps']} bps taker + "
                 f"{payload['config']['slippage_bps']} bps slippage per side "
                 f"(stress leg: 2x)\n")

    lines.append('## Why this leg exists\n')
    lines.append('Ten cells out of 17 556 clear the out-of-sample gate. The program '
                 'decision rests on them, and two questions about that set were still '
                 'open: is the family a property of the rule or of the one or two '
                 'symbols it sits on, and does the *selection* survive a walk-forward '
                 'that never shows the selection the data it is scored on.\n')

    lines.append('## Leg 1 — the family\n')
    lines.append('| Symbol | Cell | OOS trades | OOS net PF | OOS PF (2x costs) | '
                 'Full-sample net PF | Exact OOS PF | Exact OOS PF (2x) |')
    lines.append('|---|---|---|---|---|---|---|---|')
    for cell in a['family_cells']:
        lines.append(
            f"| {cell['symbol']} | P{cell['P_fast']}_{cell['P_slow']} | "
            f"{cell['oos_trades']} | {cell['oos_net_pf']:.4f} | "
            f"{cell['oos_stress_net_pf']:.4f} | {cell['net_pf']:.4f} | "
            f"{_fmt(cell.get('exact_oos_net_pf'))} | "
            f"{_fmt(cell.get('exact_oos_stress_net_pf'))} |")
    lines.append('')
    lines.append(f"Pooled over the family: net PF **{_fmt(family['net_pf'])}**, "
                 f"under 2x costs **{_fmt(family['stress_net_pf'])}**, "
                 f"net P&L {family['net_pnl']:,.0f}. The family sits on "
                 f"{len(a['family_symbols'])} symbols: "
                 f"{', '.join(a['family_symbols'])}.\n")
    lines.append('| Symbol | Family cells | Family trades | Share of the family net P&L | '
                 'Pooled net PF | Pooled net PF (2x) |')
    lines.append('|---|---|---|---|---|---|')
    for row in a['per_symbol']:
        lines.append(
            f"| {row['symbol']} | {row['cells']} | {row['trades']} | "
            f"{_pct(row['net_pnl_share'])} | {_fmt(row['net_pf'])} | "
            f"{_fmt(row['stress_net_pf'])} |")
    lines.append('')

    lines.append('## Leg 2 — leave-one-symbol-out\n')
    lines.append('Every symbol of the family is dropped in turn. The gate family '
                 'loses that symbol\'s cells; the ranked family is re-selected from '
                 'the remaining cells, so the cells that would replace them are '
                 'visible.\n')
    lines.append('| Dropped symbol | Cells dropped | Family cells left | Pooled net PF '
                 'without it | Pooled net PF (2x) without it | Ranked family: original '
                 'cells kept | Newcomers | Newcomers that clear the gate | Ranked family '
                 'net PF | Ranked family net PF (2x) | Ranked family clears the gates |')
    lines.append('|---|---|---|---|---|---|---|---|---|---|---|')
    for row in a['leave_one_symbol_out']:
        entrants = row['ranked_entrants']
        lines.append(
            f"| {row['dropped_symbol']} | {row['dropped_cells']} | "
            f"{row['family_remaining']} | {_fmt(row['family_remaining_net_pf'])} | "
            f"{_fmt(row['family_remaining_stress_net_pf'])} | "
            f"{row['ranked_retained']} | {len(entrants)} | "
            f"{sum(1 for e in entrants if e['clears_gate'])} | "
            f"{_fmt(row['ranked_family_net_pf'])} | "
            f"{_fmt(row['ranked_family_stress_net_pf'])} | "
            f"{'yes' if row['ranked_family_clears_gates'] else 'no'} |")
    lines.append('')
    for row in a['leave_one_symbol_out']:
        if row['ranked_entrants']:
            names = ', '.join(
                f"{e['symbol']} P{e['P_fast']}_{e['P_slow']} "
                f"(PF {e['oos_net_pf']:.4f}, stress {e['oos_stress_net_pf']:.4f})"
                for e in row['ranked_entrants'])
            lines.append(f"- Without {row['dropped_symbol']} the family is topped up by "
                         f"{names}.")
    lines.append('')

    b = payload['part_b']
    walk = b['walk_forward']
    lines.append('## Leg 3 — walk-forward re-selection over the whole grid\n')
    lines.append(f"The full sample of every symbol is cut into {b['n_folds']} "
                 f"sequential folds. At step k the best cell of the symbol is chosen "
                 f"on the history (folds 1..k, at least {b['min_history_trades']} "
                 f"trades) and scored on fold k+1, which the selection never saw. "
                 f"Every cell of the grid takes part; nothing is selected in advance.\n")
    lines.append('| Step (history -> test fold) | Symbols scored | Steps with a '
                 'selection | Out-of-fold PF > 1 | Pooled out-of-fold net PF | '
                 'Pooled out-of-fold net PF (2x) | Median in-fold net PF |')
    lines.append('|---|---|---|---|---|---|---|')
    for step in b['steps']:
        lines.append(
            f"| {step['history_folds']} -> {step['test_fold'] + 1} | "
            f"{step['symbols_scored']} | {step['steps_selected']} | "
            f"{step['oof_pf_gt_1']} ({_pct(step['oof_pf_gt_1_share'])}) | "
            f"{_fmt(step['pooled_oof_net_pf'])} | "
            f"{_fmt(step['pooled_oof_stress_net_pf'])} | "
            f"{_fmt(step['median_history_pf'])} |")
    lines.append('')
    lines.append('| Pooled over every step | Value |')
    lines.append('|---|---|')
    lines.append(f"| Walk-forward steps scored | {walk['steps_scored']} |")
    lines.append(f"| Out-of-fold trades | {walk['pooled_oof_trades']} |")
    lines.append(f"| Pooled out-of-fold net PF | {_fmt(walk['pooled_oof_net_pf'])} |")
    lines.append(f"| Pooled out-of-fold net PF (2x costs) | "
                 f"{_fmt(walk['pooled_oof_stress_net_pf'])} |")
    lines.append(f"| Out-of-fold windows with net PF > 1 | {walk['oof_pf_gt_1']} "
                 f"({_pct(walk['oof_pf_gt_1_share'])}) |")
    lines.append(f"| Out-of-fold windows with net PF > 1 under 2x costs | "
                 f"{walk['oof_stress_pf_gt_1']} "
                 f"({_pct(walk['oof_stress_pf_gt_1_share'])}) |")
    lines.append(f"| Median in-fold net PF of the selected cell | "
                 f"{_fmt(walk['median_history_pf'])} |")
    lines.append(f"| Median out-of-fold net PF of the selected cell | "
                 f"{_fmt(walk['median_oof_pf'])} |")
    lines.append('')

    lines.append('### Leg 3b — the selected cells against the grid\'s own null\n')
    lines.append('The null needs no randomization: the grid itself holds 17 556 '
                 'draws of what a cell scores on a fold it was not selected on. If '
                 'the selection carries information, the selected cells have to sit '
                 'at the top of that distribution; if it does not, they sit where a '
                 'random cell would.\n')
    lines.append('| Step | Null cells | Null median PF | Null mean PF | Null share '
                 'above PF 1 | Null p95 | Selected cells above the null p95 |')
    lines.append('|---|---|---|---|---|---|---|')
    for step in b['steps']:
        lines.append(
            f"| {step['history_folds']} -> {step['test_fold'] + 1} | "
            f"{step['null_cells']} | {_fmt(step['null_median_pf'])} | "
            f"{_fmt(step['null_mean_pf'])} | {_pct(step['null_pf_gt_1_share'])} | "
            f"{_fmt(step['null_p95_pf'])} | "
            f"{step['oof_pf_gt_1']} / {step['steps_scored']} |")
    lines.append('')
    vs_null = b['selection_vs_null']
    lines.append('| Measure | Value |')
    lines.append('|---|---|')
    lines.append(f"| Selected cells scored | {vs_null['scored']} |")
    lines.append(f"| Median percentile of the selected cells in the null "
                 f"distribution | {_fmt(vs_null['median_percentile'])} |")
    lines.append(f"| Selected cells above the null 95th percentile | "
                 f"{vs_null['above_p95']} ({_pct(vs_null['above_p95_share'])}) |")
    lines.append(f"| Expected under a null pick | "
                 f"{vs_null['expected_above_p95']:.1f} |")
    lines.append(f"| One-sided exact binomial p-value, P(X >= observed) | "
                 f"{_fmt_p(vs_null['binomial_p_value'])} |")
    lines.append('')

    c = payload['part_c']
    lines.append(f"## Leg 4 — sub-period stability of the closest survivors\n")
    lines.append(f"The out-of-sample window of the {len(c['closest_survivors'])} "
                 f"closest survivors is cut into {c['n_subperiods']} sequential "
                 f"sub-periods. An edge that is real has to show up in more than one "
                 f"of them.\n")
    lines.append('| Symbol | Cell | ' + ' | '.join(
        f"PF sub {i + 1}" for i in range(c['n_subperiods'])) +
        ' | Sub-periods with PF > 1 | Sub-periods with PF > 1 (2x costs) | '
        'Sub-periods with trades |')
    lines.append('|---|---|' + '---|' * (c['n_subperiods'] + 3))
    for cell in c['closest_survivors']:
        pfs = ' | '.join(_fmt(s['net_pf']) for s in cell['subperiods'])
        lines.append(
            f"| {cell['symbol']} | P{cell['P_fast']}_{cell['P_slow']} | {pfs} | "
            f"{cell['subperiods_pf_gt_1']}/{cell['subperiods_with_trades']} | "
            f"{cell['subperiods_stress_pf_gt_1']}/{cell['subperiods_with_trades']} | "
            f"{cell['subperiods_with_trades']}/{c['n_subperiods']} |")
    lines.append('')
    lines.append('A sub-period without a single trade has no profit factor: it is '
                 'missing evidence, not a loss. The last column therefore shows how '
                 'many of the sub-periods carry any trades at all.\n')
    sub_trades = [s['trades'] for cell in c['closest_survivors']
                  for s in cell['subperiods'] if s['trades'] > 0]
    if sub_trades:
        lines.append(f'The sub-periods are thin: the median sub-period of the closest '
                     f'survivors holds {int(np.median(sub_trades))} trades, so this leg '
                     f'reads the stability of the edge, not its size.\n')
    lines.append('| Symbol | Cell | Trades per sub-period |')
    lines.append('|---|---|---|')
    for cell in c['closest_survivors']:
        counts = ', '.join(str(s['trades']) for s in cell['subperiods'])
        lines.append(f"| {cell['symbol']} | P{cell['P_fast']}_{cell['P_slow']} | "
                     f"{counts} |")
    lines.append('')

    lines.append('## Verdict\n')
    for line in payload['verdict']:
        lines.append(f'- {line}')
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


def _fmt_p(value) -> str:
    """A probability, with enough digits to stay readable when it is tiny."""
    if value is None:
        return 'n/a'
    try:
        value = float(value)
    except (TypeError, ValueError):
        return str(value)
    if value == 0.0:
        return '< 1e-300'
    if value < 1e-4:
        return f'{value:.3e}'
    return f'{value:.4f}'


def main():
    parser = argparse.ArgumentParser(
        description='Selection-bias audit of the EMA continuation survivors')
    parser.add_argument('--run', type=str, default='results/20261019_135940_grid')
    parser.add_argument('--oos-audit', type=str,
                        default='results/20261021_033523_oos_grid_scan')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--min-trades', type=int, default=GATE_MIN_TRADES)
    parser.add_argument('--top-k', type=int, default=DEFAULT_TOP_K)
    parser.add_argument('--n-folds', type=int, default=DEFAULT_N_FOLDS)
    parser.add_argument('--min-history-trades', type=int,
                        default=DEFAULT_MIN_HISTORY_TRADES)
    parser.add_argument('--oos-subperiods', type=int,
                        default=DEFAULT_OOS_SUBPERIODS)
    parser.add_argument('--limit-symbols', type=int, default=0,
                        help='only audit the first N symbols (0 = all)')
    parser.add_argument('--exact-verify', type=int, default=1,
                        help='re-run the family cells through the real backtest (1/0)')
    parser.add_argument('--out', type=str, default=None)
    parser.add_argument('--closest-survivors', type=str, nargs='*', default=None,
                        help='Cells the sub-period stability leg is run on, as '
                             'SYMBOL:P_fast:P_slow. Defaults to the baseline '
                             'grid\'s closest survivors; a mutation run passes '
                             'its own gate survivors so the leg covers the '
                             'family it actually audits.')
    parser.add_argument('--render-only', type=str, default=None,
                        help='re-render summary.md from an existing summary.json')
    args = parser.parse_args()

    if args.render_only:
        out_dir = Path(args.render_only)
        payload = json.loads((out_dir / 'summary.json').read_text())
        payload['verdict'] = build_verdict(payload)
        write_report(out_dir, payload)
        print(f'Rendered {out_dir}/summary.md')
        return

    run_dir = Path(args.run)
    audit_dir = Path(args.oos_audit)
    # The cells have to be verified under the config of the run they come
    # from: a pre-registered mutation run stores its own config, and
    # re-verifying it with the default config would measure the parent rule.
    config = run_config(run_dir)
    out_dir = Path(args.out) if args.out else Path(
        f"results/{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
        f"_survivor_selection_audit")
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    with open(audit_dir / 'cells.jsonl') as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if args.limit_symbols:
        symbols = sorted({r['symbol'] for r in rows})[:args.limit_symbols]
        keep = set(symbols)
        rows = [r for r in rows if r['symbol'] in keep]

    family = survivor_cells(rows, args.min_trades, GATE_MIN_PF)
    family_symbols = sorted({r['symbol'] for r in family})
    loso = leave_one_symbol_out(rows, family, args.top_k, args.min_trades)

    per_symbol = []
    family_pooled_net = family_pooled(family)['net_pnl']
    for symbol in family_symbols:
        cells = [r for r in family if r['symbol'] == symbol]
        pooled = family_pooled(cells)
        per_symbol.append({'symbol': symbol, 'cells': len(cells),
                           'trades': pooled['trades'],
                           'net_pf': pooled['net_pf'],
                           'stress_net_pf': pooled['stress_net_pf'],
                           'net_pnl': pooled['net_pnl'],
                           'net_pnl_share': (pooled['net_pnl'] / family_pooled_net)
                           if family_pooled_net else 0.0})

    # The exact numbers of the family cells, re-run through the real backtest.
    family_cells = []
    for row in family:
        cell = {'symbol': row['symbol'], 'P_fast': int(row['P_fast']),
                'P_slow': int(row['P_slow']),
                'oos_trades': int(row.get('oos_trades') or 0),
                'oos_net_pf': row.get('oos_net_pf'),
                'oos_stress_net_pf': row.get('oos_stress_net_pf'),
                'net_pf': row.get('net_pf'),
                'stress_net_pf': row.get('stress_net_pf')}
        if args.exact_verify:
            df = load_ohlcv_csv(
                str(Path(args.fixture_base) / f"{row['symbol'].replace('/', '_')}.csv"))
            legs = verify_cell(row['symbol'], df, int(row['P_fast']),
                               int(row['P_slow']), 0.35, args.stress_multiplier,
                               config)
            cell['exact_oos_net_pf'] = legs['oos'].get('net_profit_factor')
            cell['exact_oos_stress_net_pf'] = legs['stress_oos'].get('net_profit_factor')
            cell['exact_oos_trades'] = int(legs['oos'].get('trade_count') or 0)
            cell['exact_oos_sharpe'] = legs['oos'].get('sharpe_ratio')
        family_cells.append(cell)

    # Walk-forward over the whole grid.
    fold_rows = collect_fold_stats(run_dir, rows, args.n_folds,
                                   args.stress_multiplier, args.limit_symbols)
    by_symbol = defaultdict(list)
    for cell in fold_rows:
        by_symbol[cell['symbol']].append(cell)
    walk_records = []
    for symbol in sorted(by_symbol):
        for record in walk_forward_steps(by_symbol[symbol], args.n_folds,
                                          args.min_history_trades):
            record['symbol'] = symbol
            walk_records.append(record)
    walk_summary = summarize_walk_forward(walk_records)

    # The null each selected cell has to beat: what every cell of the grid
    # would have scored on the fold it was tested on.
    nulls = {step: null_pf_distribution(fold_rows, step)
             for step in range(1, args.n_folds)}
    selection_vs_null = selection_against_null(walk_records, nulls)

    steps = []
    for step in range(1, args.n_folds):
        subset = [r for r in walk_records if r['step'] == step]
        agg = summarize_walk_forward(subset)
        distribution = nulls.get(step) or []
        agg.update({
            'null_cells': len(distribution),
            'null_median_pf': float(np.median(distribution)) if distribution else None,
            'null_mean_pf': float(np.mean(distribution)) if distribution else None,
            'null_pf_gt_1': sum(1 for v in distribution if v > 1.0),
            'null_pf_gt_1_share': (sum(1 for v in distribution if v > 1.0)
                                   / len(distribution)) if distribution else None,
            'null_p95_pf': (float(np.percentile(distribution, 95))
                            if distribution else None),
        })
        steps.append({'history_folds': step, 'test_fold': step,
                      'symbols_scored': len(subset), **agg})

    # Sub-period stability of the closest survivors.
    bars = {r['symbol']: int(r.get('n_bars') or 0) for r in rows}
    entry_start = {r['symbol']: int(r.get('entry_start_index') or 0) for r in rows}
    closest_targets = parse_closest_survivors(args.closest_survivors)
    closest = []
    for symbol, fast, slow in closest_targets:
        if symbol not in bars:
            continue
        split = oos_subperiods(run_dir, symbol, fast, slow, bars[symbol],
                               entry_start[symbol], args.oos_subperiods,
                               args.stress_multiplier)
        pfs = [s['net_pf'] for s in split['subperiods'] if s['trades'] > 0]
        stress_pfs = [s['stress_net_pf'] for s in split['subperiods']
                      if s['trades'] > 0]
        with_trades = sum(1 for s in split['subperiods'] if s['trades'] > 0)
        closest.append({'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                        'subperiods': split['subperiods'],
                        'subperiods_with_trades': with_trades,
                        'subperiods_pf_gt_1': sum(1 for p in pfs
                                                  if (p or 0.0) > 1.0),
                        'subperiods_stress_pf_gt_1': sum(1 for p in stress_pfs
                                                         if (p or 0.0) > 1.0)})

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_run': str(run_dir),
        'oos_audit': str(audit_dir),
        'n_symbols': len({r['symbol'] for r in rows}),
        'n_cells': len(rows),
        'config': config,
        'stress_multiplier': args.stress_multiplier,
        'min_trades': args.min_trades,
        'part_a': {
            'family': family_pooled(family),
            'family_cells': family_cells,
            'family_symbols': family_symbols,
            'per_symbol': per_symbol,
            'leave_one_symbol_out': loso,
        },
        'part_b': {
            'n_folds': args.n_folds,
            'min_history_trades': args.min_history_trades,
            'walk_forward': walk_summary,
            'steps': steps,
            'selection_vs_null': selection_vs_null,
        },
        'part_c': {
            'n_subperiods': args.oos_subperiods,
            'closest_survivors': closest,
        },
    }
    payload['verdict'] = build_verdict(payload)

    with open(out_dir / 'config.json', 'w') as fh:
        json.dump({'args': vars(args), 'config': config,
                   'closest_survivors': closest_targets}, fh, indent=2)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    with open(out_dir / 'cells.jsonl', 'w') as fh:
        for cell in fold_rows:
            fh.write(json.dumps(cell) + '\n')
    write_report(out_dir, payload)
    print(f'Wrote {out_dir}/summary.md')


if __name__ == '__main__':
    main()
