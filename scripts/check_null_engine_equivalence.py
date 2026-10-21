#!/usr/bin/env python3
"""Equivalence check for the randomized-entry null on the two backtest engines.

The null leg has to be run on the child grid (the pre-registered ATR
minimum-risk mutation), and the child grid is 17 556 cells - too many for
the research engine inside one session. The array twin
`backtest_symbol_fast` is the proved equivalent of the research path, but the
null leg is not a grid cell: it replaces the entry set and re-runs the
engine. This script re-runs the *same* null cells on both engines and
compares the two results field by field, so the fast null is a measured
equivalence rather than an assumed one.

Usage:
    PYTHONPATH=. python3 scripts/check_null_engine_equivalence.py \
        --run results/20261021_125403_grid --cells 6
"""
import argparse
import json
import time
from pathlib import Path

from data.data_loader import load_ohlcv_csv
from scripts.null_grid_scan import process_cell
from scripts.run_grid import run_config


def main():
    parser = argparse.ArgumentParser(
        description='Reference vs fast engine on the randomized-entry null')
    parser.add_argument('--run', type=str, required=True)
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--oos-fraction', type=float, default=0.35)
    parser.add_argument('--stress-multiplier', type=float, default=2.0)
    parser.add_argument('--min-trades', type=int, default=30)
    parser.add_argument('--modes', type=str, nargs='*', default=['block', 'timing', 'sign'])
    parser.add_argument('--cells', type=int, default=6)
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    run_dir = Path(args.run)
    config = run_config(run_dir)
    config['stress_multiplier'] = args.stress_multiplier

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
        if len(cells) >= args.cells:
            break
    cells = cells[:args.cells]

    rows = []
    for symbol, fast, slow in cells:
        df = load_ohlcv_csv(str(Path(args.fixture_base) / f"{symbol.replace('/', '_')}.csv"))
        opts = {'config': config, 'oos_fraction': args.oos_fraction,
                'min_trades': args.min_trades, 'modes': list(args.modes),
                'run': str(run_dir)}
        started = time.time()
        fast_row = process_cell(symbol, df, fast, slow, dict(opts, engine='fast'))
        fast_seconds = time.time() - started
        started = time.time()
        ref_row = process_cell(symbol, df, fast, slow, dict(opts, engine='reference'))
        ref_seconds = time.time() - started
        mismatches = []
        for leg in ['real'] + [f'null/{m}' for m in args.modes]:
            def _leg(row):
                if leg == 'real':
                    return row['real']
                return row['null'][leg.split('/')[1]]
            a, b = _leg(fast_row), _leg(ref_row)
            for key in sorted(set(a) | set(b)):
                va, vb = a.get(key), b.get(key)
                if isinstance(va, float) and isinstance(vb, float):
                    same = abs(va - vb) <= 1e-9
                else:
                    same = va == vb
                if not same:
                    mismatches.append({'leg': leg, 'field': key,
                                       'fast': va, 'reference': vb})
        rows.append({'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                     'fast_seconds': fast_seconds, 'reference_seconds': ref_seconds,
                     'speedup': (ref_seconds / fast_seconds) if fast_seconds else None,
                     'n_mismatches': len(mismatches), 'mismatches': mismatches})
        print(f"{symbol} P{fast}_{slow}: fast {fast_seconds:.2f}s, "
              f"reference {ref_seconds:.2f}s, mismatches {len(mismatches)}", flush=True)

    payload = {
        'source_run': str(run_dir),
        'config': config,
        'modes': list(args.modes),
        'n_cells': len(rows),
        'n_mismatches': sum(r['n_mismatches'] for r in rows),
        'cells': rows,
    }
    if args.out:
        out = Path(args.out)
        out.mkdir(parents=True, exist_ok=True)
        (out / 'summary.json').write_text(json.dumps(payload, indent=2, default=str))
        print(f'Wrote {out}/summary.json')
    print(f"{payload['n_cells']} cells, {payload['n_mismatches']} field mismatches")
    return 0 if payload['n_mismatches'] == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
