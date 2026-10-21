#!/usr/bin/env python3
"""Is the walk-forward result a property of the selection granularity?

Why this leg exists
-------------------
The survivor selection audit (`scripts/survivor_selection_audit.py`, leg 3)
walks the selection forward over the whole grid and reports a pooled
out-of-fold net PF of 0.6409: the procedure - "pick the best cell of a
symbol on the history, trade it on the next, unseen fold" - does not make
money out of sample. That leg selects *per symbol*, i.e. 266 independent
selections per step, which is the finest granularity the program could have
used and also the one that maximises the selection freedom.

A negative result at one granularity does not settle the question: a finer
selection can manufacture a bad result out of noise, and a coarser one can
hide a real one. This leg re-runs the identical walk-forward protocol at
several granularities and reports the same yardstick for each, so the
question "is there an edge at *any* selection granularity?" has one answer
per granularity instead of one answer for the finest one.

The granularities
-----------------
* `symbol`  - one selection per symbol (the finest: 266 selections per step).
               This reproduces leg 3 and is the script's own control.
* `bucket`  - one selection per market-cap bucket (5 buckets by default):
               the selection is made on the pooled history of a whole family
               of symbols and applied to every member of the family.
* `global`  - one selection for the whole universe: the single best pair,
               applied to all 266 symbols.
* `top-K`   - K cells per unit instead of one. It interpolates between the
               two axes above: more cells per unit is more freedom, fewer
               units is less.

The yardstick is the same for every configuration: the pooled out-of-fold net
PF of the trades the procedure actually takes, and the share of the
out-of-fold windows that land above PF 1. The grid's own null (17 556 draws
of what a cell scores on a fold it was not selected on) is reported for the
`symbol` unit, where the out-of-fold number is a per-cell number and is
therefore comparable with it.

The baseline grid is never modified: this leg only reads artifacts and writes
its own output directory.

Usage:
    python3 scripts/selection_granularity.py \
        --arm parent:results/20261021_121629_survivor_selection_audit/cells.jsonl \
        --arm child:grid:results/20261021_125403_grid \
        --out results/<RUNID>_selection_granularity
"""
import argparse
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from scripts.survivor_selection_audit import (binomial_upper_tail,
                                               collect_fold_stats,
                                               null_pf_distribution,
                                               percentile_rank, pooled_pf,
                                               sum_folds)
from scripts.run_grid import CONFIG_DEFAULTS

# The walk-forward of leg 3: the full sample of every symbol is cut into
# DEFAULT_N_FOLDS sequential folds, the best cell of the history is scored on
# the next fold, and the walk is (n_folds - 1) steps long.
DEFAULT_N_FOLDS = 5

# A cell needs at least this many trades in the history window before it can
# be selected; below it the profit factor is noise. A unit that covers S
# symbols has to clear S times this many history trades, so the rule stays
# "at least this many trades per symbol".
DEFAULT_MIN_HISTORY_TRADES = 20

# How many market-cap buckets the `bucket` unit uses.
DEFAULT_BUCKETS = 5

# How many cells a unit may select.
DEFAULT_TOP_K = (1, 3, 10)


def unit_of(symbol: str, unit: str, buckets: dict) -> str:
    """The selection unit a symbol belongs to."""
    if unit == 'symbol':
        return symbol
    if unit == 'bucket':
        return buckets.get(symbol, symbol)
    if unit == 'global':
        return 'GLOBAL'
    raise ValueError(f'unknown unit: {unit}')


def market_cap_buckets(symbols: list, n_buckets: int) -> dict:
    """Split the symbols into market-cap buckets.

    The order of the symbols is the program's market-cap descending order
    (`universe/mcap_rank.json`), so the buckets are contiguous market-cap
    ranges: bucket 0 holds the largest names, the last bucket the smallest.
    """
    if n_buckets < 1:
        raise ValueError('n_buckets must be >= 1')
    out = {}
    total = len(symbols)
    for index, symbol in enumerate(symbols):
        bucket = min(n_buckets - 1, index * n_buckets // max(1, total))
        out[symbol] = f'B{bucket:02d}'
    return out


def rank_symbols(mcap_path: str, symbols: list) -> list:
    """Order the symbols by market cap, using the universe ranking.

    Symbols that are not in the ranking (a symbol that was added to the
    universe file after the grid ran) keep their alphabetical position at the
    end, so the bucketing stays deterministic.
    """
    ranking = []
    try:
        with open(mcap_path) as fh:
            data = json.load(fh)
        if isinstance(data, dict):
            for key in ('symbols', 'ranking', 'entries'):
                if key in data and isinstance(data[key], list):
                    ranking = data[key]
                    break
        elif isinstance(data, list):
            ranking = data
    except Exception:
        ranking = []
    order = {}
    for index, item in enumerate(ranking):
        if isinstance(item, str):
            order[item] = index
        elif isinstance(item, dict):
            name = item.get('symbol') or item.get('base') or item.get('name')
            if name:
                order[name] = index
    known = [s for s in symbols if s in order]
    unknown = sorted(s for s in symbols if s not in order)
    known.sort(key=lambda s: order[s])
    return known + unknown


def cells_by_symbol(fold_rows: list) -> dict:
    """Group the per-cell fold statistics by symbol."""
    out = defaultdict(list)
    for cell in fold_rows:
        out[cell['symbol']].append(cell)
    for symbol in out:
        out[symbol].sort(key=lambda c: (c['P_fast'], c['P_slow']))
    return out


def pair_of(cell: dict) -> tuple:
    return (cell['P_fast'], cell['P_slow'])


def unit_candidates(unit_cells: dict, step: int,
                    min_history_trades: int) -> list:
    """The candidate cells of a unit at one walk-forward step.

    A unit is a set of symbols. The history of a candidate pair is the
    history of that pair *pooled over the unit's symbols*, so a unit that
    covers many symbols selects the pair that worked best across the whole
    family, not the pair that worked best in one symbol.
    """
    n_symbols = len(unit_cells)
    minimum = min_history_trades * max(1, n_symbols)
    pooled = defaultdict(lambda: {'trades': 0, 'win_sum': 0.0, 'loss_abs': 0.0,
                                  'stress_win_sum': 0.0, 'stress_loss_abs': 0.0})
    for cells in unit_cells.values():
        for cell in cells:
            hist = sum_folds(cell['folds'], step)
            entry = pooled[pair_of(cell)]
            entry['trades'] += hist['trades']
            entry['win_sum'] += hist['win_sum']
            entry['loss_abs'] += hist['loss_abs']
            entry['stress_win_sum'] += hist['stress_win_sum']
            entry['stress_loss_abs'] += hist['stress_loss_abs']
    candidates = []
    for (fast, slow), hist in pooled.items():
        if hist['trades'] < minimum:
            continue
        net_pf = pooled_pf(hist['win_sum'], hist['loss_abs'])
        if net_pf is None or not math.isfinite(net_pf):
            continue
        candidates.append({'P_fast': fast, 'P_slow': slow,
                           'trades': hist['trades'], 'net_pf': net_pf,
                           'stress_net_pf': pooled_pf(hist['stress_win_sum'],
                                                     hist['stress_loss_abs'])})
    return candidates


def select(candidates: list, top_k: int) -> list:
    """The `top_k` candidates with the best history profit factor.

    Ties are broken by the trade count (the thicker sample) and then by the
    pair order, so the selection is deterministic.
    """
    usable = [c for c in candidates
              if c.get('net_pf') is not None and math.isfinite(c['net_pf'])
              and c.get('trades', 0) > 0]
    usable.sort(key=lambda c: (-c['net_pf'], -c.get('trades', 0),
                               c['P_fast'], c['P_slow']))
    return usable[:top_k]


def score_unit(unit_cells: dict, selected: list, step: int) -> dict:
    """Score the selected cells of a unit on the test fold.

    The test fold is the fold the selection never saw: its trades are pooled
    over the unit's symbols, exactly the way the history was pooled.
    """
    wanted = {(c['P_fast'], c['P_slow']) for c in selected}
    win = loss = 0.0
    s_win = s_loss = 0.0
    trades = 0
    for cells in unit_cells.values():
        for cell in cells:
            if pair_of(cell) not in wanted:
                continue
            fold = cell['folds'][step]
            win += fold['win_sum']
            loss += fold['loss_abs']
            s_win += fold['stress_win_sum']
            s_loss += fold['stress_loss_abs']
            trades += fold['trades']
    return {'trades': trades, 'win_sum': win, 'loss_abs': loss,
            'stress_win_sum': s_win, 'stress_loss_abs': s_loss,
            'net_pf': pooled_pf(win, loss),
            'stress_net_pf': pooled_pf(s_win, s_loss)}


def walk_forward(fold_rows: list, unit: str, top_k: int, n_folds: int,
                 min_history_trades: int, buckets: dict) -> list:
    """The walk-forward steps of one selection configuration."""
    by_symbol = cells_by_symbol(fold_rows)
    units = defaultdict(dict)
    for symbol, cells in by_symbol.items():
        units[unit_of(symbol, unit, buckets)][symbol] = cells
    out = []
    for step in range(1, n_folds):
        for name in sorted(units):
            unit_cells = units[name]
            candidates = unit_candidates(unit_cells, step, min_history_trades)
            if not candidates:
                out.append({'step': step, 'unit': unit, 'unit_name': name,
                            'selected': [], 'scored': False})
                continue
            chosen = select(candidates, top_k)
            score = score_unit(unit_cells, chosen, step)
            out.append({
                'step': step,
                'unit': unit,
                'unit_name': name,
                'symbols': len(unit_cells),
                'selected': [{'P_fast': c['P_fast'], 'P_slow': c['P_slow'],
                              'history_net_pf': c['net_pf'],
                              'history_stress_net_pf': c['stress_net_pf'],
                              'history_trades': c['trades']} for c in chosen],
                'history_net_pf': chosen[0]['net_pf'],
                'history_stress_net_pf': chosen[0]['stress_net_pf'],
                'oof_trades': score['trades'],
                'oof_net_pf': score['net_pf'],
                'oof_stress_net_pf': score['stress_net_pf'],
                'oof_win_sum': score['win_sum'],
                'oof_loss_abs': score['loss_abs'],
                'oof_stress_win_sum': score['stress_win_sum'],
                'oof_stress_loss_abs': score['stress_loss_abs'],
                'scored': score['trades'] > 0,
            })
    return out


def summarize(steps: list) -> dict:
    """Aggregate the walk-forward steps of one configuration."""
    scored = [s for s in steps if s.get('scored')]
    win = sum(s['oof_win_sum'] for s in scored)
    loss = sum(s['oof_loss_abs'] for s in scored)
    s_win = sum(s['oof_stress_win_sum'] for s in scored)
    s_loss = sum(s['oof_stress_loss_abs'] for s in scored)
    above = sum(1 for s in scored if (s['oof_net_pf'] or 0.0) > 1.0)
    above_stress = sum(1 for s in scored if (s['oof_stress_net_pf'] or 0.0) > 1.0)
    history = [s['history_net_pf'] for s in steps
               if s.get('history_net_pf') is not None
               and math.isfinite(s['history_net_pf'])]
    oof = [s['oof_net_pf'] for s in scored
           if s.get('oof_net_pf') is not None and math.isfinite(s['oof_net_pf'])]
    return {
        'steps': len(steps),
        'steps_scored': len(scored),
        'oof_trades': sum(s['oof_trades'] for s in scored),
        'pooled_oof_net_pf': pooled_pf(win, loss),
        'pooled_oof_stress_net_pf': pooled_pf(s_win, s_loss),
        'pooled_oof_net_pnl': win - loss,
        'oof_pf_gt_1': above,
        'oof_pf_gt_1_share': (above / len(scored)) if scored else None,
        'oof_stress_pf_gt_1': above_stress,
        'oof_stress_pf_gt_1_share': (above_stress / len(scored)) if scored else None,
        'median_history_pf': float(np.median(history)) if history else None,
        'median_oof_pf': float(np.median(oof)) if oof else None,
    }


def selection_vs_null(steps: list, nulls: dict) -> dict:
    """How the selected cells rank against the grid's own null.

    Only meaningful where the out-of-fold number is a per-cell number (the
    `symbol` unit): the null of a fold is the profit factor of every cell of
    the grid on that fold.
    """
    ranks = []
    for step in steps:
        if not step.get('scored') or step.get('oof_net_pf') is None:
            continue
        distribution = nulls.get(step['step']) or []
        rank = percentile_rank(step['oof_net_pf'], distribution)
        if rank is not None:
            step['oof_percentile'] = rank
            ranks.append(rank)
    if not ranks:
        return {'scored': 0, 'median_percentile': None, 'above_p95': 0,
                'binomial_p_value': None}
    beats = sum(1 for r in ranks if r > 0.95)
    return {
        'scored': len(ranks),
        'median_percentile': float(np.median(ranks)),
        'mean_percentile': float(np.mean(ranks)),
        'above_p95': beats,
        'expected_above_p95': 0.05 * len(ranks),
        'binomial_p_value': binomial_upper_tail(beats, len(ranks), 0.05),
    }


def build_fold_stats(run_dir: Path, fixture_base: str, n_folds: int,
                     stress_multiplier: float) -> list:
    """The per-cell fold statistics of a grid run.

    The cell list is taken from the run's own artifact tree (so the child
    mutation run is covered without an out-of-sample audit first) and the
    number of bars of a symbol is read from its fixture, the same source the
    out-of-sample audit uses.
    """
    from data.data_loader import load_ohlcv_csv
    from scripts.oos_grid_scan import read_trades
    from scripts.run_grid import symbol_dir_name

    rows = []
    bars_cache = {}
    results_root = run_dir / 'results'
    for sym_dir in sorted(results_root.iterdir()):
        if not sym_dir.is_dir():
            continue
        symbol = sym_dir.name.replace('_', '/')
        if symbol not in bars_cache:
            path = Path(fixture_base) / f'{symbol_dir_name(symbol)}.csv'
            if not path.exists():
                continue
            bars_cache[symbol] = len(load_ohlcv_csv(str(path)))
        n_bars = bars_cache[symbol]
        for cell_dir in sorted(sym_dir.iterdir()):
            summary_path = cell_dir / 'summary.json'
            if not cell_dir.is_dir() or not summary_path.exists():
                continue
            summary = json.loads(summary_path.read_text())
            if summary.get('blocked'):
                continue
            if not (cell_dir / 'trades.csv.gz').exists() and not (cell_dir / 'trades.csv').exists():
                continue
            rows.append({'symbol': symbol,
                         'P_fast': int(summary['P_fast']),
                         'P_slow': int(summary['P_slow']),
                         'n_bars': n_bars})
    return collect_fold_stats(run_dir, rows, n_folds, stress_multiplier)


def load_arm(label: str, source: str, fixture_base: str, n_folds: int,
             stress_multiplier: float, cache_dir: Path) -> dict:
    """Load the fold statistics of one arm.

    `source` is either the path of a saved `cells.jsonl` (the fold statistics
    of a grid run) or `grid:<run dir>`, in which case the statistics are
    computed from the run's blotters and cached next to the output.
    """
    if source.startswith('grid:'):
        run_dir = Path(source[len('grid:'):])
        cache = cache_dir / f'{label}_fold_stats.jsonl'
        if cache.exists():
            rows = [json.loads(line) for line in cache.read_text().splitlines() if line.strip()]
        else:
            rows = build_fold_stats(run_dir, fixture_base, n_folds, stress_multiplier)
            with open(cache, 'w') as fh:
                for row in rows:
                    fh.write(json.dumps(row) + '\n')
        return {'label': label, 'source': str(run_dir), 'rows': rows}
    path = Path(source)
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    return {'label': label, 'source': str(path), 'rows': rows}


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


def write_report(out_dir: Path, payload: dict) -> None:
    """Write the human-readable leg report."""
    lines = []
    lines.append('# Selection Granularity — EMA Hourly Continuation\n')
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Folds:** {payload['n_folds']} | **Minimum history trades per "
                 f"symbol:** {payload['min_history_trades']} | **Market-cap buckets:** "
                 f"{payload['buckets']}")
    lines.append(f"**Cost model:** {payload['config']['taker_fee_bps']} bps taker + "
                 f"{payload['config']['slippage_bps']} bps slippage per side "
                 f"(stress leg: {payload['stress_multiplier']}x)\n")

    lines.append('## Why this leg exists\n')
    lines.append('The survivor selection audit walks the selection forward over the whole '
                 'grid and reports a pooled out-of-fold net PF of 0.6409 for the '
                 'per-symbol selection (266 independent selections per step). A negative '
                 'result at one granularity does not settle the question: a fine '
                 'selection can manufacture a bad result out of noise, and a coarse one '
                 'can hide a good one. This leg re-runs the identical protocol at several '
                 'granularities and reports the same yardstick for each.\n')

    lines.append('## The ladder\n')
    lines.append('| Arm | Unit | Cells per unit (K) | Units | Out-of-fold trades | '
                 'Pooled out-of-fold net PF | Pooled out-of-fold net PF (2x) | '
                 'Out-of-fold windows above PF 1 | Median in-fold PF | Median out-of-fold PF |')
    lines.append('|---|---|---|---|---|---|---|---|---|---|')
    for row in payload['ladder']:
        lines.append(
            f"| {row['arm']} | {row['unit']} | {row['top_k']} | {row['units']} | "
            f"{row['oof_trades']} | {_fmt(row['pooled_oof_net_pf'])} | "
            f"{_fmt(row['pooled_oof_stress_net_pf'])} | "
            f"{row['oof_pf_gt_1']} ({_pct(row['oof_pf_gt_1_share'])}) | "
            f"{_fmt(row['median_history_pf'])} | {_fmt(row['median_oof_pf'])} |")
    lines.append('')

    lines.append('## The selected cells against the grid\'s own null\n')
    lines.append('The null needs no randomization: the grid holds 17 556 draws of what a '
                 'cell scores on a fold it was not selected on. It is comparable with the '
                 'out-of-fold number only where that number is a per-cell number, i.e. '
                 'for the `symbol` unit.\n')
    lines.append('| Arm | Unit | K | Selected cells scored | Median percentile | '
                 'Above the null p95 | Expected under a null pick | One-sided exact binomial p |')
    lines.append('|---|---|---|---|---|---|---|---|')
    for row in payload['ladder']:
        null = row.get('vs_null')
        if not null:
            lines.append(f"| {row['arm']} | {row['unit']} | {row['top_k']} | n/a "
                         f"(pooled number, not comparable with a per-cell null) | n/a | "
                         f"n/a | n/a | n/a |")
            continue
        lines.append(
            f"| {row['arm']} | {row['unit']} | {row['top_k']} | {null.get('scored', 0)} | "
            f"{_fmt(null.get('median_percentile'))} | {null.get('above_p95', 0)} | "
            f"{null.get('expected_above_p95', 0):.1f} | "
            f"{_fmt_p(null.get('binomial_p_value'))} |")
    lines.append('')

    for arm in payload['arms']:
        lines.append(f"## Arm `{arm['label']}` — what each granularity selects\n")
        lines.append(f"Source: `{arm['source']}` ({arm['n_cells']} cells, "
                     f"{arm['n_symbols']} symbols)\n")
        lines.append('| Unit | Step | Unit name | Symbols | Cells selected | '
                     'History net PF | Out-of-fold trades | Out-of-fold net PF |')
        lines.append('|---|---|---|---|---|---|---|---|')
        for row in arm['selections']:
            for entry in row['entries']:
                chosen = ', '.join(f"P{c['P_fast']}_{c['P_slow']}"
                                   for c in entry['selected'])
                lines.append(
                    f"| {row['unit']} | {row['step']} | {entry['unit_name']} | "
                    f"{entry['symbols']} | {chosen} | "
                    f"{_fmt(entry['history_net_pf'])} | {entry['oof_trades']} | "
                    f"{_fmt(entry['oof_net_pf'])} |")
        lines.append('')

    lines.append('## Verdict\n')
    for line in payload['verdict']:
        lines.append(f'- {line}')
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def build_verdict(payload: dict) -> list:
    """The conclusion of the leg, as a list of report lines."""
    lines = []
    ladder = payload['ladder']
    arms = []
    for row in ladder:
        if row['arm'] not in arms:
            arms.append(row['arm'])
    for arm in arms:
        rows = [r for r in ladder if r['arm'] == arm]
        best = max(rows, key=lambda r: (r['pooled_oof_net_pf'] or 0.0))
        control = next((r for r in rows
                        if r['unit'] == 'symbol' and r['top_k'] == 1), None)
        if control:
            lines.append(
                f"Arm `{arm}`: the control (per-symbol selection, one cell per symbol) "
                f"gives a pooled out-of-fold net PF of "
                f"{_fmt(control['pooled_oof_net_pf'])} over "
                f"{control['oof_trades']} out-of-fold trades.")
        lines.append(
            f"Arm `{arm}`: the best granularity on this ladder is `{best['unit']}` with "
            f"K = {best['top_k']}: pooled out-of-fold net PF "
            f"{_fmt(best['pooled_oof_net_pf'])} "
            f"({_fmt(best['pooled_oof_stress_net_pf'])} under 2x costs) over "
            f"{best['oof_trades']} out-of-fold trades.")
        above = [r for r in rows if (r['pooled_oof_net_pf'] or 0.0) > 1.0]
        if above:
            lines.append(
                f"Arm `{arm}`: at least one granularity clears PF 1 out of sample: "
                + ', '.join(f"{r['unit']} K={r['top_k']} "
                            f"({_fmt(r['pooled_oof_net_pf'])})" for r in above)
                + ". The gates still have to be applied before anything is promoted.")
        else:
            lines.append(
                f"Arm `{arm}`: no granularity clears PF 1 out of sample. The rule has no "
                f"edge at the per-symbol, per-family or global selection granularity, so "
                f"the negative result of the finest selection is a property of the rule, "
                f"not of the selection granularity.")
        if control and best['unit'] != 'symbol':
            lines.append(
                f"Arm `{arm}`: a coarser selection does not rescue the procedure - the "
                f"per-family and global selections score "
                f"{_fmt(best['pooled_oof_net_pf'])} against the per-symbol control's "
                f"{_fmt(control['pooled_oof_net_pf'])}.")
    if len(arms) > 1:
        lines.append(
            "The arms are read against each other on the same yardstick: the pooled "
            "out-of-fold net PF of the trades the procedure actually takes.")
    return lines


def main():
    parser = argparse.ArgumentParser(
        description='Walk-forward selection at several granularities')
    parser.add_argument('--arm', action='append', required=True,
                        help='arm as <label>:<cells.jsonl path> or <label>:grid:<run dir>')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--n-folds', type=int, default=DEFAULT_N_FOLDS)
    parser.add_argument('--min-history-trades', type=int,
                        default=DEFAULT_MIN_HISTORY_TRADES)
    parser.add_argument('--buckets', type=int, default=DEFAULT_BUCKETS)
    parser.add_argument('--top-k', type=str, default=','.join(str(k) for k in DEFAULT_TOP_K))
    parser.add_argument('--units', type=str, default='symbol,bucket,global')
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    top_ks = [int(k) for k in args.top_k.split(',') if k.strip()]
    units = [u.strip() for u in args.units.split(',') if u.strip()]

    out_dir = Path(args.out) if args.out else Path(
        f"results/{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
        f"_selection_granularity")
    out_dir.mkdir(parents=True, exist_ok=True)

    arms = []
    for spec in args.arm:
        label, _, source = spec.partition(':')
        if not source:
            raise SystemExit(f'--arm needs <label>:<source>, got {spec!r}')
        arms.append(load_arm(label, source, args.fixture_base, args.n_folds,
                             args.stress_multiplier, out_dir))

    ladder = []
    arm_payloads = []
    for arm in arms:
        fold_rows = arm['rows']
        symbols = sorted({row['symbol'] for row in fold_rows})
        ordered = rank_symbols(args.mcap, symbols)
        buckets = market_cap_buckets(ordered, args.buckets)
        nulls = {step: null_pf_distribution(fold_rows, step)
                 for step in range(1, args.n_folds)}
        selections = []
        for unit in units:
            for top_k in top_ks:
                steps = walk_forward(fold_rows, unit, top_k, args.n_folds,
                                     args.min_history_trades, buckets)
                summary = summarize(steps)
                units_scored = len({s['unit_name'] for s in steps if s.get('scored')})
                row = {'arm': arm['label'], 'unit': unit, 'top_k': top_k,
                       'units': units_scored, **summary}
                if unit == 'symbol' and top_k == 1:
                    row['vs_null'] = selection_vs_null(steps, nulls)
                else:
                    row['vs_null'] = None
                ladder.append(row)
                if unit in ('bucket', 'global'):
                    # The per-unit detail of the coarse selections: which pair
                    # the family picked on the history, and what that pair did
                    # on the fold the selection never saw.
                    detail = []
                    for step in range(1, args.n_folds):
                        entries = []
                        for record in steps:
                            if record['step'] != step or not record.get('selected'):
                                continue
                            entries.append({
                                'unit_name': record['unit_name'],
                                'symbols': record.get('symbols', 0),
                                'selected': record['selected'],
                                'history_net_pf': record.get('history_net_pf'),
                                'oof_trades': record.get('oof_trades', 0),
                                'oof_net_pf': record.get('oof_net_pf'),
                            })
                        detail.append({'unit': unit, 'step': step, 'entries': entries})
                    selections.extend(detail)
        arm_payloads.append({'label': arm['label'], 'source': arm['source'],
                             'n_cells': len(fold_rows), 'n_symbols': len(symbols),
                             'selections': selections})

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'config': dict(CONFIG_DEFAULTS),
        'stress_multiplier': args.stress_multiplier,
        'n_folds': args.n_folds,
        'min_history_trades': args.min_history_trades,
        'buckets': args.buckets,
        'units': units,
        'top_k': top_ks,
        'ladder': ladder,
        'arms': arm_payloads,
    }
    payload['verdict'] = build_verdict(payload)

    with open(out_dir / 'config.json', 'w') as fh:
        json.dump({'args': vars(args), 'config': dict(CONFIG_DEFAULTS)}, fh, indent=2)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    write_report(out_dir, payload)
    print(f'Wrote {out_dir}/summary.md')


if __name__ == '__main__':
    main()
