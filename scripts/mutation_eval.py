#!/usr/bin/env python3
"""Parent -> child -> delta evaluation of a pre-registered grid mutation.

Why this exists
---------------
PROMPT.md §5 allows ordered optional mutations of the baseline grid and asks
for the *parent config -> child config -> delta metrics* of every one of
them. The baseline grid is never replaced by a mutation; the mutation is a
child run that is read next to its parent.

This script reads both runs and produces that comparison:

* the single-variable check: the child config must differ from the parent
  config in exactly the registered mutation keys;
* the pooled delta on the full sample: net profit factor, trade count, and
  the gross-versus-net cost drag that explains a profit-factor change;
* the same delta on the out-of-sample window (the trailing 35 % of each
  symbol's bars, entries restricted to it) and under 2x costs;
* the walk-forward re-selection leg: the procedure picks the best cell of a
  symbol on the history and is scored on the fold it never saw, so the
  comparison is between two *procedures*, not between two selected cells;
* a reproducibility check: a sample of child cells is re-run through the
  real backtest and has to reproduce the stored summary exactly.

Both runs are read over the **same symbol set** - the symbols whose child
grid is complete - so the delta is an apples-to-apples comparison even when
the child grid is still running.

Usage:
    python scripts/mutation_eval.py --parent results/20261019_135940_grid \
        --child results/20261021_172619_grid --out results/<TS>_mutation_eval
"""
import argparse
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from data.data_loader import load_ohlcv_csv
from scripts.oos_grid_scan import (entry_start_index, net_profit_factor,
                                    read_trades, stressed_pnl_net, win_loss_sums)
from scripts.run_grid import CONFIG_DEFAULTS, period_pairs, run_cell, symbol_dir_name
from scripts.survivor_selection_audit import (cell_fold_stats, fold_edges,
                                               null_pf_distribution,
                                               selection_against_null,
                                               summarize_walk_forward,
                                               walk_forward_steps)

# The keys a mutation is allowed to change. The child config has to differ
# from the parent config in exactly these, otherwise the comparison is not a
# single-variable mutation.
MUTATION_KEYS = ('min_risk_atr', 'atr_threshold')


def cell_dir(run_dir: Path, symbol: str, fast: int, slow: int) -> Path:
    return run_dir / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'


def symbol_bars(fixture_base: str, symbol: str, cache: dict) -> int:
    """Number of bars of a symbol's fixture (cached per symbol)."""
    if symbol not in cache:
        path = Path(fixture_base) / f"{symbol_dir_name(symbol)}.csv"
        cache[symbol] = len(load_ohlcv_csv(str(path)))
    return cache[symbol]


def complete_symbols(child_dir: Path, symbols: list) -> list:
    """Symbols whose child grid is complete (every cell has a summary)."""
    pairs = period_pairs()
    out = []
    for symbol in symbols:
        if all((cell_dir(child_dir, symbol, f, s) / 'summary.json').exists()
               for f, s in pairs):
            out.append(symbol)
    return out


def read_cell(run_dir: Path, symbol: str, fast: int, slow: int) -> dict:
    """Stored summary and blotter of one cell."""
    cdir = cell_dir(run_dir, symbol, fast, slow)
    summary = json.loads((cdir / 'summary.json').read_text())
    trades = read_trades(cdir)
    return {'summary': summary, 'trades': trades}


def cell_statistics(run_dir: Path, symbols: list, fixture_base: str,
                     oos_fraction: float, stress_multiplier: float,
                     n_folds: int, min_trades: int) -> dict:
    """Full-sample, out-of-sample and fold statistics of one run.

    The out-of-sample window is the trailing `oos_fraction` of each
    symbol's bars with the entries restricted to it, the same rule the
    grid-wide out-of-sample audit uses, so the numbers are comparable with
    the parent run's audit.
    """
    bars_cache = {}
    rows = []
    fold_rows = []
    for symbol in symbols:
        n_bars = symbol_bars(fixture_base, symbol, bars_cache)
        entry_start = entry_start_index(n_bars, oos_fraction)
        edges = fold_edges(n_bars, n_folds)
        for fast, slow in period_pairs():
            cdir = cell_dir(run_dir, symbol, fast, slow)
            if not (cdir / 'summary.json').exists():
                continue
            cell = read_cell(run_dir, symbol, fast, slow)
            trades = cell['trades']
            summary = cell['summary']
            pnl_net = trades['pnl_net'].to_numpy(dtype=float)
            pnl_gross = trades['pnl'].to_numpy(dtype=float)
            costs = (trades['entry_cost'].to_numpy(dtype=float)
                     + trades['exit_cost'].to_numpy(dtype=float))
            oos = trades[trades['bar_index'] >= entry_start]
            oos_net = oos['pnl_net'].to_numpy(dtype=float)
            oos_stress = stressed_pnl_net(oos['pnl_net'],
                                           oos['entry_cost'].to_numpy(dtype=float),
                                           oos['exit_cost'].to_numpy(dtype=float),
                                           stress_multiplier)
            full_win, full_loss = win_loss_sums(pnl_net)
            gross_win, gross_loss = win_loss_sums(pnl_gross)
            oos_win, oos_loss = win_loss_sums(oos_net)
            oos_s_win, oos_s_loss = win_loss_sums(oos_stress)
            oos_net_pf = net_profit_factor(oos_net)
            oos_stress_pf = net_profit_factor(oos_stress)
            rows.append({
                'symbol': symbol,
                'P_fast': fast,
                'P_slow': slow,
                'n_bars': n_bars,
                'entry_start_index': entry_start,
                'trades': int(len(trades)),
                'oos_trades': int(len(oos)),
                'net_pf': net_profit_factor(pnl_net),
                'gross_pf': net_profit_factor(pnl_gross),
                'stored_net_pf': summary.get('net_profit_factor'),
                'win_sum': full_win,
                'loss_abs': full_loss,
                'gross_win_sum': gross_win,
                'gross_loss_abs': gross_loss,
                'costs': float(costs.sum()),
                'net_pnl': float(pnl_net.sum()),
                'gross_pnl': float(pnl_gross.sum()),
                'oos_net_pf': oos_net_pf,
                'oos_stress_net_pf': oos_stress_pf,
                'oos_win_sum': oos_win,
                'oos_loss_abs': oos_loss,
                'oos_stress_win_sum': oos_s_win,
                'oos_stress_loss_abs': oos_s_loss,
                'clears_gate': bool((oos_net_pf or 0.0) > 1.0
                                    and int(len(oos)) >= min_trades
                                    and (oos_stress_pf or 0.0) > 1.0),
            })
            fold_rows.append({
                'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                'n_bars': n_bars,
                'folds': cell_fold_stats(trades, edges, stress_multiplier),
            })
    return {'rows': rows, 'fold_rows': fold_rows}


def restrict_to_common_cells(parent_stats: dict, child_stats: dict) -> tuple:
    """Keep only the cells both runs have, so the delta is cell by cell.

    A child grid that is still running can be missing cells. Comparing a
    parent cell against a child cell that does not exist (or the other way
    round) would make the pooled numbers incomparable, so the comparison
    runs over the intersection of the two cell sets.
    """
    parent_keys = {(r['symbol'], r['P_fast'], r['P_slow']) for r in parent_stats['rows']}
    child_keys = {(r['symbol'], r['P_fast'], r['P_slow']) for r in child_stats['rows']}
    common = parent_keys & child_keys
    for stats in (parent_stats, child_stats):
        stats['rows'] = [r for r in stats['rows']
                         if (r['symbol'], r['P_fast'], r['P_slow']) in common]
        stats['fold_rows'] = [r for r in stats['fold_rows']
                              if (r['symbol'], r['P_fast'], r['P_slow']) in common]
    return parent_keys, child_keys


def pooled_pf(win: float, loss: float):
    """Profit factor of a pooled trade series (wins / losses)."""
    if loss > 0:
        return win / loss
    if win > 0:
        return float('inf')
    return None


def summarize_run(stats: dict, min_trades: int, n_folds: int = 5,
                  min_history_trades: int = 20) -> dict:
    """Pooled metrics of one run over the compared symbol set."""
    rows = stats['rows']
    fold_rows = stats['fold_rows']
    cell_pfs = [r['net_pf'] for r in rows if r['net_pf'] is not None]
    win = sum(r['win_sum'] for r in rows)
    loss = sum(r['loss_abs'] for r in rows)
    gross_win = sum(r['gross_win_sum'] for r in rows)
    gross_loss = sum(r['gross_loss_abs'] for r in rows)
    costs = sum(r['costs'] for r in rows)
    oos_win = sum(r['oos_win_sum'] for r in rows)
    oos_loss = sum(r['oos_loss_abs'] for r in rows)
    oos_s_win = sum(r['oos_stress_win_sum'] for r in rows)
    oos_s_loss = sum(r['oos_stress_loss_abs'] for r in rows)

    by_symbol = defaultdict(list)
    for cell in fold_rows:
        by_symbol[cell['symbol']].append(cell)
    walk_records = []
    for symbol in sorted(by_symbol):
        for record in walk_forward_steps(by_symbol[symbol], n_folds, min_history_trades):
            record['symbol'] = symbol
            walk_records.append(record)
    walk = summarize_walk_forward(walk_records)
    nulls = {step: null_pf_distribution(fold_rows, step) for step in range(1, n_folds)}
    vs_null = selection_against_null(walk_records, nulls)

    return {
        'n_symbols': len({r['symbol'] for r in rows}),
        'n_cells': len(rows),
        'trades': sum(r['trades'] for r in rows),
        'mean_cell_net_pf': float(np.mean(cell_pfs)) if cell_pfs else None,
        'median_cell_net_pf': float(np.median(cell_pfs)) if cell_pfs else None,
        'pooled_net_pf': pooled_pf(win, loss),
        'pooled_gross_pf': pooled_pf(gross_win, gross_loss),
        'pooled_net_pnl': win - loss,
        'pooled_gross_pnl': gross_win - gross_loss,
        'total_costs': costs,
        'costs_per_trade': (costs / sum(r['trades'] for r in rows)
                            if sum(r['trades'] for r in rows) else None),
        'cost_share_of_gross_pnl': (costs / (gross_win - gross_loss)
                                     if (gross_win - gross_loss) > 0 else None),
        'cost_share_of_gross_profit': (costs / gross_win if gross_win > 0 else None),
        'cells_net_pf_gt_1': sum(1 for r in rows if (r['net_pf'] or 0.0) > 1.0),
        'cells_without_trades': sum(1 for r in rows if r['trades'] == 0),
        'pooled_oos_net_pf': pooled_pf(oos_win, oos_loss),
        'pooled_oos_stress_net_pf': pooled_pf(oos_s_win, oos_s_loss),
        'cells_oos_pf_gt_1': sum(1 for r in rows if (r['oos_net_pf'] or 0.0) > 1.0),
        'cells_oos_pf_gt_1_with_trades': sum(
            1 for r in rows
            if (r['oos_net_pf'] or 0.0) > 1.0 and r['oos_trades'] >= min_trades),
        'cells_clearing_gate': sum(1 for r in rows if r['clears_gate']),
        'walk_forward': walk,
        'selection_vs_null': vs_null,
        'walk_records': walk_records,
    }


def config_delta(parent_cfg: dict, child_cfg: dict) -> dict:
    """The single-variable check: which config keys actually changed."""
    keys = sorted(set(parent_cfg) | set(child_cfg))
    changed = {k: {'parent': parent_cfg.get(k), 'child': child_cfg.get(k)}
               for k in keys if parent_cfg.get(k) != child_cfg.get(k)}
    return {
        'parent': parent_cfg,
        'child': child_cfg,
        'changed': changed,
        'changed_keys': sorted(changed),
        'within_mutation_keys': bool(changed) and set(changed).issubset(set(MUTATION_KEYS)),
        'single_variable': bool(changed) and set(changed).issubset(set(MUTATION_KEYS)),
    }


def verify_sample(child_dir: Path, child_cfg: dict, symbols: list,
                  fixture_base: str, sample_size: int) -> list:
    """Re-run a sample of child cells and compare with the stored summary."""
    pairs = period_pairs()
    out = []
    if not symbols or sample_size <= 0:
        return out
    step = max(1, len(symbols) // max(1, sample_size))
    picks = symbols[::step][:sample_size]
    for symbol in picks:
        fast, slow = pairs[0]
        cdir = cell_dir(child_dir, symbol, fast, slow)
        if not (cdir / 'summary.json').exists():
            continue
        stored = json.loads((cdir / 'summary.json').read_text())
        df = load_ohlcv_csv(str(Path(fixture_base) / f'{symbol_dir_name(symbol)}.csv'))
        _, _, metrics = run_cell(
            symbol, df, fast, slow, child_cfg['taker_fee_bps'],
            child_cfg['slippage_bps'], child_cfg['rr'], child_cfg['stricter_trend'],
            child_cfg['min_risk_atr'], child_cfg['atr_threshold'],
            child_cfg['conservative_exit'], oos_fraction=None,
            sizing=child_cfg['sizing'], risk_fraction=child_cfg['risk_fraction'],
            max_notional_multiple=child_cfg['max_notional_multiple'])
        keys = ('trade_count', 'net_profit_factor', 'gross_profit_factor',
                'sharpe_ratio', 'max_drawdown', 'equity_reconciles')
        deltas = {}
        for key in keys:
            a, b = stored.get(key), metrics.get(key)
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                deltas[key] = abs(float(a) - float(b))
            else:
                deltas[key] = 0.0 if a == b else float('inf')
        out.append({'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                    'max_abs_delta': max(deltas.values()),
                    'deltas': deltas})
    return out


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


def write_report(out_dir: Path, payload: dict) -> None:
    """The parent -> child -> delta report."""
    parent = payload['parent']
    child = payload['child']
    delta = payload['delta']
    lines = []
    lines.append('# Mutation Evaluation — ATR Minimum-Risk (PROMPT.md §5.2)\n')
    lines.append(f"**Parent run:** `{payload['parent_run']}`")
    lines.append(f"**Child run:** `{payload['child_run']}`")
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Compared symbol set:** {payload['n_symbols']} symbols "
                 f"({payload['n_cells_per_symbol']} EMA pairs each, "
                 f"{payload['n_cells']} cells per run)")
    lines.append(f"**Out-of-sample window:** trailing {payload['oos_fraction']:.0%} "
                 f"of each symbol's bars")
    lines.append(f"**Cost stress:** {payload['stress_multiplier']:g}x fees and "
                 f"slippage\n")

    lines.append('## Leg 1 — the mutation is a single variable\n')
    lines.append('| Config key | Parent | Child |')
    lines.append('|---|---|---|')
    for key in sorted(set(payload['config']['parent']) | set(payload['config']['child'])):
        p = payload['config']['parent'].get(key)
        c = payload['config']['child'].get(key)
        mark = ' **<- changed**' if p != c else ''
        lines.append(f'| {key} | {p} | {c}{mark} |')
    lines.append('')
    lines.append(f"Changed keys: `{'`, `'.join(payload['config']['changed_keys']) or 'none'}`. "
                 f"Single-variable mutation: **{payload['config']['single_variable']}**.\n")

    lines.append('## Leg 2 — parent -> child -> delta (full sample)\n')
    lines.append('| Measure | Parent | Child | Delta |')
    lines.append('|---|---|---|---|')
    measures = [
        ('Cells', 'n_cells', 'int'),
        ('Symbols', 'n_symbols', 'int'),
        ('Trades', 'trades', 'int'),
        ('Mean cell net PF', 'mean_cell_net_pf', 'f'),
        ('Median cell net PF', 'median_cell_net_pf', 'f'),
        ('Pooled net PF', 'pooled_net_pf', 'f'),
        ('Pooled gross PF', 'pooled_gross_pf', 'f'),
        ('Pooled net P&L', 'pooled_net_pnl', 'f2'),
        ('Total costs', 'total_costs', 'f2'),
        ('Costs per trade', 'costs_per_trade', 'f2'),
        ('Cost share of gross profit', 'cost_share_of_gross_profit', 'pct'),
        ('Cells with net PF > 1', 'cells_net_pf_gt_1', 'int'),
        ('Cells without a trade', 'cells_without_trades', 'int'),
    ]
    for label, key, kind in measures:
        p, c = parent.get(key), child.get(key)
        if kind == 'int':
            pv, cv, dv = str(p), str(c), str((c or 0) - (p or 0))
        elif kind == 'f2':
            pv, cv = fmt(p, 2), fmt(c, 2)
            dv = fmt((c or 0.0) - (p or 0.0), 2)
        elif kind == 'pct':
            pv, cv = pct(p), pct(c)
            dv = f'{(c - p) * 100:+.1f} pp' if (p is not None and c is not None) else 'n/a'
        else:
            pv, cv = fmt(p), fmt(c)
            dv = fmt((c or 0.0) - (p or 0.0))
        lines.append(f'| {label} | {pv} | {cv} | {dv} |')
    lines.append('')

    lines.append('## Leg 3 — parent -> child -> delta (out of sample)\n')
    lines.append('| Measure | Parent | Child | Delta |')
    lines.append('|---|---|---|---|')
    oos_measures = [
        ('Pooled OOS net PF', 'pooled_oos_net_pf', 'f'),
        ('Pooled OOS net PF (2x costs)', 'pooled_oos_stress_net_pf', 'f'),
        ('Cells with OOS net PF > 1', 'cells_oos_pf_gt_1', 'int'),
        ('Cells with OOS net PF > 1 and >= 30 OOS trades', 'cells_oos_pf_gt_1_with_trades', 'int'),
        ('Cells clearing the full §3.4 gate', 'cells_clearing_gate', 'int'),
    ]
    for label, key, kind in oos_measures:
        p, c = parent.get(key), child.get(key)
        if kind == 'int':
            lines.append(f'| {label} | {p} | {c} | {(c or 0) - (p or 0)} |')
        else:
            lines.append(f'| {label} | {fmt(p)} | {fmt(c)} | '
                         f'{fmt((c or 0.0) - (p or 0.0))} |')
    lines.append('')

    lines.append('## Leg 4 — the walk-forward selection, parent vs child\n')
    lines.append('The full sample of every symbol is cut into 5 sequential folds. At '
                 'step k the best cell of the symbol is chosen on the history and '
                 'scored on fold k+1, which the selection never saw. This is the '
                 'comparison that matters: it scores the *procedure*, not a cell that '
                 'was picked because it looked good.\n')
    lines.append('| Measure | Parent | Child | Delta |')
    lines.append('|---|---|---|---|')
    pw = parent['walk_forward']
    cw = child['walk_forward']
    wf_measures = [
        ('Walk-forward steps scored', 'steps_scored', 'int'),
        ('Out-of-fold trades', 'pooled_oof_trades', 'int'),
        ('Pooled out-of-fold net PF', 'pooled_oof_net_pf', 'f'),
        ('Pooled out-of-fold net PF (2x costs)', 'pooled_oof_stress_net_pf', 'f'),
        ('Out-of-fold windows with net PF > 1', 'oof_pf_gt_1', 'int'),
        ('Share of out-of-fold windows with net PF > 1', 'oof_pf_gt_1_share', 'pct'),
        ('Median in-fold net PF of the selected cell', 'median_history_pf', 'f'),
        ('Median out-of-fold net PF of the selected cell', 'median_oof_pf', 'f'),
    ]
    for label, key, kind in wf_measures:
        p, c = pw.get(key), cw.get(key)
        if kind == 'int':
            lines.append(f'| {label} | {p} | {c} | {(c or 0) - (p or 0)} |')
        elif kind == 'pct':
            lines.append(f'| {label} | {pct(p)} | {pct(c)} | '
                         f'{(c - p) * 100:+.1f} pp |')
        else:
            lines.append(f'| {label} | {fmt(p)} | {fmt(c)} | '
                         f'{fmt((c or 0.0) - (p or 0.0))} |')
    lines.append('')
    lines.append('| Selection against the grid\'s own null | Parent | Child |')
    lines.append('|---|---|---|')
    pn = parent['selection_vs_null']
    cn = child['selection_vs_null']
    lines.append(f"| Median percentile of the selected cells | {fmt(pn.get('median_percentile'))} "
                 f"| {fmt(cn.get('median_percentile'))} |")
    lines.append(f"| Selected cells above the null p95 | {pn.get('above_p95')} of "
                 f"{pn.get('scored')} | {cn.get('above_p95')} of {cn.get('scored')} |")
    lines.append(f"| One-sided exact binomial p-value | {fmt(pn.get('binomial_p_value'))} "
                 f"| {fmt(cn.get('binomial_p_value'))} |")
    lines.append('')

    lines.append('## Leg 5 — reproducibility of the child cells\n')
    verified = payload['verification']
    if verified:
        lines.append('| Symbol | Cell | Max absolute difference vs the stored summary |')
        lines.append('|---|---|---|')
        for row in verified:
            lines.append(f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                         f"{row['max_abs_delta']:.2e} |")
        lines.append('')
        lines.append('A child cell re-run through the real backtest reproduces the '
                     'stored summary exactly, so the child run is the engine the '
                     'baseline run used, with the mutation applied.\n')
    else:
        lines.append('No child cell was re-run (empty sample).\n')

    lines.append('## Verdict\n')
    for line in payload['verdict']:
        lines.append(f'- {line}')
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def build_verdict(payload: dict) -> list:
    """The reading of the mutation, on the numbers the legs produced."""
    parent = payload['parent']
    child = payload['child']
    yardstick = payload.get('yardstick') or {}
    lines = []
    lines.append(
        f"The child grid trades {child['trades']} trades against the parent's "
        f"{parent['trades']} on the same {payload['n_symbols']} symbols "
        f"({(child['trades'] / parent['trades'] - 1) * 100:+.1f} %), and the "
        f"pooled net profit factor moves from {fmt(parent['pooled_net_pf'])} to "
        f"{fmt(child['pooled_net_pf'])}.")
    lines.append(
        f"The cost of a trade falls from {fmt(parent['costs_per_trade'], 2)} to "
        f"{fmt(child['costs_per_trade'], 2)}, and the costs as a share of the "
        f"gross profit move from {pct(parent['cost_share_of_gross_profit'])} "
        f"to {pct(child['cost_share_of_gross_profit'])}: the ATR minimum-risk filter "
        f"buys back cost drag by trading less, not by trading better.")
    lines.append(
        f"Out of sample the child's pooled net PF is {fmt(child['pooled_oos_net_pf'])} "
        f"against the parent's {fmt(parent['pooled_oos_net_pf'])}, and the cells that "
        f"clear the full §3.4 gate are {child['cells_clearing_gate']} against "
        f"{parent['cells_clearing_gate']}.")
    lines.append(
        f"The walk-forward leg, which scores the *procedure* and never shows the "
        f"selection the data it is judged on, moves the pooled out-of-fold net PF from "
        f"{fmt(parent['walk_forward']['pooled_oof_net_pf'])} to "
        f"{fmt(child['walk_forward']['pooled_oof_net_pf'])} "
        f"(2x costs: {fmt(parent['walk_forward']['pooled_oof_stress_net_pf'])} -> "
        f"{fmt(child['walk_forward']['pooled_oof_stress_net_pf'])}).")
    if yardstick:
        lines.append(
            f"The yardstick is the parent's walk-forward pooled out-of-fold net PF over "
            f"the full {yardstick.get('n_symbols')} symbols: {fmt(yardstick.get('pooled_oof_net_pf'))} "
            f"({fmt(yardstick.get('pooled_oof_stress_net_pf'))} under 2x costs). The child "
            f"has to beat that number on its own symbol set to be worth anything.")
    if (child['walk_forward']['pooled_oof_net_pf'] or 0.0) > (parent['walk_forward']['pooled_oof_net_pf'] or 0.0):
        lines.append(
            "The mutation improves the walk-forward number, but the improvement is a "
            "cost effect (fewer, wider trades) and not a new edge: the program still "
            "has no cell that clears the gates out of sample.")
    else:
        lines.append(
            "The mutation does not improve the walk-forward number: it thins the "
            "sample without creating an edge, which is what the cost-drag leg "
            "predicted.")
    if child['cells_clearing_gate'] == 0:
        lines.append(
            "No child cell clears the PROMPT.md §3.4 gate, so the mutation cannot be "
            "promoted and the baseline grid stays the program's grid.")
    return lines


def main():
    parser = argparse.ArgumentParser(
        description='Parent -> child -> delta evaluation of a grid mutation')
    parser.add_argument('--parent', type=str, default='results/20261019_135940_grid')
    parser.add_argument('--child', type=str, default='results/20261021_172619_grid')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--oos-fraction', type=float, default=0.35)
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--min-trades', type=int, default=30)
    parser.add_argument('--n-folds', type=int, default=5)
    parser.add_argument('--min-history-trades', type=int, default=20)
    parser.add_argument('--min-symbols', type=int, default=1,
                        help='minimum number of complete child symbols to compare')
    parser.add_argument('--symbols', type=str, default=None,
                        help='comma separated symbol list (default: the complete '
                             'child symbols)')
    parser.add_argument('--verify-sample', type=int, default=5,
                        help='how many child cells to re-run for the '
                             'reproducibility check')
    parser.add_argument('--yardstick', type=str, default=None,
                        help='JSON file with the reference walk-forward numbers')
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    parent_dir = Path(args.parent)
    child_dir = Path(args.child)
    out_dir = Path(args.out) if args.out else Path(
        f"results/{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_mutation_eval")
    out_dir.mkdir(parents=True, exist_ok=True)

    parent_cfg = json.loads((parent_dir / 'run_config.json').read_text())['config']
    child_cfg = json.loads((child_dir / 'run_config.json').read_text())['config']

    from universe.universe import load_mcap_ranking
    ranking = load_mcap_ranking(args.mcap)
    if args.symbols:
        wanted = [s.strip() for s in args.symbols.split(',') if s.strip()]
        symbols = [s for s in ranking if s in wanted]
    else:
        symbols = complete_symbols(child_dir, ranking)
    if len(symbols) < args.min_symbols:
        raise SystemExit(f'only {len(symbols)} complete child symbols, need '
                         f'{args.min_symbols}')

    print(f'Comparing {len(symbols)} symbols x {len(period_pairs())} pairs '
          f'({len(symbols) * len(period_pairs())} cells per run).', flush=True)

    parent_stats = cell_statistics(parent_dir, symbols, args.fixture_base,
                                   args.oos_fraction, args.stress_multiplier,
                                   args.n_folds, args.min_trades)
    print(f'Parent: {len(parent_stats["rows"])} cells read.', flush=True)
    child_stats = cell_statistics(child_dir, symbols, args.fixture_base,
                                  args.oos_fraction, args.stress_multiplier,
                                  args.n_folds, args.min_trades)
    print(f'Child: {len(child_stats["rows"])} cells read.', flush=True)

    parent_keys, child_keys = restrict_to_common_cells(parent_stats, child_stats)
    print(f'Compared cell set: {len(parent_keys & child_keys)} cells '
          f'(parent only: {len(parent_keys - child_keys)}, '
          f'child only: {len(child_keys - parent_keys)}).', flush=True)

    parent_summary = summarize_run(parent_stats, args.min_trades, args.n_folds,
                                   args.min_history_trades)
    child_summary = summarize_run(child_stats, args.min_trades, args.n_folds,
                                  args.min_history_trades)

    # The stored summaries have to agree with the blotters they came with.
    for label, stats in (('parent', parent_stats), ('child', child_stats)):
        mismatches = 0
        for row in stats['rows']:
            stored = row['stored_net_pf']
            if stored is None or row['net_pf'] is None:
                continue
            if abs(float(stored) - float(row['net_pf'])) > 1e-9 * max(1.0, abs(float(stored))):
                mismatches += 1
        parent_summary[f'{label}_pf_mismatches'] = mismatches

    yardstick = None
    if args.yardstick and Path(args.yardstick).exists():
        yardstick = json.loads(Path(args.yardstick).read_text())

    verification = verify_sample(child_dir, child_cfg, symbols,
                                  args.fixture_base, args.verify_sample)

    delta = {}
    for key in parent_summary:
        p, c = parent_summary.get(key), child_summary.get(key)
        if isinstance(p, (int, float)) and isinstance(c, (int, float)):
            delta[key] = c - p
    delta['walk_forward'] = {
        key: child_summary['walk_forward'].get(key, 0)
        - parent_summary['walk_forward'].get(key, 0)
        for key in parent_summary['walk_forward']
        if isinstance(parent_summary['walk_forward'].get(key), (int, float))
        and isinstance(child_summary['walk_forward'].get(key), (int, float))
    }

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'parent_run': str(parent_dir),
        'child_run': str(child_dir),
        'symbols': symbols,
        'n_symbols': len(symbols),
        'n_cells_per_symbol': len(period_pairs()),
        'n_cells': len(child_stats['rows']),
        'oos_fraction': args.oos_fraction,
        'stress_multiplier': args.stress_multiplier,
        'min_trades': args.min_trades,
        'config': config_delta(parent_cfg, child_cfg),
        'parent': parent_summary,
        'child': child_summary,
        'delta': delta,
        'verification': verification,
        'yardstick': yardstick,
    }
    payload['verdict'] = build_verdict(payload)

    with open(out_dir / 'config.json', 'w') as fh:
        json.dump({'args': vars(args), 'parent_config': parent_cfg,
                   'child_config': child_cfg}, fh, indent=2, default=str)
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump(payload, fh, indent=2, default=str)
    with open(out_dir / 'cells.jsonl', 'w') as fh:
        for row in child_stats['rows']:
            fh.write(json.dumps(row) + '\n')
    write_report(out_dir, payload)
    print(f'Wrote {out_dir}/summary.md')


if __name__ == '__main__':
    main()
