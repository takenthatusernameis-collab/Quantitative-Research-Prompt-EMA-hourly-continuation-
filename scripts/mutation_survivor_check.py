#!/usr/bin/env python3
"""Read the gate-clearing cells of a mutation child grid and test them.

Why this exists
---------------
The ATR minimum-risk mutation removes the cost drag of the baseline grid, and
that is enough to make cells *able* to clear the PROMPT.md §3.4 gate: the
child grid produces cells with an out-of-sample net PF above 1 that is still
above 1 under 2x costs, which the parent grid never does. A cell that clears
a gate is a selection result, not a promotion. This leg asks the questions
that decide whether it is anything else:

* **Leg 1 - the family:** how many child cells clear the gate, on how many
  symbols, and how do they compare with the child's own cell distribution;
* **Leg 2 - concentration:** the pooled out-of-sample profit factor of the
  family, and what it becomes when each symbol is dropped in turn, so a
  family that stands on one symbol is visible;
* **Leg 3 - sub-period stability:** the out-of-sample window of every
  gate-clearing cell is cut into sequential sub-periods, and a cell that only
  works in one stretch of time is not an edge;
* **Leg 4 - the selection against the child's own cells:** where each
  gate-clearing cell ranks inside the distribution of the child's own
  out-of-sample scores.

The randomized null of the child grid (the leg that says whether these cells
beat their own randomizations) is a separate, expensive leg and is run on the
complete child grid; this leg is the cheap half of that question.

Usage:
    python scripts/mutation_survivor_check.py \
        --child results/20261021_172619_grid \
        --out results/<TS>_mutation_survivor_check
"""
import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from data.data_loader import load_ohlcv_csv
from scripts.mutation_eval import cell_dir, complete_symbols, symbol_bars
from scripts.oos_grid_scan import (entry_start_index, net_profit_factor,
                                    read_trades, stressed_pnl_net, win_loss_sums)
from scripts.run_grid import period_pairs
from scripts.survivor_selection_audit import oos_subperiods


def cell_rows(child_dir: Path, symbols: list, fixture_base: str,
              oos_fraction: float, stress_multiplier: float,
              min_trades: int) -> list:
    """The out-of-sample score of every cell of the child grid."""
    cache = {}
    rows = []
    for symbol in symbols:
        n_bars = symbol_bars(fixture_base, symbol, cache)
        entry_start = entry_start_index(n_bars, oos_fraction)
        for fast, slow in period_pairs():
            cdir = cell_dir(child_dir, symbol, fast, slow)
            if not (cdir / 'summary.json').exists():
                continue
            try:
                trades = read_trades(cdir)
            except Exception:
                # a cell that is still being written is not a result
                continue
            oos = trades[trades['bar_index'] >= entry_start]
            net = oos['pnl_net'].to_numpy(dtype=float)
            stress = stressed_pnl_net(net, oos['entry_cost'].to_numpy(dtype=float),
                                      oos['exit_cost'].to_numpy(dtype=float),
                                      stress_multiplier)
            oos_pf = net_profit_factor(net)
            stress_pf = net_profit_factor(stress)
            full_net = trades['pnl_net'].to_numpy(dtype=float)
            rows.append({
                'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                'n_bars': n_bars, 'entry_start_index': entry_start,
                'oos_trades': int(len(oos)),
                'oos_net_pf': oos_pf,
                'oos_stress_net_pf': stress_pf,
                'full_net_pf': net_profit_factor(full_net),
                'oos_win_sum': win_loss_sums(net)[0],
                'oos_loss_abs': win_loss_sums(net)[1],
                'clears_gate': bool((oos_pf or 0.0) > 1.0
                                    and (stress_pf or 0.0) > 1.0
                                    and int(len(oos)) >= min_trades),
            })
    return rows


def family_pooled(rows: list) -> dict:
    """The pooled out-of-sample profit factor of a set of cells."""
    win = sum(r['oos_win_sum'] for r in rows)
    loss = sum(r['oos_loss_abs'] for r in rows)
    pf = (win / loss) if loss > 0 else None
    return {'cells': len(rows), 'trades': sum(r['oos_trades'] for r in rows),
            'pooled_oos_net_pf': pf, 'pooled_oos_net_pnl': win - loss}


def leave_one_symbol_out(rows: list) -> list:
    """The family with each symbol dropped in turn."""
    symbols = sorted({r['symbol'] for r in rows})
    out = []
    for symbol in symbols:
        without = [r for r in rows if r['symbol'] != symbol]
        pooled = family_pooled(without)
        pooled['dropped_symbol'] = symbol
        pooled['cells_left'] = pooled['cells']
        pooled['gate_cells_left'] = sum(1 for r in without if r['clears_gate'])
        out.append(pooled)
    return out


def subperiod_stability(child_dir: Path, rows: list, subperiods: int,
                        stress_multiplier: float) -> list:
    """Split the out-of-sample window of every gate-clearing cell."""
    out = []
    for row in rows:
        if not row['clears_gate']:
            continue
        result = oos_subperiods(child_dir, row['symbol'], row['P_fast'],
                                 row['P_slow'], row['n_bars'],
                                 row['entry_start_index'], subperiods,
                                 stress_multiplier)
        subs = result['subperiods']
        with_trades = [s for s in subs if s['trades'] > 0]
        out.append({
            'symbol': row['symbol'], 'P_fast': row['P_fast'],
            'P_slow': row['P_slow'],
            'oos_trades': row['oos_trades'],
            'oos_net_pf': row['oos_net_pf'],
            'oos_stress_net_pf': row['oos_stress_net_pf'],
            'subperiods': subs,
            'n_subperiods': len(subs),
            'subperiods_with_trades': len(with_trades),
            'subperiods_pf_gt_1': sum(1 for s in subs if (s['net_pf'] or 0.0) > 1.0),
            'subperiods_stress_pf_gt_1': sum(
                1 for s in subs if (s['stress_net_pf'] or 0.0) > 1.0),
            'stable': bool(with_trades) and all(
                (s['net_pf'] or 0.0) > 1.0 for s in with_trades),
        })
    return out


def percentile_rank(value: float, distribution: list) -> float:
    """Share of the distribution below a value."""
    if not distribution:
        return None
    below = sum(1 for v in distribution if v is not None and v < value)
    return below / len(distribution)


def fmt_pf(value) -> str:
    """A profit factor, or 'n/a' when there is no loss to divide by."""
    return 'n/a' if value is None else f'{value:.4f}'


def build_verdict(payload: dict) -> list:
    """The plain-language reading of the check."""
    verdict = []
    n_gate = payload['n_gate_cells']
    if n_gate == 0:
        verdict.append('No cell of the child grid clears the §3.4 gate.')
        return verdict
    verdict.append(
        f"{n_gate} of {payload['n_cells']} child cells clear the §3.4 gate, on "
        f"{payload['n_gate_symbols']} symbols: {payload['gate_by_symbol']}.")
    verdict.append(
        f"The family pools to an out-of-sample net PF of "
        f"{fmt_pf(payload['family']['pooled_oos_net_pf'])} over "
        f"{payload['family']['trades']} out-of-sample trades, and the child's "
        f"own cells put {payload['share_of_cells_oos_pf_gt_1'] * 100:.1f} % of "
        f"their out-of-sample scores above PF 1.")
    stable_cells = [s for s in payload.get('subperiod_stability', [])
                    if s.get('stable')]
    stable = len(stable_cells)
    if stable == n_gate:
        verdict.append(
            f"All {n_gate} gate-clearing cells keep a net PF above 1 in every "
            f"out-of-sample sub-period that carries trades.")
    elif stable:
        names = ', '.join(f"{s['symbol']} P{s['P_fast']}_{s['P_slow']}"
                          for s in stable_cells[:5])
        verdict.append(
            f"{stable} of {n_gate} gate-clearing cells keep a net PF above 1 in "
            f"every out-of-sample sub-period that carries trades ({names}); the "
            f"other {n_gate - stable} work in one stretch of time only.")
    else:
        verdict.append(
            f"None of the {n_gate} gate-clearing cells keeps a net PF above 1 in "
            f"every out-of-sample sub-period that carries trades: the family is "
            f"a time artefact.")
    verdict.append(
        'A cell that clears a gate is a selection result, not a promotion: the '
        'family still has to beat its own randomizations (the null leg on the '
        'child grid) and the walk-forward has to hold up on the complete child '
        'grid before anything can be promoted.')
    return verdict


def write_report(out_dir: Path, payload: dict) -> None:
    """Render the human-readable summary of the check."""
    lines = ['# Mutation Survivor Check — the gate-clearing cells of the child grid',
             '',
             f"**Child run:** `{payload['child_run']}`",
             f"**Generated:** {payload['generated_at']}",
             f"**Cells read:** {payload['n_cells']} on {payload['n_symbols']} symbols",
             f"**Gate:** OOS net PF > 1, OOS net PF under {payload['stress_multiplier']:g}x "
             f"costs > 1, >= {payload['min_trades']} OOS trades", '',
             '## Leg 1 — the family', '',
             '| Measure | Value |', '|---|---|',
             f"| Cells read | {payload['n_cells']} |",
             f"| Cells clearing the gate | {payload['n_gate_cells']} |",
             f"| Symbols with a gate-clearing cell | {payload['n_gate_symbols']} |",
             f"| Gate cells per symbol | {payload['gate_by_symbol']} |",
             f"| Pooled OOS net PF of the family | {fmt_pf(payload['family']['pooled_oos_net_pf'])} |",
             f"| Pooled OOS trades of the family | {payload['family']['trades']} |",
             f"| Child cells with OOS net PF > 1 | {payload['n_cells_oos_pf_gt_1']} "
             f"({payload['share_of_cells_oos_pf_gt_1'] * 100:.1f} %) |",
             f"| Child cells clearing the gate | {payload['n_gate_cells']} "
             f"({payload['share_of_cells_clearing_gate'] * 100:.2f} %) |", '']
    lines += ['### The gate-clearing cells', '',
              '| Symbol | Cell | OOS trades | OOS net PF | OOS net PF (2x costs) | '
              'Full-sample net PF | Sub-periods with PF > 1 |',
              '|---|---|---|---|---|---|---|']
    stability = {(s['symbol'], s['P_fast'], s['P_slow']): s
                 for s in payload['subperiod_stability']}
    for row in payload['gate_cells']:
        key = (row['symbol'], row['P_fast'], row['P_slow'])
        sub = stability.get(key)
        subs = (f"{sub['subperiods_pf_gt_1']}/{sub['subperiods_with_trades']}"
                 if sub else 'n/a')
        lines.append(
            f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
            f"{row['oos_trades']} | {row['oos_net_pf']:.4f} | "
            f"{row['oos_stress_net_pf']:.4f} | {row['full_net_pf']:.4f} | {subs} |")
    lines += ['', '## Leg 2 — concentration', '',
              'The pooled out-of-sample profit factor of the family with each '
              'symbol dropped in turn: a family that stands on one symbol is '
              'not a family.', '',
              '| Dropped symbol | Cells left | Gate cells left | Pooled OOS net PF |',
              '|---|---|---|---|']
    for row in payload['leave_one_symbol_out']:
        pf = fmt_pf(row['pooled_oos_net_pf'])
        lines.append(f"| {row['dropped_symbol']} | {row['cells_left']} | "
                     f"{row['gate_cells_left']} | {pf} |")
    lines += ['', '## Leg 3 — sub-period stability', '',
              f"The out-of-sample window of every gate-clearing cell is cut into "
              f"{payload['subperiods']} sequential sub-periods.", '',
             f"**{payload['n_stable_cells']} of {payload['n_gate_cells']}** "
             f"gate-clearing cells keep a net PF above 1 in every sub-period "
             f"that carries trades.", '']
    lines += ['| Symbol | Cell | Sub-periods with PF > 1 | Sub-periods with '
              'trades | Stable |', '|---|---|---|---|---|']
    for sub in payload['subperiod_stability']:
        lines.append(f"| {sub['symbol']} | P{sub['P_fast']}_{sub['P_slow']} | "
                     f"{sub['subperiods_pf_gt_1']} | "
                     f"{sub['subperiods_with_trades']} | "
                     f"{'yes' if sub['stable'] else 'no'} |")
    lines += ['## Verdict', '']
    for item in payload['verdict']:
        lines.append(f'- {item}')
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(
        description='Gate-clearing cells of a mutation child grid and their stability')
    parser.add_argument('--child', type=str, default='results/20261021_172619_grid')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--oos-fraction', type=float, default=0.35)
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--min-trades', type=int, default=30)
    parser.add_argument('--subperiods', type=int, default=4)
    parser.add_argument('--out', type=str, default=None)
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

    child_dir = Path(args.child)
    out_dir = Path(args.out) if args.out else Path(
        f"results/{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"
        f"_mutation_survivor_check")
    out_dir.mkdir(parents=True, exist_ok=True)

    from universe.universe import load_mcap_ranking
    ranking = load_mcap_ranking(args.mcap)
    symbols = complete_symbols(child_dir, ranking)
    print(f'Reading {len(symbols)} complete symbol(s) x '
          f'{len(period_pairs())} pairs.', flush=True)

    rows = cell_rows(child_dir, symbols, args.fixture_base, args.oos_fraction,
                     args.stress_multiplier, args.min_trades)
    gate = [r for r in rows if r['clears_gate']]
    print(f'{len(gate)} cell(s) clear the gate.', flush=True)

    stability = subperiod_stability(child_dir, gate, args.subperiods,
                                    args.stress_multiplier)
    distribution = [r['oos_net_pf'] for r in rows if r['oos_net_pf'] is not None]
    for row in gate:
        row['oos_pf_percentile'] = percentile_rank(row['oos_net_pf'], distribution)

    n_oos_gt_1 = sum(1 for r in rows if (r['oos_net_pf'] or 0.0) > 1.0)
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'child_run': str(child_dir),
        'n_symbols': len(symbols),
        'n_cells': len(rows),
        'oos_fraction': args.oos_fraction,
        'stress_multiplier': args.stress_multiplier,
        'min_trades': args.min_trades,
        'subperiods': args.subperiods,
        'n_gate_cells': len(gate),
        'n_gate_symbols': len({r['symbol'] for r in gate}),
        'gate_by_symbol': dict(Counter(r['symbol'] for r in gate).most_common()),
        'gate_cells': gate,
        'family': family_pooled(gate),
        'leave_one_symbol_out': leave_one_symbol_out(gate),
        'subperiod_stability': stability,
        'n_stable_cells': sum(1 for s in stability if s['stable']),
        'n_cells_oos_pf_gt_1': n_oos_gt_1,
        'share_of_cells_oos_pf_gt_1': n_oos_gt_1 / len(rows) if rows else 0.0,
        'share_of_cells_clearing_gate': len(gate) / len(rows) if rows else 0.0,
    }
    payload['verdict'] = build_verdict(payload)
    payload['artifact'] = str(out_dir)

    with open(out_dir / 'config.json', 'w') as fh:
        json.dump({'args': vars(args)}, fh, indent=2, default=str)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    with open(out_dir / 'cells.jsonl', 'w') as fh:
        for row in rows:
            fh.write(json.dumps(row) + '\n')
    write_report(out_dir, payload)
    print(f'Wrote {out_dir}/summary.md')


if __name__ == '__main__':
    main()
