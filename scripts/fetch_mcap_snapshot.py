#!/usr/bin/env python3
"""Fetch a dated market-cap ranking snapshot and expand the working universe.

Source: CoinGecko public API /coins/markets (vs_currency=usd, order=market_cap_desc).
No API key required. The snapshot is persisted to universe/mcap_snapshot_<TS>.json
so that rank drift and the exact market caps used for ordering are auditable.

Filters applied before a name becomes eligible (PROMPT.md §2.4):
  * stablecoins / fiat-pegged bases are excluded (the tradable is BASE/USDT)
  * wrapped-derivative duplicates of already-included names are excluded
  * names without a tradable spot USDT pair on the data layer (KuCoin) are excluded
  * names without enough hourly history for the largest P_slow (200) + OOS window
    are excluded

Expansion rule (PROMPT.md §2.1.2): append names that rank strictly below the
lowest market-cap name already in the working universe, in descending market-cap
order. Prior names are never reordered or dropped.

Usage:
    python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10
    python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10 --apply
"""
import argparse
import json
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

COINGECKO_URL = 'https://api.coingecko.com/api/v3/coins/markets'
KUCOIN_SYMBOLS_URL = 'https://api.kucoin.com/api/v1/symbols'
KUCOIN_CANDLES_URL = 'https://api.kucoin.com/api/v1/market/candles'
REQUEST_TIMEOUT = 30
PAUSE_SECONDS = 0.6

# Minimum hourly history a name needs before it is eligible (PROMPT.md §2.4).
# Must cover the largest P_slow in the grid (200) plus an out-of-sample window.
# The existing top-5 fixtures carry ~22k hourly bars, so require 2 years of
# hourly coverage (17520 bars) to keep the new batch comparable.
MIN_HISTORY_YEARS = 2.0

# Stablecoin / fiat-pegged bases that must not be treated as crypto continuation
# instruments. Matched case-insensitively on the CoinGecko symbol.
STABLE_SYMBOLS = {
    'usdt', 'usdc', 'usde', 'usds', 'usd1', 'dai', 'usdd', 'usdg', 'usdy', 'pyusd',
    'tusd', 'fdusd', 'usdtb', 'usdt0', 'susde', 'susds', 'buidl', 'usdf', 'rlusd',
    'rlusdt', 'rlusde', 'xaut', 'xau', 'paxg', 'xauusdt', 'usdp', 'ustc', 'vai',
    'eurs', 'eurt', 'eurc', 'agde', 'eurcv', 'jupusd', 'bfc', 'deusd', 'susdsusdt',
    'gyd', 'gyen', 'ceur', 'usddc', 'syrupusdc',
}

# Known wrapped / staked duplicates of names already in the universe. These are not
# independent instruments and would double-count exposure.
WRAPPED_DUPLICATES = {
    'btcb', 'cbbtc', 'wbtc', 'tbtc', 'solvbtc', 'btcusd',
    'weeth', 'steth', 'weth', 'reth', 'cbeth', 'reth2', 'ezeth', 'rseth', 'oseth',
    'wbeth', 'sweth', 'meth', 'ethx', 'ethplus', 'ankreth',
    'solwb', 'msol', 'jitosol', 'bsol', 'hsol',
    'bnbpeg', 'bnbchain',
}


def fetch_markets(pages: int, per_page: int = 100) -> list:
    """Fetch market-cap-descending market data from CoinGecko."""
    out = []
    for page in range(1, pages + 1):
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': per_page,
            'page': page,
            'sparkline': 'false',
        }
        resp = requests.get(COINGECKO_URL, params=params, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        rows = resp.json()
        if not rows:
            break
        out.extend(rows)
        time.sleep(PAUSE_SECONDS)
    return out


def fetch_kucoin_usdt_pairs() -> set:
    """Return set of tradable KuCoin spot USDT pair base assets."""
    resp = requests.get(KUCOIN_SYMBOLS_URL, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    payload = resp.json()
    pairs = set()
    for s in payload.get('data', []) or []:
        if s.get('quoteCurrency') == 'USDT' and s.get('enableTrading'):
            pairs.add(s['symbol'].split('-')[0].upper())
    return pairs


def has_min_history(symbol: str, min_years: float = MIN_HISTORY_YEARS) -> bool:
    """Check that the KuCoin pair has at least `min_years` of hourly bars.

    A single probe far enough in the past is enough: if a candle exists at or
    before (now - min_years), the listing is old enough.
    """
    probe_ts = int((datetime.now(timezone.utc) - timedelta(days=365.25 * min_years)).timestamp())
    params = {'symbol': f'{symbol}-USDT', 'type': '1hour', 'limit': 1, 'endAt': probe_ts}
    try:
        resp = requests.get(KUCOIN_CANDLES_URL, params=params, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        payload = resp.json()
    except Exception:
        return False
    if payload.get('code') != '200000':
        return False
    rows = payload.get('data') or []
    if not rows:
        return False
    oldest = int(rows[-1][0])
    return oldest <= probe_ts


def build_snapshot(pages: int) -> dict:
    rows = fetch_markets(pages)
    kucoin_pairs = fetch_kucoin_usdt_pairs()

    entries = []
    rank = 0
    for row in rows:
        sym = (row.get('symbol') or '').upper()
        mcap = row.get('market_cap') or 0
        if not sym or not mcap:
            continue
        rank += 1
        if sym.lower() in STABLE_SYMBOLS:
            reason = 'stablecoin_or_fiat_pegged'
        elif sym.lower() in WRAPPED_DUPLICATES:
            reason = 'wrapped_or_staked_duplicate'
        elif sym not in kucoin_pairs:
            reason = 'no_tradable_kucoin_spot_usdt_pair'
        elif not has_min_history(sym):
            reason = 'insufficient_hourly_history_for_grid'
        else:
            reason = None
        entries.append({
            'rank': rank,
            'symbol': sym,
            'name': row.get('name'),
            'market_cap_usd': int(mcap),
            'price_usd': row.get('current_price'),
            'volume_24h_usd': row.get('total_volume'),
            'kucoin_usdt_pair': sym in kucoin_pairs,
            'exclusion_reason': reason,
        })
    return {
        'source': 'CoinGecko public API /api/v3/coins/markets (vs_currency=usd, order=market_cap_desc)',
        'pages_fetched': pages,
        'fetched_at': datetime.now(timezone.utc).isoformat(),
        'entries': entries,
    }


def main():
    parser = argparse.ArgumentParser(description='Fetch market-cap snapshot and expand universe')
    parser.add_argument('--pages', type=int, default=4, help='CoinGecko pages of 100 to fetch')
    parser.add_argument('--batch-size', type=int, default=10, help='Max new names to append')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--out-dir', type=str, default='universe')
    parser.add_argument('--apply', action='store_true', default=False,
                        help='Write the expanded ranking to universe/mcap_rank.json')
    args = parser.parse_args()

    snapshot = build_snapshot(args.pages)
    ts = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    snapshot_path = out_dir / f'mcap_snapshot_{ts}.json'
    with open(snapshot_path, 'w') as f:
        json.dump(snapshot, f, indent=2)

    # Current working universe
    mcap_path = Path(args.mcap)
    with open(mcap_path) as f:
        current = json.load(f)
    current_symbols = list(current.get('symbols', []))
    current_set = {s.split('/')[0].upper() for s in current_symbols}

    # Market cap of each already-included name, from the fresh snapshot.
    by_sym = {e['symbol']: e for e in snapshot['entries']}
    included_mcaps = {s: by_sym.get(s.split('/')[0].upper(), {}).get('market_cap_usd') for s in current_symbols}
    known = [m for m in included_mcaps.values() if m]
    floor_mcap = min(known) if known else 0

    added = []
    for e in snapshot['entries']:
        if len(added) >= args.batch_size:
            break
        if e['exclusion_reason'] is not None:
            continue
        if e['symbol'] in current_set:
            continue
        if e['market_cap_usd'] >= floor_mcap:
            continue
        added.append(e)

    print(f'Snapshot: {snapshot_path}')
    print(f'Current universe ({len(current_symbols)}): {current_symbols}')
    print(f'Included market caps (fresh snapshot): {included_mcaps}')
    print(f'Expansion floor (lowest included mcap): {floor_mcap}')
    print(f'New batch ({len(added)}):')
    for e in added:
        print(f"  #{e['rank']:>4} {e['symbol']:<8} mcap=${e['market_cap_usd']:,}")

    if args.apply and added:
        expanded = current_symbols + [f"{e['symbol']}/USDT" for e in added]
        payload = {
            'updated_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            'snapshot_id': snapshot_path.stem,
            'snapshot_source': snapshot['source'],
            'snapshot_fetched_at': snapshot['fetched_at'],
            'n_symbols': len(expanded),
            'added_in_this_expansion': [f"{e['symbol']}/USDT" for e in added],
            'added_market_caps_usd': {e['symbol']: e['market_cap_usd'] for e in added},
            'symbols': expanded,
        }
        with open(mcap_path, 'w') as f:
            json.dump(payload, f, indent=2)
        print(f'\nUpdated {mcap_path}: {len(current_symbols)} -> {len(expanded)} symbols')
    elif not args.apply:
        print('\n(dry run: pass --apply to write the expanded ranking)')


if __name__ == '__main__':
    main()
