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
"""
import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

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


def main():
    parser = argparse.ArgumentParser(description='Validate hourly fixtures')
    parser.add_argument('--symbols', nargs='+', required=True)
    parser.add_argument('--fixtures-dir', default='data/fixtures')
    parser.add_argument('--cg-prices', default=None,
                        help='JSON mapping symbol -> CoinGecko price_usd')
    args = parser.parse_args()

    cg = {}
    if args.cg_prices:
        cg = json.loads(Path(args.cg_prices).read_text())

    results = []
    for sym in args.symbols:
        path = Path(args.fixtures_dir) / f'{sym.replace("/", "_")}.csv'
        r = validate(path)
        if sym in cg:
            cg_price = float(cg[sym])
            r['cg_price'] = cg_price
            if r.get('last_close'):
                r['log_price_ratio'] = round(math.log(r['last_close'] / cg_price), 4)
                r['price_identity_ok'] = bool(abs(r['log_price_ratio']) <= 0.20)
        results.append(r)

    print(json.dumps(results, indent=2))
    bad = [r for r in results if not r.get('valid')]
    print(f'\n{len(results) - len(bad)}/{len(results)} fixtures valid')
    if bad:
        sys.exit(1)


if __name__ == '__main__':
    main()