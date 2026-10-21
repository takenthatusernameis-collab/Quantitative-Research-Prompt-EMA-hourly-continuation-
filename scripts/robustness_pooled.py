#!/usr/bin/env python3
"""Pooled robustness legs for the full EMA grid (PROMPT.md §3.3, §2.1.6).

The grid pipeline already applies the cost-stress and out-of-sample gates
(scripts/candidate_check.py). Two robustness legs required by PROMPT.md §3.3
were still missing over the expanded universe, and this harness adds them
without re-running a backtest or fetching market data - every number is
pooled from the per-cell artifacts the grid run already wrote:

  drop-top-N : does the pooled result depend on the largest market-cap names?
               Pooled net PF over the whole universe compared with the universe
               with the N largest names removed.
  subperiod  : is a cell's edge stable over time? Every cell whose full-sample
               net PF > 1 is split into K chronological subperiods and its net
               PF is recomputed in each one.
  buckets    : pooled net PF and trade counts by market-cap rank bucket and by
               EMA pair (PROMPT.md §2.1.6 reporting requirement).

All figures are net of the registered costs (10 bps taker + 2 bps slippage per
side). Pooling is done on trade-level net P&L: pooled PF = sum(net wins) /
sum(net losses), never a mean of per-cell profit factors.

Usage:
    python scripts/robustness_pooled.py --run results/20261019_135940_grid
    python scripts/robustness_pooled.py --run results/20261019_135940_grid \
        --drop-top 5 10 20 50 --subperiods 4
"""
import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from scripts.run_grid import read_artifact_csv

# A subperiod with fewer trades than this cannot say anything about the sign of
# its profit factor, so it is reported but not counted towards the stability
# verdict.
MIN_TRADES_PER_SUBPERIOD = 5

# The grid runner writes gzip-compressed blotters, but the five largest
# market-cap names (ranks 1-5) still carry the legacy baseline-study layout.
TRADES_FILENAME = 'trades.csv.gz'
LEGACY_TRADES_FILENAME = 'trades.csv'

# Market-cap rank buckets used for the §2.1.6 reporting requirement. The last
# bucket is open-ended and covers every remaining rank.
RANK_BUCKET_EDGES = [(1, 10), (11, 50), (51, 100), (101, 200), (201, None)]


def cell_net_totals(summary: dict) -> tuple:
    """Return (net_win_sum, net_loss_abs, trades) implied by a cell summary.

    A cell summary stores the net average win/loss and the net win rate, so the
    pooled win and loss totals of the cell are recovered exactly instead of
    re-reading the trade blotter.
    """
    trades = int(summary.get('trade_count') or 0)
    win_rate = float(summary.get('net_win_rate') or 0.0)
    avg_win = float(summary.get('net_avg_win') or 0.0)
    avg_loss = float(summary.get('net_avg_loss') or 0.0)
    win_sum = max(avg_win, 0.0) * win_rate * trades
    loss_abs = max(-avg_loss, 0.0) * (1.0 - win_rate) * trades
    return win_sum, loss_abs, trades


def pool(cells: list) -> dict:
    """Pool a list of cells into trade-level net P&L statistics.

    `cells` items are dicts with `win_sum`, `loss_abs` and `trades` keys (see
    `cell_net_totals`). The pooled profit factor is the ratio of summed net
    wins to summed net losses, which is the only correct way to pool cells
    that carry very different trade counts.
    """
    win_sum = sum(c['win_sum'] for c in cells)
    loss_abs = sum(c['loss_abs'] for c in cells)
    trades = sum(c['trades'] for c in cells)
    if loss_abs > 0:
        net_pf = win_sum / loss_abs
    elif win_sum > 0:
        net_pf = float('inf')
    else:
        net_pf = 0.0
    return {
        'n_cells': len(cells),
        'trades': trades,
        'net_win_sum': win_sum,
        'net_loss_abs': loss_abs,
        'net_pnl': win_sum - loss_abs,
        'net_profit_factor': net_pf,
        'net_win_rate': (win_sum / trades) if trades else 0.0,
    }


def load_cells(run_dir: Path) -> list:
    """Read every completed cell summary of a grid run into a flat list."""
    cells = []
    results_root = run_dir / 'results'
    if not results_root.exists():
        return cells
    for sym_dir in sorted(results_root.iterdir()):
        if not sym_dir.is_dir():
            continue
        symbol = sym_dir.name.replace('_', '/')
        for cell_dir in sorted(sym_dir.iterdir()):
            summary_path = cell_dir / 'summary.json'
            if not cell_dir.is_dir() or not summary_path.exists():
                continue
            summary = json.loads(summary_path.read_text())
            if (summary.get('blocked')):
                continue
            win_sum, loss_abs, trades = cell_net_totals(summary)
            cells.append({
                'symbol': symbol,
                'P_fast': int(summary['P_fast']),
                'P_slow': int(summary['P_slow']),
                'trades': trades,
                'win_sum': win_sum,
                'loss_abs': loss_abs,
                'net_profit_factor': float(summary.get('net_profit_factor') or 0.0),
                'sharpe_ratio': float(summary.get('sharpe_ratio') or 0.0),
                'cell_dir': str(cell_dir),
            })
    return cells


def rank_of(symbol: str, order: list) -> int:
    """Market-cap rank (1 = largest) of a symbol in the descending universe."""
    try:
        return order.index(symbol) + 1
    except ValueError:
        return len(order) + 1


def bucket_label(rank: int) -> str:
    """Label of the market-cap rank bucket a rank falls into."""
    for low, high in RANK_BUCKET_EDGES:
        if rank >= low and (high is None or rank <= high):
            return f'{low}-{high}' if high is not None else f'{low}+'
    return 'unknown'


def split_subperiods(entry_times: pd.Series, k: int) -> np.ndarray:
    """Assign each trade to one of `k` chronological subperiods.

    The subperiod edges are spread evenly over the trade timeline of the cell
    itself, so a cell that only covers part of the sample is still split into
    comparable slices of its own history.
    """
    if len(entry_times) == 0:
        return np.zeros(0, dtype=int)
    times = entry_times.astype('int64').to_numpy()
    lo, hi = times.min(), times.max()
    if hi == lo or k <= 1:
        return np.zeros(len(times), dtype=int)
    edges = np.linspace(lo, hi, k + 1)
    idx = np.searchsorted(edges, times, side='right') - 1
    return np.clip(idx, 0, k - 1)


def classify_subperiod(trades: int, net_pf) -> str:
    """Label of one subperiod.

    A slice with fewer than `MIN_TRADES_PER_SUBPERIOD` trades cannot carry a
    reliable profit factor, so it is labelled `thin_win` / `thin_loss` instead
    of being counted as a full observation. A thin slice is still allowed to
    disagree with the rest of the cell: a slice that lost money is evidence
    against a stable edge even when it is underpowered.
    """
    if trades == 0:
        return 'empty'
    positive = net_pf is not None and net_pf > 1.0
    if trades < MIN_TRADES_PER_SUBPERIOD:
        return 'thin_win' if positive else 'thin_loss'
    return 'win' if positive else 'loss'


def subperiod_stats(pnl_net: pd.Series, buckets: np.ndarray, k: int) -> list:
    """Net PF and trade count of every subperiod of one cell."""
    stats = []
    buckets = np.asarray(buckets, dtype=int)
    for i in range(k):
        mask = buckets == i
        pnls = pnl_net[mask]
        trades = int(len(pnls))
        if trades == 0:
            stats.append({'subperiod': i, 'trades': 0, 'net_profit_factor': None,
                          'net_pnl': 0.0, 'class': 'empty'})
            continue
        wins = float(pnls[pnls > 0].sum())
        losses = float(-pnls[pnls < 0].sum())
        if losses > 0:
            pf = wins / losses
        elif wins > 0:
            pf = float('inf')
        else:
            pf = 0.0
        stats.append({'subperiod': i, 'trades': trades, 'net_profit_factor': pf,
                      'net_pnl': wins - losses,
                      'class': classify_subperiod(trades, pf)})
    return stats


def stability_verdict(subperiods: list) -> str:
    """Verdict of the subperiod leg for one cell.

    stable        - every slice that carries trades kept net PF > 1
    fragile       - the slices disagree on the sign of the profit factor
    loss_only     - no slice made money
    insufficient  - too few slices carry enough trades to judge
    no_trades     - the cell never traded
    """
    active = [s for s in subperiods if s['trades'] > 0]
    if not active:
        return 'no_trades'
    evaluable = [s for s in active if s['class'] in ('win', 'loss')]
    if len(evaluable) < 2:
        return 'insufficient'
    positive = [s for s in active if s['class'] in ('win', 'thin_win')]
    negative = [s for s in active if s['class'] in ('loss', 'thin_loss')]
    if not positive:
        return 'loss_only'
    if negative:
        return 'fragile'
    return 'stable'


def read_trades(cell_dir: Path) -> pd.DataFrame:
    """Read one cell's trade blotter.

    The run is not uniform: the five largest market-cap names carry the
    legacy baseline-study layout (`trades.csv`), the rest carry the
    gzip-compressed layout (`trades.csv.gz`). `read_artifact_csv` handles
    both, so the subperiod leg does not skip - or crash on - the top of the
    universe.
    """
    path = Path(cell_dir) / TRADES_FILENAME
    if not path.exists():
        path = Path(cell_dir) / LEGACY_TRADES_FILENAME
    df = read_artifact_csv(path)
    df['entry_time'] = pd.to_datetime(df['entry_time'], utc=True)
    return df


def drop_top_n_legs(cells: list, order: list, drop_sizes: list) -> list:
    """Pooled result for the universe with the N largest names removed."""
    legs = []
    for n in drop_sizes:
        dropped = set(order[:n])
        kept = [c for c in cells if c['symbol'] not in dropped]
        pooled = pool(kept)
        pooled['dropped_n'] = n
        pooled['dropped_symbols'] = [s for s in order[:n]]
        legs.append(pooled)
    return legs


def bucket_legs(cells: list, order: list) -> list:
    """Pooled result per market-cap rank bucket and per EMA pair."""
    by_bucket = defaultdict(list)
    by_pair = defaultdict(list)
    for cell in cells:
        by_bucket[bucket_label(rank_of(cell['symbol'], order))].append(cell)
        by_pair[f"P{cell['P_fast']}_{cell['P_slow']}"].append(cell)
    legs = []
    for label, bucket_cells in by_bucket.items():
        pooled = pool(bucket_cells)
        pooled['bucket'] = label
        pooled['n_symbols'] = len({c['symbol'] for c in bucket_cells})
        legs.append(pooled)
    for label, pair_cells in by_pair.items():
        pooled = pool(pair_cells)
        pooled['pair'] = label
        pooled['n_symbols'] = len({c['symbol'] for c in pair_cells})
        legs.append(pooled)
    return legs


def subperiod_leg(cells: list, k: int) -> list:
    """Subperiod stability for every cell whose full-sample net PF > 1."""
    rows = []
    for cell in cells:
        if cell['net_profit_factor'] <= 1.0:
            continue
        df = read_trades(Path(cell['cell_dir']))
        buckets = split_subperiods(df['entry_time'], k)
        stats = subperiod_stats(df['pnl_net'], buckets, k)
        verdict = stability_verdict(stats)
        rows.append({
            'symbol': cell['symbol'],
            'P_fast': cell['P_fast'],
            'P_slow': cell['P_slow'],
            'trades': cell['trades'],
            'full_sample_net_pf': cell['net_profit_factor'],
            'subperiods': stats,
            'n_subperiods_evaluated': len([s for s in stats
                                           if s['class'] in ('win', 'loss')]),
            'n_subperiods_pf_gt_1': len([s for s in stats
                                         if s['trades'] > 0
                                         and (s['net_profit_factor'] or 0) > 1.0]),
            'n_subperiods_pf_le_1': len([s for s in stats
                                         if s['trades'] > 0
                                         and (s['net_profit_factor'] or 0) <= 1.0]),
            'verdict': verdict,
        })
    return rows


def fmt_pf(value) -> str:
    """Format a profit factor for the markdown report."""
    if value is None:
        return 'n/a'
    if value == float('inf'):
        return 'inf'
    return f'{value:.4f}'


def write_report(out_dir: Path, payload: dict) -> None:
    """Write the human-readable robustness report."""
    lines = []
    lines.append('# Pooled Robustness — EMA Hourly Continuation Grid')
    lines.append('')
    lines.append(f"**Source run:** `{payload['source_run']}`")
    lines.append(f"**Generated:** {payload['generated_at']}")
    lines.append(f"**Universe:** {payload['n_symbols']} symbols, "
                 f"{payload['n_cells']} grid cells (net of costs)")
    lines.append('')

    lines.append('## Leg 1 — Drop the N largest market-cap names')
    lines.append('')
    lines.append('| Universe | Symbols | Trades | Pooled net PF | Pooled net P&L |')
    lines.append('|---|---|---|---|---|')
    full = payload['pooled_full']
    lines.append(f"| all | {payload['n_symbols']} | {full['trades']} | "
                 f"{fmt_pf(full['net_profit_factor'])} | {full['net_pnl']:.0f} |")
    for leg in payload['drop_top_n']:
        lines.append(f"| minus top {leg['dropped_n']} | "
                     f"{payload['n_symbols'] - leg['dropped_n']} | {leg['trades']} | "
                     f"{fmt_pf(leg['net_profit_factor'])} | {leg['net_pnl']:.0f} |")
    lines.append('')
    lines.append('The pooled net PF is a trade-level ratio of summed net wins to '
                 'summed net losses, not a mean of per-cell profit factors.')
    lines.append('')

    lines.append('## Leg 2 — Pooled result by market-cap rank bucket')
    lines.append('')
    lines.append('| Rank bucket | Symbols | Trades | Pooled net PF |')
    lines.append('|---|---|---|---|')
    for leg in payload['buckets']:
        if 'bucket' not in leg:
            continue
        lines.append(f"| {leg['bucket']} | {leg['n_symbols']} | {leg['trades']} | "
                     f"{fmt_pf(leg['net_profit_factor'])} |")
    lines.append('')

    lines.append('## Leg 3 — Subperiod stability of every net PF > 1 cell')
    lines.append('')
    lines.append(f"Subperiods per cell: {payload['subperiods']} (equal-time slices of "
                 "the cell's own trade timeline).")
    lines.append('')
    lines.append('| Symbol | Cell | Trades | Full-sample net PF | Subperiod net PF (trades) | Verdict |')
    lines.append('|---|---|---|---|---|---|')
    for row in payload['subperiod_cells']:
        pfs = ' / '.join(
            ('n/a' if s['net_profit_factor'] is None else fmt_pf(s['net_profit_factor']))
            + f"({s['trades']})"
            for s in row['subperiods'])
        lines.append(f"| {row['symbol']} | P{row['P_fast']}_{row['P_slow']} | "
                     f"{row['trades']} | {fmt_pf(row['full_sample_net_pf'])} | {pfs} | "
                     f"{row['verdict']} |")
    lines.append('')

    verdicts = payload['subperiod_verdict_counts']
    lines.append('Verdict counts: ' + ', '.join(f'{k}={v}' for k, v in verdicts.items())
                 + '.')
    lines.append('')
    lines.append('Verdict rules: `stable` = every slice that carries trades kept net PF > 1; '
                 f'`fragile` = the slices disagree on the sign; `loss_only` = no slice made '
                 f'money; `insufficient` = fewer than two slices carry at least '
                 f'{payload["min_trades_per_subperiod"]} trades.')
    lines.append('')
    lines.append('## Gates (PROMPT.md §3.3, §3.4)')
    lines.append('')
    lines.append(f"- Cells with full-sample net PF > 1: **{payload['n_cells_pf_gt_1']}** "
                 f"of {payload['n_cells']} ({payload['frac_cells_pf_gt_1']:.2%}).")
    lines.append(f"- Cells whose edge is stable in every subperiod: "
                 f"**{payload['n_stable_cells']}**.")
    lines.append(f"- Cells judged fragile across subperiods: "
                 f"**{payload['n_fragile_cells']}**.")
    lines.append(f"- Cells with too few subperiod trades to judge: "
                 f"**{payload['n_insufficient_cells']}**.")
    lines.append(f"- Cells with no subperiod making money: "
                 f"**{payload['n_loss_only_cells']}**.")
    lines.append('- No cell may be promoted on full-sample net PF alone; the OOS and '
                 '2x-cost gates in `scripts/candidate_check.py` apply on top of these legs.')
    lines.append('')
    (out_dir / 'summary.md').write_text('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(
        description='Pooled robustness legs (drop top-N, rank buckets, subperiods)')
    parser.add_argument('--run', type=str, required=True,
                        help='results/<RUNID>_grid directory')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--drop-top', type=int, nargs='*', default=[5, 10, 20, 50],
                        help='Market-cap rank cut-offs to drop from the pooled result')
    parser.add_argument('--subperiods', type=int, default=4)
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    run_dir = Path(args.run)
    cells = load_cells(run_dir)
    if not cells:
        raise SystemExit(f'no completed cells found in {run_dir}')

    mcap = json.loads(Path(args.mcap).read_text())
    order = list(mcap.get('symbols', []))
    for cell in cells:
        if cell['symbol'] not in order:
            order.append(cell['symbol'])

    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    out_dir = Path(args.out) if args.out else Path('results') / f'{timestamp}_robustness'
    out_dir.mkdir(parents=True, exist_ok=True)

    pooled_full = pool(cells)
    drop_legs = drop_top_n_legs(cells, order, args.drop_top)
    bucket_legs_all = bucket_legs(cells, order)
    sub_cells = subperiod_leg(cells, args.subperiods)

    verdict_counts = defaultdict(int)
    for row in sub_cells:
        verdict_counts[row['verdict']] += 1

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_run': str(run_dir),
        'n_symbols': len({c['symbol'] for c in cells}),
        'n_cells': len(cells),
        'subperiods': args.subperiods,
        'min_trades_per_subperiod': MIN_TRADES_PER_SUBPERIOD,
        'pooled_full': pooled_full,
        'drop_top_n': drop_legs,
        'buckets': bucket_legs_all,
        'n_cells_pf_gt_1': sum(1 for c in cells if c['net_profit_factor'] > 1.0),
        'frac_cells_pf_gt_1': (sum(1 for c in cells if c['net_profit_factor'] > 1.0)
                               / len(cells)),
        'subperiod_cells': sub_cells,
        'subperiod_verdict_counts': dict(verdict_counts),
        'n_stable_cells': verdict_counts.get('stable', 0),
        'n_fragile_cells': verdict_counts.get('fragile', 0),
        'n_insufficient_cells': verdict_counts.get('insufficient', 0),
        'n_loss_only_cells': verdict_counts.get('loss_only', 0),
    }

    with open(out_dir / 'summary.json', 'w') as f:
        json.dump(payload, f, indent=2, default=str)
    with open(out_dir / 'config.json', 'w') as f:
        json.dump({
            'timestamp': timestamp,
            'source_run': str(run_dir),
            'mcap': args.mcap,
            'drop_top': args.drop_top,
            'subperiods': args.subperiods,
            'min_trades_per_subperiod': MIN_TRADES_PER_SUBPERIOD,
            'command': (f'PYTHONPATH=. python3 scripts/robustness_pooled.py --run {run_dir} '
                        f'--drop-top {" ".join(str(n) for n in args.drop_top)} '
                        f'--subperiods {args.subperiods}'),
        }, f, indent=2)
    write_report(out_dir, payload)

    print(f'Cells: {payload["n_cells"]} over {payload["n_symbols"]} symbols')
    print(f'Pooled net PF (all): {pooled_full["net_profit_factor"]:.4f} over '
          f'{pooled_full["trades"]} trades')
    for leg in drop_legs:
        print(f'  minus top {leg["dropped_n"]:>3}: net PF '
              f'{leg["net_profit_factor"]:.4f} over {leg["trades"]} trades')
    print(f'Cells with net PF > 1: {payload["n_cells_pf_gt_1"]}')
    print(f'Subperiod verdicts: {dict(verdict_counts)}')
    print(f'Wrote {out_dir}/summary.md and summary.json')


if __name__ == '__main__':
    main()
