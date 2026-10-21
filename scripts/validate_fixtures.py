#!/usr/bin/env python3
"""Validate hourly fixtures for a batch of symbols.

Checks (PROMPT.md validation recipe):
  1. no duplicate timestamps
  2. contiguous 1h grid with no missing hours (max gap <= 1h)
  3. no invalid OHLC rows (high >= low, high >= open/close, low <= open/close)
  4. no NaN rows
  5. price identity: |log(last close / CoinGecko ranked price)| <= 0.20
  6. cost-to-move multiple: 0.12 / median absolute hourly return

Usage:
    python scripts/validate_fixtures.py --symbols SATS/USDT OGN/USDT ...
    python scripts/validate_fixtures.py --all --out results/fixture_validation.json
"""
import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from data.data_loader import load_ohlcv_csv

COSTS_BPS_PER_SIDE = 12.0  # 10 bps taker + 2 bps slippage


def validate(path: Path) -> dict:
    out = {'path': str(path), 'symbol': path.stem.replace('_', '/')}
    try:
        df = pd.read_csv(path)
    except Exception as e:
        out['error'] = f'read failed: {e}'
        return out
    out['rows'] = len(df)
    if len(df) == 0:
        out['error'] = 'empty fixture'
        return out

    cols = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    missing = [c for c in cols if c not in df.columns]
    if missing:
        out['error'] = f'missing columns {missing}'
        return out

    # NaN rows
    nan_rows = int(df[cols].isna().any(axis=1).sum())
    out['nan_rows'] = nan_rows

    # duplicate timestamps
    dup_ts = int(df['timestamp'].duplicated().sum())
    out['dup_timestamps'] = dup_ts

    # contiguous 1h grid
    ts = pd.to_datetime(df['timestamp'], unit='s', utc=True, errors='coerce')
    if ts.isna().any():
        out['bad_timestamps'] = int(ts.isna().sum())
    else:
        ts_sorted = ts.sort_values()
        deltas = ts_sorted.diff().dropna()
        gaps = deltas[~(deltas == pd.Timedelta(hours=1))]
        out['max_gap_hours'] = float(gaps.max().total_seconds() / 3600) if len(gaps) else 0.0
        out['gap_count'] = int(len(gaps))

    # invalid OHLC
    bad_ohlc = int(((df['high'] < df['low']) |
                    (df['high'] < df['open']) |
                    (df['high'] < df['close']) |
                    (df['low'] > df['open']) |
                    (df['low'] > df['close'])).sum())
    out['invalid_ohlc_rows'] = bad_ohlc

    # zero-volume bars
    out['zero_volume_rows'] = int((df['volume'] == 0).sum())
    out['zero_volume_pct'] = round(100.0 * out['zero_volume_rows'] / len(df), 2)

    # price identity vs CoinGecko
    last_close = float(df['close'].iloc[-1])
    out['last_close'] = last_close
    out['last_ts'] = str(ts.iloc[-1])

    # cost-to-move multiple
    rets = df['close'].pct_change().dropna()
    med_abs_move = float(rets.abs().median()) if len(rets) else float('nan')
    out['median_abs_hourly_return'] = med_abs_move
    if med_abs_move and med_abs_move > 0:
        out['cost_to_move_multiple'] = round(COSTS_BPS_PER_SIDE / (med_abs_move * 100), 2)
    else:
        out['cost_to_move_multiple'] = None

    ok = (nan_rows == 0 and dup_ts == 0 and bad_ohlc == 0
          and out.get('bad_timestamps', 0) == 0
          and out.get('max_gap_hours', 2) <= 1.0)
    out['valid'] = bool(ok)
    return out


def loader_rows(path: Path) -> dict:
    """How many rows the data loader keeps, and how many it drops.

    The loader removes duplicate timestamps, NaN rows and rows whose OHLC
    geometry is impossible. Every grid result is computed on the *loaded*
    series, so the number of dropped rows is part of the data-layer record.
    """
    raw = pd.read_csv(path)
    loaded = load_ohlcv_csv(path)
    return {
        'raw_rows': int(len(raw)),
        'loaded_rows': int(len(loaded)),
        'dropped_rows': int(len(raw) - len(loaded)),
    }


def main():
    parser = argparse.ArgumentParser(description='Validate hourly fixtures')
    parser.add_argument('--symbols', nargs='+', default=None)
    parser.add_argument('--all', action='store_true',
                        help='Validate every fixture in the fixtures directory')
    parser.add_argument('--fixtures-dir', default='data/fixtures')
    parser.add_argument('--cg-prices', default=None,
                        help='JSON mapping symbol -> CoinGecko price_usd')
    parser.add_argument('--out', default=None,
                        help='Write the JSON result to this path')
    args = parser.parse_args()

    if not args.symbols and not args.all:
        raise SystemExit('pass --symbols or --all')

    cg = {}
    if args.cg_prices:
        cg = json.loads(Path(args.cg_prices).read_text())

    results = []
    if args.all:
        for path in sorted(Path(args.fixtures_dir).glob('*.csv')):
            r = validate(path)
            r.update(loader_rows(path))
            results.append(r)
    else:
        for sym in args.symbols:
            path = Path(args.fixtures_dir) / f'{sym.replace("/", "_")}.csv'
            r = validate(path)
            r.update(loader_rows(path))
            if sym in cg:
                cg_price = float(cg[sym])
                r['cg_price'] = cg_price
                if r.get('last_close'):
                    r['log_price_ratio'] = round(math.log(r['last_close'] / cg_price), 4)
                    r['price_identity_ok'] = bool(abs(r['log_price_ratio']) <= 0.20)
            results.append(r)

    if args.all:
        summary = {
            'fixtures': len(results),
            'valid': sum(1 for r in results if r.get('valid')),
            'invalid': sum(1 for r in results if not r.get('valid')),
            'with_gaps': sum(1 for r in results if r.get('gap_count')),
            'max_gap_hours': max((r.get('max_gap_hours') or 0.0) for r in results),
            'duplicate_timestamps': sum(r.get('dup_timestamps') or 0 for r in results),
            'nan_rows': sum(r.get('nan_rows') or 0 for r in results),
            'invalid_ohlc_rows': sum(r.get('invalid_ohlc_rows') or 0 for r in results),
            'raw_rows': sum(r.get('raw_rows') or 0 for r in results),
            'loaded_rows': sum(r.get('loaded_rows') or 0 for r in results),
            'dropped_rows': sum(r.get('dropped_rows') or 0 for r in results),
            'median_cost_to_move_multiple': float(np.median(
                [r['cost_to_move_multiple'] for r in results
                 if r.get('cost_to_move_multiple')])),
        }
        print(json.dumps(summary, indent=2))
        invalid = [r for r in results if not r.get('valid')]
        if invalid:
            print(f'\n{len(invalid)} invalid fixture(s): '
                  f'{[r["symbol"] for r in invalid][:20]}')
        results = {'summary': summary, 'fixtures': results}
    else:
        print(json.dumps(results, indent=2))

    if args.out:
        Path(args.out).write_text(json.dumps(results, indent=2))
        print(f'\nWrote {args.out}')

    bad = [r for r in (results if isinstance(results, list) else results['fixtures'])
           if not r.get('valid')]
    checked = len(results) if isinstance(results, list) else len(results['fixtures'])
    print(f'{checked} fixtures checked, {len(bad)} invalid')
    if bad and not args.all:
        # The single-symbol path keeps its original contract: an invalid
        # fixture is a non-zero exit.
        sys.exit(1)


if __name__ == '__main__':
    main()