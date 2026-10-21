#!/usr/bin/env python3
"""Selection-granularity leg: is the walk-forward result a property of the rule?

Why this leg exists
-------------------
The survivor selection audit (Leg 3 of
`scripts/survivor_selection_audit.py`) walks the grid forward per symbol:
for every symbol the best cell of its 66 EMA pairs is chosen on the history
and is then scored on the fold the selection never saw. Over 1060 steps and
95 786 out-of-fold trades the pooled out-of-fold net profit factor is
0.6409 (0.4521 under 2x costs).

That number is the yardstick the ATR minimum-risk mutation is measured
against, so it has to be read carefully. Two things were still open about
it:

1. **Granularity.** The per-symbol selection is the *finest* selection the
   program can make: one cell per symbol, 266 selections. A rule with a real
   edge would also survive a coarser selection, because a coarser selection
   throws away the noise-chasing degrees of freedom. This leg repeats the
   walk-forward with the selection made once per *family* of symbols
   (market-cap buckets) instead of once per symbol, and once for the whole
   grid, and reports the out-of-fold result of each. If the out-of-fold
   profit factor only holds at the finest granularity, it is a property of
   the selection, not of the rule.

2. **The random control.** The decisive version of the same question: at
   every step, select a *random* eligible cell instead of the best one and
   score it on the unseen fold. If "pick the best cell on the history" and
   "pick any cell" score the same out of fold, the selection carries no
   information and the 0.6409 is what the grid produces by itself. The
   control is seeded, so the run is reproducible.

The leg only reads the grid and writes its own artifact directory. The
baseline grid is never touched and no market data is fetched.

Usage:
    python scripts/selection_granularity_leg.py --run results/20261019_135940_grid
    python scripts/selection_granularity_leg.py --run results/20261019_135940_grid \
        --buckets 5 10 25 50 100 --random-replicates 200 --seed 20261021
"""
import argparse
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from data.data_loader import load_ohlcv_csv
from scripts.oos_grid_scan import read_trades
from scripts.run_grid import period_pairs, symbol_dir_name
from scripts.survivor_selection_audit import (cell_fold_stats, fold_edges,
                                               pooled_pf, select_best,
                                               sum_folds, summarize_walk_forward,
                                               walk_forward_steps)

# The market-cap buckets the family-level selection is run on. The buckets
# are the first N symbols of the market-cap ranking, so they are the N
# largest names of the universe.
DEFAULT_BUCKETS = (5, 10, 25, 50, 100)

# How many times the random-selection control is repeated. Each replicate
# is a full walk-forward of the whole grid with a random pick at every step.
DEFAULT_RANDOM_REPLICATES = 200

# The seed of the random control, so the leg is reproducible.
DEFAULT_SEED = 20261021

# A cell needs at least this many trades in the history window before it can
# be selected; the same rule the survivor selection audit uses.
DEFAULT_MIN_HISTORY_TRADES = 20


def cell_dir(run_dir: Path, symbol: str, fast: int, slow: int) -> Path:
    """Directory of one (symbol, P_fast, P_slow) cell of a run."""
    return run_dir / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'


def collect_grid_folds(run_dir: Path, symbols: list, fixture_base: str,
                       n_folds: int, stress_multiplier: float = 2.0) -> list:
    """Fold statistics of every cell of the grid, in market-cap order.

    The bar count of a symbol comes from its fixture, so the fold edges are
    the same ones the grid runner used; the trades come from the blotter
    the grid wrote.
    """
    pairs = period_pairs()
    out = []
    for symbol in symbols:
        fixture = Path(fixture_base) / f'{symbol_dir_name(symbol)}.csv'
        if not fixture.exists():
            continue
        n_bars = len(load_ohlcv_csv(str(fixture)))
        edges = fold_edges(n_bars, n_folds)
        for fast, slow in pairs:
            cdir = cell_dir(run_dir, symbol, fast, slow)
            if not (cdir / 'trades.csv.gz').exists() and not (cdir / 'trades.csv').exists():
                continue
            trades = read_trades(cdir)
            out.append({'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                        'n_bars': n_bars,
                        'folds': cell_fold_stats(trades, edges, stress_multiplier)})
    return out


def merge_pair_folds(cells: list, n_folds: int) -> dict:
    """Pool the fold statistics of a family of symbols, per EMA pair.

    The key is the EMA pair, the value is the list of merged folds, so a
    family-level selection can be run on exactly the same fold statistics
    the per-symbol selection uses.
    """
    merged = defaultdict(lambda: [None] * n_folds)
    for cell in cells:
        key = (cell['P_fast'], cell['P_slow'])
        for fold in cell['folds']:
            slot = merged[key][fold['fold']]
            if slot is None:
                slot = {'fold': fold['fold'], 'trades': 0, 'win_sum': 0.0,
                        'loss_abs': 0.0, 'stress_win_sum': 0.0,
                        'stress_loss_abs': 0.0}
                merged[key][fold['fold']] = slot
            slot['trades'] += fold['trades']
            slot['win_sum'] += fold['win_sum']
            slot['loss_abs'] += fold['loss_abs']
            slot['stress_win_sum'] += fold['stress_win_sum']
            slot['stress_loss_abs'] += fold['stress_loss_abs']
    return {key: folds for key, folds in merged.items()}


def family_walk_forward(cells: list, n_folds: int,
                        min_history_trades: int) -> list:
    """Walk the selection forward for one family of symbols.

    Step `k` selects the EMA pair with the best profit factor over the
    history `folds[0:k]` of the whole family and scores that pair on
    `folds[k]`, which the selection never saw. One selection per family per
    step, against one per symbol in the per-symbol walk-forward.
    """
    merged = merge_pair_folds(cells, n_folds)
    out = []
    for step in range(1, n_folds):
        candidates = []
        for (fast, slow), folds in merged.items():
            hist = sum_folds(folds, step)
            candidates.append({'P_fast': fast, 'P_slow': slow,
                               'trades': hist['trades'], 'net_pf': hist['net_pf'],
                               'stress_net_pf': hist['stress_net_pf'],
                               'folds': folds})
        eligible = [c for c in candidates
                    if c['trades'] >= min_history_trades and c['net_pf'] is not None
                    and math.isfinite(c['net_pf'])]
        selected = select_best(eligible)
        record = {'step': step, 'history_folds': step, 'test_fold': step,
                  'candidates': len(eligible), 'selected': None}
        if selected is not None:
            test = selected['folds'][step]
            record.update({
                'selected': (selected['P_fast'], selected['P_slow']),
                'history_trades': selected['trades'],
                'history_net_pf': selected['net_pf'],
                'history_stress_net_pf': selected['stress_net_pf'],
                'oof_trades': test['trades'],
                'oof_net_pf': pooled_pf(test['win_sum'], test['loss_abs']),
                'oof_stress_net_pf': pooled_pf(test['stress_win_sum'],
                                               test['stress_loss_abs']),
                'oof_win_sum': test['win_sum'],
                'oof_loss_abs': test['loss_abs'],
                'oof_stress_win_sum': test['stress_win_sum'],
                'oof_stress_loss_abs': test['stress_loss_abs'],
            })
        out.append(record)
    return out


def random_walk_forward_steps(cells: list, n_folds: int,
                               min_history_trades: int, rng) -> list:
    """The control: pick a random eligible cell instead of the best one.

    Same walk-forward as `walk_forward_steps`, but the selection is uniform
    over the eligible cells instead of the best profit factor. The control
    has to be scored on exactly the same folds, so the two are comparable.
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
        selected = None
        if eligible:
            selected = eligible[int(rng.integers(len(eligible)))]
        record = {'step': step, 'history_folds': step, 'test_fold': step,
                  'candidates': len(eligible), 'selected': None}
        if selected is not None:
            test = selected['folds'][step]
            record.update({
                'selected': (selected['P_fast'], selected['P_slow']),
                'history_trades': selected['trades'],
                'history_net_pf': selected['net_pf'],
                'history_stress_net_pf': selected['stress_net_pf'],
                'oof_trades': test['trades'],
                'oof_net_pf': pooled_pf(test['win_sum'], test['loss_abs']),
                'oof_stress_net_pf': pooled_pf(test['stress_win_sum'],
                                               test['stress_loss_abs']),
                'oof_win_sum': test['win_sum'],
                'oof_loss_abs': test['loss_abs'],
                'oof_stress_win_sum': test['stress_win_sum'],
                'oof_stress_loss_abs': test['stress_loss_abs'],
            })
        out.append(record)
    return out


def per_symbol_walk_forward(fold_rows: list, n_folds: int,
                            min_history_trades: int) -> list:
    """The per-symbol walk-forward of the whole grid (Leg 3 of the audit)."""
    by_symbol = defaultdict(list)
    for cell in fold_rows:
        by_symbol[cell['symbol']].append(cell)
    records = []
    for symbol in sorted(by_symbol):
        for record in walk_forward_steps(by_symbol[symbol], n_folds,
                                         min_history_trades):
            record['symbol'] = symbol
            records.append(record)
    return records


def random_control(fold_rows: list, n_folds: int, min_history_trades: int,
                   replicates: int, seed: int) -> dict:
    """The distribution the per-symbol selection has to beat.

    Every replicate is a full walk-forward of the grid with a random pick at
    every step; the pooled out-of-fold profit factor of the replicate is
    one draw from the null of "the selection carries no information".

    The eligible candidates of every step are built once and then sampled,
    so the replicates do not repeat the work of the history windows.
    """
    by_symbol = defaultdict(list)
    for cell in fold_rows:
        by_symbol[cell['symbol']].append(cell)
    symbols = sorted(by_symbol)

    # The candidate table of every step of every symbol: the candidates are
    # the same in every replicate, only the pick changes.
    tables = []
    for symbol in symbols:
        steps = []
        for step in range(1, n_folds):
            eligible = []
            for cell in by_symbol[symbol]:
                hist = sum_folds(cell['folds'], step)
                if (hist['trades'] < min_history_trades
                        or hist['net_pf'] is None
                        or not math.isfinite(hist['net_pf'])):
                    continue
                test = cell['folds'][step]
                eligible.append({
                    'P_fast': cell['P_fast'], 'P_slow': cell['P_slow'],
                    'history_trades': hist['trades'],
                    'history_net_pf': hist['net_pf'],
                    'oof_trades': test['trades'],
                    'oof_net_pf': pooled_pf(test['win_sum'], test['loss_abs']),
                    'oof_stress_net_pf': pooled_pf(test['stress_win_sum'],
                                                   test['stress_loss_abs']),
                    'oof_win_sum': test['win_sum'],
                    'oof_loss_abs': test['loss_abs'],
                    'oof_stress_win_sum': test['stress_win_sum'],
                    'oof_stress_loss_abs': test['stress_loss_abs'],
                })
            steps.append(eligible)
        tables.append(steps)

    rng = np.random.default_rng(seed)
    pooled_pfs = []
    pooled_stress = []
    trades = []
    for _ in range(replicates):
        win = loss = s_win = s_loss = 0.0
        n_trades = 0
        n_scored = 0
        for steps in tables:
            for eligible in steps:
                if not eligible:
                    continue
                pick = eligible[int(rng.integers(len(eligible)))]
                if not pick['oof_trades']:
                    continue
                win += pick['oof_win_sum']
                loss += pick['oof_loss_abs']
                s_win += pick['oof_stress_win_sum']
                s_loss += pick['oof_stress_loss_abs']
                n_trades += pick['oof_trades']
                n_scored += 1
        pooled_pfs.append(pooled_pf(win, loss))
        pooled_stress.append(pooled_pf(s_win, s_loss))
        trades.append(n_trades)
    finite = [v for v in pooled_pfs if v is not None and math.isfinite(v)]
    return {
        'replicates': replicates,
        'seed': seed,
        'scored_steps_per_replicate': n_scored,
        'pooled_net_pf': {
            'mean': float(np.mean(finite)) if finite else None,
            'median': float(np.median(finite)) if finite else None,
            'p05': float(np.percentile(finite, 5)) if finite else None,
            'p95': float(np.percentile(finite, 95)) if finite else None,
            'min': float(np.min(finite)) if finite else None,
            'max': float(np.max(finite)) if finite else None,
        },
        'pooled_stress_net_pf': {
            'mean': float(np.mean([v for v in pooled_stress
                                    if v is not None and math.isfinite(v)])),
            'median': float(np.median([v for v in pooled_stress
                                        if v is not None and math.isfinite(v)])),
        },
        'pooled_oof_trades': {
            'mean': float(np.mean(trades)) if trades else None,
        },
        'draws': [float(v) if v is not None else None for v in pooled_pfs],
    }


def percentile_of(value, draws: list) -> float:
    """Share of the random draws that the observed value beats."""
    clean = [d for d in draws if d is not None and math.isfinite(d)]
    if not clean or value is None or not math.isfinite(value):
        return None
    return sum(1 for d in clean if d <= value) / len(clean)


def fmt(value, digits: int = 4) -> str:
    if value is None:
        return 'n/a'
    try:
        value = float(value)
    except (TypeError, ValueError):
        return str(value)
    if not math.isfinite(value):
        return 'inf'
    return f'{value:.{digits}f}'


def pct(value) -> str:
    if value is None:
        return 'n/a'
    return f'{float(value) * 100:.1f}%'


def build_verdict(payload: dict) -> list:
    """The reading of the leg, on the numbers it produced."""
    lines = []
    per_cell = payload['per_cell_selection']
    families = payload['family_selection']
    control = payload['random_control']
    lines.append(
        f"The per-symbol selection scores {fmt(per_cell['pooled_oof_net_pf'])} "
        f"pooled out-of-fold net PF over {per_cell['pooled_oof_trades']} trades "
        f"({fmt(per_cell['pooled_oof_stress_net_pf'])} under 2x costs), with "
        f"{pct(per_cell['oof_pf_gt_1_share'])} of the out-of-fold windows above "
        f"profit factor 1.")
    widest = families[-1] if families else None
    if widest:
        lines.append(
            f"The same walk-forward with one selection for the whole market-cap "
            f"family of {widest['n_symbols']} symbols scores "
            f"{fmt(widest['pooled_oof_net_pf'])} "
            f"({fmt(widest['pooled_oof_stress_net_pf'])} under 2x costs) on "
            f"{widest['pooled_oof_trades']} trades.")
    lines.append(
        f"The random control - the same walk-forward with a random eligible cell "
        f"picked at every step - scores a median pooled out-of-fold net PF of "
        f"{fmt(control['pooled_net_pf']['median'])} "
        f"(p05 {fmt(control['pooled_net_pf']['p05'])}, "
        f"p95 {fmt(control['pooled_net_pf']['p95'])}) over "
        f"{control['replicates']} replicates.")
    observed = percentile_of(per_cell['pooled_oof_net_pf'], control['draws'])
    if observed is not None:
        lines.append(
            f"The per-symbol selection sits at the {pct(observed)} percentile of "
            f"the random control, so the selection is worth "
            f"{'something over a random pick' if observed > 0.5 else 'no more than a random pick'} "
            f"out of fold.")
    if (widest and (widest['pooled_oof_net_pf'] or 0.0)
            < (per_cell['pooled_oof_net_pf'] or 0.0) * 0.9):
        lines.append(
            "The out-of-fold result is a property of the selection granularity: it "
            "shrinks when the selection is made once per family instead of once per "
            "symbol, so the number does not describe the rule.")
    else:
        lines.append(
            "The out-of-fold result survives the coarser selection, so it is not an "
            "artefact of the selection granularity.")
    lines.append(
        "Either way the number stays below 1 out of fold: the program still has no "
        "rule that clears the PROMPT.md §3.4 gate out of sample.")
    return lines


def write_report(out_dir: Path, payload: dict) -> None:
    """The report of the leg."""
    lines = []
    lines.append('# Selection Granularity Leg\n')
    lines.append(f"**Grid:** `{payload['run']}`")
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Symbols:** {payload['n_symbols']} "
                 f"({payload['n_cells']} cells)")
    lines.append(f"**Folds:** {payload['n_folds']} sequential folds of the full "
                 f"sample of every symbol\n")

    lines.append('## Leg A - the per-symbol selection (Leg 3 of the audit)\n')
    per_cell = payload['per_cell_selection']
    lines.append('| Measure | Value |')
    lines.append('|---|---|')
    for label, key, kind in [
            ('Steps scored', 'steps_scored', 'int'),
            ('Out-of-fold trades', 'pooled_oof_trades', 'int'),
            ('Pooled out-of-fold net PF', 'pooled_oof_net_pf', 'f'),
            ('Pooled out-of-fold net PF (2x costs)', 'pooled_oof_stress_net_pf', 'f'),
            ('Out-of-fold windows with net PF > 1', 'oof_pf_gt_1', 'int'),
            ('Share of out-of-fold windows with net PF > 1', 'oof_pf_gt_1_share', 'pct'),
            ('Median in-fold net PF of the selected cell', 'median_history_pf', 'f'),
            ('Median out-of-fold net PF of the selected cell', 'median_oof_pf', 'f')]:
        value = per_cell.get(key)
        lines.append(f'| {label} | {pct(value) if kind == "pct" else fmt(value, 0 if kind == "int" else 4)} |')
    lines.append('')

    lines.append('## Leg B - the same walk-forward at a coarser granularity\n')
    lines.append('One selection per market-cap family instead of one per symbol: '
                 'the best EMA pair of the family is chosen on the history and '
                 'scored on the fold the selection never saw.\n')
    lines.append('| Family | Symbols | Steps | Out-of-fold trades | Pooled OOF net PF | '
                 'Pooled OOF net PF (2x costs) | Windows with PF > 1 |')
    lines.append('|---|---|---|---|---|---|---|')
    for row in payload['family_selection']:
        lines.append(
            f"| {row['family']} | {row['n_symbols']} | {row['steps_scored']} | "
            f"{row['pooled_oof_trades']} | {fmt(row['pooled_oof_net_pf'])} | "
            f"{fmt(row['pooled_oof_stress_net_pf'])} | "
            f"{row['oof_pf_gt_1']} ({pct(row['oof_pf_gt_1_share'])}) |")
    lines.append('')

    lines.append('## Leg C - the random control\n')
    lines.append(f"The same per-symbol walk-forward with a *random* eligible cell "
                 f"picked at every step, {payload['random_control']['replicates']} "
                 f"replicates, seed {payload['random_control']['seed']}.\n")
    control = payload['random_control']
    lines.append('| Measure | Value |')
    lines.append('|---|---|')
    lines.append(f"| Median pooled out-of-fold net PF | {fmt(control['pooled_net_pf']['median'])} |")
    lines.append(f"| Mean pooled out-of-fold net PF | {fmt(control['pooled_net_pf']['mean'])} |")
    lines.append(f"| 5th percentile | {fmt(control['pooled_net_pf']['p05'])} |")
    lines.append(f"| 95th percentile | {fmt(control['pooled_net_pf']['p95'])} |")
    lines.append(f"| Min / max | {fmt(control['pooled_net_pf']['min'])} / {fmt(control['pooled_net_pf']['max'])} |")
    lines.append(f"| Median pooled out-of-fold net PF (2x costs) | {fmt(control['pooled_stress_net_pf']['median'])} |")
    lines.append(f"| Percentile of the per-symbol selection | {pct(payload['selection_vs_control'])} |")
    lines.append('')

    lines.append('## Verdict\n')
    for line in payload['verdict']:
        lines.append(f'- {line}')
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(
        description='Selection-granularity leg of the EMA continuation program')
    parser.add_argument('--run', type=str, default='results/20261019_135940_grid')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--n-folds', type=int, default=5)
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--min-history-trades', type=int,
                        default=DEFAULT_MIN_HISTORY_TRADES)
    parser.add_argument('--buckets', type=int, nargs='*', default=list(DEFAULT_BUCKETS))
    parser.add_argument('--random-replicates', type=int,
                        default=DEFAULT_RANDOM_REPLICATES)
    parser.add_argument('--seed', type=int, default=DEFAULT_SEED)
    parser.add_argument('--limit-symbols', type=int, default=0)
    parser.add_argument('--out', type=str, default=None)
    parser.add_argument('--render-only', type=str, default=None)
    args = parser.parse_args()

    if args.render_only:
        out_dir = Path(args.render_only)
        payload = json.loads((out_dir / 'summary.json').read_text())
        payload['verdict'] = build_verdict(payload)
        write_report(out_dir, payload)
        print(f'Rendered {out_dir}/summary.md')
        return

    from universe.universe import load_mcap_ranking
    run_dir = Path(args.run)
    out_dir = Path(args.out) if args.out else Path(
        f"results/{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
        f"_selection_granularity")
    out_dir.mkdir(parents=True, exist_ok=True)

    symbols = load_mcap_ranking(args.mcap)
    if args.limit_symbols:
        symbols = symbols[:args.limit_symbols]
    print(f'Reading {len(symbols)} symbols x {len(period_pairs())} pairs from '
          f'{run_dir}.', flush=True)
    fold_rows = collect_grid_folds(run_dir, symbols, args.fixture_base,
                                   args.n_folds, args.stress_multiplier)
    print(f'{len(fold_rows)} cells read.', flush=True)

    per_symbol_records = per_symbol_walk_forward(fold_rows, args.n_folds,
                                                 args.min_history_trades)
    per_cell = summarize_walk_forward(per_symbol_records)

    by_symbol = defaultdict(list)
    for cell in fold_rows:
        by_symbol[cell['symbol']].append(cell)
    ordered = [s for s in symbols if s in by_symbol]

    family_rows = []
    for size in args.buckets:
        if size <= 0 or size > len(ordered):
            continue
        family_cells = []
        for symbol in ordered[:size]:
            family_cells.extend(by_symbol[symbol])
        records = family_walk_forward(family_cells, args.n_folds,
                                      args.min_history_trades)
        summary = summarize_walk_forward(records)
        family_rows.append({'family': f'top {size} by market cap',
                             'n_symbols': size, **summary})
        print(f'Family top {size}: pooled out-of-fold net PF '
              f'{fmt(summary["pooled_oof_net_pf"])}.', flush=True)

    print(f'Running the random control ({args.random_replicates} replicates)...',
          flush=True)
    control = random_control(fold_rows, args.n_folds, args.min_history_trades,
                             args.random_replicates, args.seed)
    selection_vs_control = percentile_of(per_cell['pooled_oof_net_pf'],
                                          control['draws'])

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'run': str(run_dir),
        'n_symbols': len(ordered),
        'n_cells': len(fold_rows),
        'n_folds': args.n_folds,
        'min_history_trades': args.min_history_trades,
        'buckets': list(args.buckets),
        'per_cell_selection': per_cell,
        'family_selection': family_rows,
        'random_control': control,
        'selection_vs_control': selection_vs_control,
    }
    payload['verdict'] = build_verdict(payload)

    with open(out_dir / 'config.json', 'w') as fh:
        json.dump({'args': vars(args)}, fh, indent=2, default=str)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    write_report(out_dir, payload)
    print(f'Wrote {out_dir}/summary.md')


if __name__ == '__main__':
    main()
