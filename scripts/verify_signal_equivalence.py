#!/usr/bin/env python3
"""Check that the vectorized signal generator matches the reference exactly.

`signals.signals.generate_signals_vectorized` is a drop-in twin of the
reference `generate_signals`. The null harness (`scripts/null_grid_scan.py`)
runs the vectorized version over all 17 556 grid cells, so the two must agree
exactly - an approximate agreement would make the randomization null compare
against a slightly different strategy than the one the program ran.

Usage:
    PYTHONPATH=. python3 scripts/verify_signal_equivalence.py
"""
import argparse
import json
from pathlib import Path

import numpy as np

from data.data_loader import load_ohlcv_csv
from signals.signals import generate_signals, generate_signals_vectorized

DEFAULT_PAIRS = [(8, 12), (20, 26), (50, 100), (89, 144), (144, 200)]


def compare(df, fast, slow):
    """Return (n_signals, identical) for one frame and one period pair."""
    ref = generate_signals(df.copy(), ema_fast_period=fast, ema_slow_period=slow)
    vec = generate_signals_vectorized(df.copy(), ema_fast_period=fast, ema_slow_period=slow)
    same_signal = np.array_equal(ref['signal'].to_numpy(), vec['signal'].to_numpy())
    same_entry = np.array_equal(ref['entry_price'].to_numpy(),
                                 vec['entry_price'].to_numpy(), equal_nan=True)
    same_emas = (np.array_equal(ref['ema_fast'].to_numpy(), vec['ema_fast'].to_numpy())
                 and np.array_equal(ref['ema_slow'].to_numpy(), vec['ema_slow'].to_numpy()))
    n_signals = int((ref['signal'].to_numpy() != 0).sum())
    return n_signals, bool(same_signal and same_entry and same_emas)


def main():
    parser = argparse.ArgumentParser(description='Vectorized vs reference signal check')
    parser.add_argument('--fixture-base', type=str, default='data/fixtures')
    parser.add_argument('--bars', type=int, default=4000,
                        help='Bars of each fixture used for the sweep (0 = full series)')
    parser.add_argument('--pairs', type=str, default=None,
                        help='Comma separated "fast:slow" pairs (default: five pairs)')
    parser.add_argument('--full-series-symbols', type=int, default=10,
                        help='How many symbols are additionally checked on the full series')
    parser.add_argument('--out', type=str, default=None)
    args = parser.parse_args()

    pairs = DEFAULT_PAIRS
    if args.pairs:
        pairs = [tuple(int(x) for x in item.split(':')) for item in args.pairs.split(',')]

    base = Path(args.fixture_base)
    files = sorted(base.glob('*.csv'))
    n_checked = 0
    n_signals = 0
    mismatches = []

    for i, path in enumerate(files):
        df = load_ohlcv_csv(path)
        if args.bars:
            df = df.iloc[:args.bars].reset_index(drop=True)
        for fast, slow in pairs:
            count, ok = compare(df, fast, slow)
            n_checked += 1
            n_signals += count
            if not ok:
                mismatches.append({'symbol': path.stem, 'P_fast': fast, 'P_slow': slow})
        if (i + 1) % 25 == 0:
            print(f'{i + 1}/{len(files)} symbols checked', flush=True)

    # The sweep above truncates the series, so a handful of symbols are also
    # compared on their full history (the EMA warm-up then spans ~200 bars).
    full_checked = 0
    for path in files[:args.full_series_symbols]:
        df = load_ohlcv_csv(path)
        for fast, slow in pairs[:2]:
            count, ok = compare(df, fast, slow)
            full_checked += 1
            n_checked += 1
            n_signals += count
            if not ok:
                mismatches.append({'symbol': path.stem, 'P_fast': fast,
                                   'P_slow': slow, 'full_series': True})

    payload = {
        'symbols': len(files),
        'cells_compared': n_checked,
        'signals_compared': n_signals,
        'pairs': [list(p) for p in pairs],
        'bars_used': args.bars or 'full',
        'full_series_cells_compared': full_checked,
        'mismatches': mismatches,
        'identical': not mismatches,
    }
    print(json.dumps(payload, indent=2))
    if args.out:
        Path(args.out).write_text(json.dumps(payload, indent=2))
    if mismatches:
        raise SystemExit(f'{len(mismatches)} mismatching cell(s)')


if __name__ == '__main__':
    main()
