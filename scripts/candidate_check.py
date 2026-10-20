#!/usr/bin/env python3
"""Robustness check for grid cells that reached net PF > 1 (PROMPT.md §3.3).

The full EMA grid is an in-sample scan over every (symbol, P_fast, P_slow) cell,
so a cell with net PF > 1 is only a *candidate* until it survives an
out-of-sample window and a cost-stress leg. This harness re-runs the named
cells in four configurations and applies the §3.4 decision gates:

    base      full sample, registered costs (10 bps taker + 2 bps slippage/side)
    oos       trailing `oos_fraction` of the bars, entries restricted to it
    stress    full sample, `stress_multiplier` x fees and slippage
    stress_oos  trailing window, stressed costs

Verdict rules (mirroring scripts/aggregate_grid.py, with the cost-stress gate
applied to both the full sample and the out-of-sample window):
    credible candidate : net OOS PF > 1, net OOS Sharpe > 0, >= 30 OOS trades,
                         and net PF still > 1 under 2x cost stress in both the
                         full sample and the out-of-sample window
    exploratory signal : net OOS PF > 1 and >= 30 OOS trades, but fails one of
                         the robustness gates
    rejected           : everything else (net PF <= 1 or too few trades)

Usage:
    python scripts/candidate_check.py --run results/20261019_135940_grid
    python scripts/candidate_check.py --run results/20261019_135940_grid \
        --cells "JASMY/USDT:20:200" --oos-fraction 0.35

Each finished cell is appended to <out>/rows.jsonl, so a run that is cut short
keeps the cells it already computed and the next invocation resumes from them.
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from data.data_loader import load_ohlcv_csv
from scripts.run_grid import CONFIG_DEFAULTS, run_cell

MIN_TRADES_EXPLORATORY = 30
MIN_TRADES_CREDIBLE = 30
ROWS_FILENAME = 'rows.jsonl'


def load_completed_rows(path: Path) -> dict:
    """Cell results already computed in an earlier, interrupted run.

    Keyed by (symbol, P_fast, P_slow). A truncated trailing line is ignored.
    """
    rows = {}
    if not path.exists():
        return rows
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            rows[(row['symbol'], row['P_fast'], row['P_slow'])] = row
    return rows


def load_candidates(run_dir: Path, explicit: str) -> list:
    """Return [(symbol, P_fast, P_slow)] to check.

    Without --cells, every cell in the run with net PF > 1 is taken from the
    aggregate summary, so the check always covers the current best cells.
    """
    if explicit:
        out = []
        for item in explicit.split(','):
            symbol, fast, slow = item.strip().split(':')
            out.append((symbol.strip(), int(fast), int(slow)))
        return out

    summary_path = run_dir / 'summary.json'
    pooled_best = ''
    if summary_path.exists():
        pooled = json.loads(summary_path.read_text())['pooled']
        pooled_best = f' (pooled best {pooled.get("best_net_pf"):.4f})'
    out = []
    for sym_dir in sorted((run_dir / 'results').iterdir()):
        if not sym_dir.is_dir():
            continue
        symbol = sym_dir.name.replace('_', '/')
        for cell_dir in sorted(sym_dir.iterdir()):
            sp = cell_dir / 'summary.json'
            if not sp.exists():
                continue
            m = json.loads(sp.read_text())
            if (m.get('net_profit_factor') or 0) > 1.0:
                out.append((symbol, m['P_fast'], m['P_slow']))
    print(f'Discovered {len(out)} cell(s) with net PF > 1 in {run_dir}{pooled_best}.')
    return out


def verdict(legs: dict) -> str:
    oos = legs['oos']['metrics']
    stress = legs['stress']['metrics']
    stress_oos = legs['stress_oos']['metrics']
    n_oos = oos.get('trade_count') or 0
    if n_oos < MIN_TRADES_EXPLORATORY:
        return 'rejected'
    if ((oos.get('net_profit_factor') or 0) > 1.0
            and (oos.get('sharpe_ratio') or 0) > 0.0
            and n_oos >= MIN_TRADES_CREDIBLE
            and (stress.get('net_profit_factor') or 0) > 1.0
            and (stress_oos.get('net_profit_factor') or 0) > 1.0):
        return 'credible candidate'
    if (oos.get('net_profit_factor') or 0) > 1.0 and n_oos >= MIN_TRADES_EXPLORATORY:
        return 'exploratory signal'
    return 'rejected'


def main():
    ap = argparse.ArgumentParser(description='OOS + cost-stress check for net PF > 1 grid cells')
    ap.add_argument('--run', type=str, required=True, help='results/<RUNID>_grid directory')
    ap.add_argument('--cells', type=str, default=None,
                    help='Comma-separated "SYMBOL/USDT:fast:slow" list; default = every '
                         'cell in the run with net PF > 1')
    ap.add_argument('--fixture-base', type=str, default='data/fixtures')
    ap.add_argument('--oos-fraction', type=float, default=0.35,
                    help='Trailing out-of-sample fraction of the bars (default 0.35)')
    ap.add_argument('--stress-multiplier', type=float, default=2.0)
    ap.add_argument('--out', type=str, default=None,
                    help='Output dir (default results/<TS>_candidate_check)')
    ap.add_argument('--restart', action='store_true', default=False,
                    help='Ignore a previously written rows.jsonl and recompute every cell')
    args = ap.parse_args()

    run_dir = Path(args.run)
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    out_dir = Path(args.out) if args.out else Path('results') / f'{timestamp}_candidate_check'
    out_dir.mkdir(parents=True, exist_ok=True)

    candidates = load_candidates(run_dir, args.cells)
    if not candidates:
        print('No candidate cells to check.')
        return

    rows_path = out_dir / ROWS_FILENAME
    done = {} if args.restart else load_completed_rows(rows_path)
    if done:
        print(f'Resuming from {rows_path}: {len(done)} cell(s) already computed.')

    cfg = dict(CONFIG_DEFAULTS)
    taker = cfg['taker_fee_bps']
    slip = cfg['slippage_bps']
    stress_taker = taker * args.stress_multiplier
    stress_slip = slip * args.stress_multiplier

    run_config = {
        'timestamp': timestamp,
        'source_run': str(run_dir),
        'oos_fraction': args.oos_fraction,
        'stress_multiplier': args.stress_multiplier,
        'base_costs_bps': {'taker': taker, 'slippage': slip},
        'stress_costs_bps': {'taker': stress_taker, 'slippage': stress_slip},
        'config': cfg,
        'cells': [{'symbol': s, 'P_fast': f, 'P_slow': p} for (s, f, p) in candidates],
    }
    with open(out_dir / 'config.json', 'w') as fh:
        json.dump(run_config, fh, indent=2, default=str)

    rows = []
    with open(rows_path, 'a') as rows_fh:
        for symbol, fast, slow in candidates:
            key = (symbol, fast, slow)
            if key in done:
                rows.append(done[key])
                continue
            fixture = Path(args.fixture_base) / f"{symbol.replace('/', '_')}.csv"
            df = load_ohlcv_csv(str(fixture))
            legs = {}
            legs['base'] = {'metrics': run_cell(symbol, df, fast, slow, taker, slip, cfg['rr'],
                                                cfg['stricter_trend'], cfg['min_risk_atr'],
                                                cfg['atr_threshold'], cfg['conservative_exit'],
                                                oos_fraction=None, sizing=cfg['sizing'],
                                                risk_fraction=cfg['risk_fraction'],
                                                max_notional_multiple=cfg['max_notional_multiple'])[2]}
            legs['oos'] = {'metrics': run_cell(symbol, df, fast, slow, taker, slip, cfg['rr'],
                                               cfg['stricter_trend'], cfg['min_risk_atr'],
                                               cfg['atr_threshold'], cfg['conservative_exit'],
                                               oos_fraction=args.oos_fraction, sizing=cfg['sizing'],
                                               risk_fraction=cfg['risk_fraction'],
                                               max_notional_multiple=cfg['max_notional_multiple'])[2]}
            legs['stress'] = {'metrics': run_cell(symbol, df, fast, slow, stress_taker, stress_slip,
                                                   cfg['rr'], cfg['stricter_trend'], cfg['min_risk_atr'],
                                                   cfg['atr_threshold'], cfg['conservative_exit'],
                                                   oos_fraction=None, sizing=cfg['sizing'],
                                                   risk_fraction=cfg['risk_fraction'],
                                                   max_notional_multiple=cfg['max_notional_multiple'])[2]}
            legs['stress_oos'] = {'metrics': run_cell(symbol, df, fast, slow, stress_taker, stress_slip,
                                                       cfg['rr'], cfg['stricter_trend'], cfg['min_risk_atr'],
                                                       cfg['atr_threshold'], cfg['conservative_exit'],
                                                       oos_fraction=args.oos_fraction, sizing=cfg['sizing'],
                                                       risk_fraction=cfg['risk_fraction'],
                                                       max_notional_multiple=cfg['max_notional_multiple'])[2]}
            label = verdict(legs)
            row = {'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                   'decision_label': label,
                   'legs': {k: v['metrics'] for k, v in legs.items()}}
            rows.append(row)
            done[key] = row
            rows_fh.write(json.dumps(row, default=str) + '\n')
            rows_fh.flush()
            print(f'{symbol} P{fast}_{slow}: base netPF={legs["base"]["metrics"].get("net_profit_factor"):.4f} '
                  f'oos netPF={legs["oos"]["metrics"].get("net_profit_factor"):.4f} '
                  f'(trades {legs["oos"]["metrics"].get("trade_count")}) '
                  f'stress netPF={legs["stress"]["metrics"].get("net_profit_factor"):.4f} '
                  f'-> {label}', flush=True)

    rows.sort(key=lambda r: (r['symbol'], r['P_fast'], r['P_slow']))
    with open(out_dir / 'summary.json', 'w') as fh:
        json.dump({'run_config': run_config, 'cells': rows}, fh, indent=2, default=str)

    lines = ['# Candidate Check — OOS + Cost Stress for net PF > 1 Grid Cells\n']
    lines.append(f'**Source run:** `{run_dir}`')
    lines.append(f'**OOS fraction:** trailing {args.oos_fraction:.0%} of bars')
    lines.append(f'**Cost stress:** {args.stress_multiplier:g}x fees and slippage')
    lines.append(f'**Base costs:** {taker:g} bps taker + {slip:g} bps slippage per side\n')
    lines.append('| Symbol | Cell | Label | Base PF | Base Sharpe | OOS PF | OOS Sharpe | OOS trades | Stress PF | Stress OOS PF |')
    lines.append('|---|---|---|---|---|---|---|---|---|---|')
    for r in rows:
        b, o, s, so = (r['legs']['base'], r['legs']['oos'],
                       r['legs']['stress'], r['legs']['stress_oos'])
        lines.append(
            f'| {r["symbol"]} | P{r["P_fast"]}_{r["P_slow"]} | {r["decision_label"]} | '
            f'{b.get("net_profit_factor"):.4f} | {b.get("sharpe_ratio"):.4f} | '
            f'{o.get("net_profit_factor"):.4f} | {o.get("sharpe_ratio"):.4f} | '
            f'{o.get("trade_count")} | {s.get("net_profit_factor"):.4f} | '
            f'{so.get("net_profit_factor"):.4f} |')
    lines.append('\nDecision gates (PROMPT.md §3.4): credible candidate = net OOS PF > 1, '
                 'net OOS Sharpe > 0, >= 30 OOS trades, and net PF still > 1 under the cost stress.\n')
    with open(out_dir / 'summary.md', 'w') as fh:
        fh.write('\n'.join(lines).rstrip('\n') + '\n')

    print(f'\nWrote {out_dir}/summary.json and {out_dir}/summary.md')


if __name__ == '__main__':
    main()
