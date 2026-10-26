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

The ranking may be refreshed at most once per 24 h (PROMPT.md §2.1.5): a live
pass is refused before the bound in `universe/last_scan.json` has elapsed, and
`--apply-from` (which makes no provider call) is never gated.
"""
import argparse
import csv
import json
import math
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

try:
    from scripts.refresh_gate import bound_after, override_reason, require_open_gate
except ModuleNotFoundError:  # direct execution: sys.path[0] is scripts/, not the root
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts.refresh_gate import bound_after, override_reason, require_open_gate

COINGECKO_URL = 'https://api.coingecko.com/api/v3/coins/markets'
KUCOIN_SYMBOLS_URL = 'https://api.kucoin.com/api/v1/symbols'
KUCOIN_CANDLES_URL = 'https://api.kucoin.com/api/v1/market/candles'
KUCOIN_TICKER_URL = 'https://api.kucoin.com/api/v1/market/orderbook/level1'
REQUEST_TIMEOUT = 30
PAUSE_SECONDS = 0.6

# The CoinGecko free tier rate-limits the public markets endpoint to a handful of
# calls per minute; paging through 10 pages 0.6s apart reliably answers 429 on
# page 6. The ranking pages are therefore spaced out so a multi-page pass
# completes instead of aborting half-way through the coverage band.
COINGECKO_PAUSE_SECONDS = 30.0

# A ticker can name two different assets (CoinGecko "ONE" is "ONEchain" while
# KuCoin's ONE-USDT is "Harmony"). Trading the wrong asset would put a name in
# the universe whose market cap does not match the asset actually backtested, so
# a candidate is only eligible when the KuCoin pair trades at the same price as
# the ranked CoinGecko entry (within this log tolerance).
PRICE_MATCH_TOLERANCE = 0.20

# The public CoinGecko endpoint rate-limits with HTTP 429 under burst traffic, which
# aborted the ranking fetch mid-way. Retry those (and transient 5xx) with a bounded
# exponential backoff instead of losing the whole snapshot.
MAX_RETRIES = 6
RETRY_BACKOFF_SECONDS = 5.0
RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def get_with_retry(url: str, params: dict, timeout: int = REQUEST_TIMEOUT,
                   max_retries: int = MAX_RETRIES) -> requests.Response:
    """GET with bounded exponential backoff on rate limits and transient server errors."""
    last_exc = None
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, params=params, timeout=timeout)
        except requests.RequestException as exc:
            last_exc = exc
        else:
            if resp.status_code not in RETRYABLE_STATUS:
                resp.raise_for_status()
                return resp
            last_exc = requests.HTTPError(
                f'{resp.status_code} for {resp.url}', response=resp)
        sleep_for = RETRY_BACKOFF_SECONDS * (2 ** attempt)
        print(f'  retry {attempt + 1}/{max_retries} in {sleep_for:.0f}s '
              f'({last_exc})', flush=True)
        time.sleep(sleep_for)
    raise last_exc

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


def fetch_markets(pages: int, per_page: int = 100):
    """Fetch market-cap-descending market data from CoinGecko.

    Returns (rows, pages_fetched). `pages_fetched` counts the pages that
    actually returned rows, so a pass that stops early is never recorded as a
    complete pass over the requested page range.
    """
    out = []
    pages_fetched = 0
    for page in range(1, pages + 1):
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': per_page,
            'page': page,
            'sparkline': 'false',
        }
        resp = get_with_retry(COINGECKO_URL, params)
        rows = resp.json()
        if not rows:
            break
        out.extend(rows)
        pages_fetched = page
        time.sleep(COINGECKO_PAUSE_SECONDS)
    return out, pages_fetched


def fetch_kucoin_usdt_pairs() -> set:
    """Return set of tradable KuCoin spot USDT pair base assets."""
    resp = get_with_retry(KUCOIN_SYMBOLS_URL, {})
    payload = resp.json()
    pairs = set()
    for s in payload.get('data', []) or []:
        if s.get('quoteCurrency') == 'USDT' and s.get('enableTrading'):
            pairs.add(s['symbol'].split('-')[0].upper())
    return pairs


def has_min_history(symbol: str, min_years: float = MIN_HISTORY_YEARS):
    """Check that the KuCoin pair has at least `min_years` of hourly bars.

    A single probe far enough in the past is enough: if a candle exists at or
    before (now - min_years), the listing is old enough.

    Returns True (old enough), False (the pair demonstrably has no history that
    far back) or None when the probe itself failed. The third answer is the
    point of this signature: PROMPT.md §2.1.5 says an API failure is not proof
    that a symbol is ineligible, so a failed probe must not be reported as
    "no history" - that would silently drop a tradable name from the universe.
    The caller keeps such a name as a candidate and lets the fixture download
    (which reads the real bar series) be the authoritative gate.
    """
    probe_ts = int((datetime.now(timezone.utc) - timedelta(days=365.25 * min_years)).timestamp())
    params = {'symbol': f'{symbol}-USDT', 'type': '1hour', 'limit': 1, 'endAt': probe_ts}
    try:
        resp = get_with_retry(KUCOIN_CANDLES_URL, params)
        payload = resp.json()
    except Exception:
        return None
    if payload.get('code') != '200000':
        # An error answer (e.g. the transient 400100 of batch 12) is not
        # evidence about the listing date.
        return None
    rows = payload.get('data') or []
    if not rows:
        return False
    oldest = int(rows[-1][0])
    return oldest <= probe_ts


def kucoin_last_price(symbol: str):
    """Last traded price of BASE-USDT on KuCoin, or None when unavailable."""
    try:
        resp = get_with_retry(KUCOIN_TICKER_URL, {'symbol': f'{symbol}-USDT'})
        payload = resp.json()
    except Exception:
        return None
    if payload.get('code') != '200000':
        return None
    try:
        price = float((payload.get('data') or {}).get('price'))
    except (TypeError, ValueError):
        return None
    return price if price > 0 else None


def price_identity_ok(entry: dict) -> bool:
    """True when the KuCoin pair trades the same asset the ranking describes.

    A ticker can belong to two different assets; the KuCoin pair may then be a
    completely different coin. Comparing the live KuCoin price with the ranked
    CoinGecko price catches that. An unavailable price is not treated as a
    mismatch: a name is never dropped because an API call failed.
    """
    cg_price = entry.get('price_usd')
    if not cg_price or cg_price <= 0:
        return True
    kc_price = kucoin_last_price(entry['symbol'])
    if kc_price is None:
        return True
    return abs(math.log(kc_price / cg_price)) <= PRICE_MATCH_TOLERANCE


def build_snapshot(pages: int) -> dict:
    rows, pages_fetched = fetch_markets(pages)
    kucoin_pairs = fetch_kucoin_usdt_pairs()

    entries = []
    rank = 0
    probe_failures = []
    for row in rows:
        sym = (row.get('symbol') or '').upper()
        mcap = row.get('market_cap') or 0
        if not sym or not mcap:
            continue
        rank += 1
        entry = {
            'rank': rank,
            'symbol': sym,
            'name': row.get('name'),
            'market_cap_usd': int(mcap),
            'price_usd': row.get('current_price'),
            'volume_24h_usd': row.get('total_volume'),
            'kucoin_usdt_pair': sym in kucoin_pairs,
            'exclusion_reason': None,
        }
        if sym.lower() in STABLE_SYMBOLS:
            reason = 'stablecoin_or_fiat_pegged'
        elif sym.lower() in WRAPPED_DUPLICATES:
            reason = 'wrapped_or_staked_duplicate'
        elif sym not in kucoin_pairs:
            reason = 'no_tradable_kucoin_spot_usdt_pair'
        elif not price_identity_ok(entry):
            reason = 'kucoin_pair_trades_a_different_asset'
        else:
            history_ok = has_min_history(sym)
            if history_ok is None:
                # The probe failed, so the listing date is unknown - not known
                # to be too recent. Such a name stays a candidate and the
                # fixture download (which reads the real bar series) is the
                # authoritative gate; dropping it here would turn a transient
                # API failure into a permanent exclusion.
                probe_failures.append(sym)
                entry['history_probe_failed'] = True
                reason = None
            elif not history_ok:
                reason = 'insufficient_hourly_history_for_grid'
            else:
                reason = None
        entry['exclusion_reason'] = reason
        entries.append(entry)
    snapshot = {
        'source': 'CoinGecko public API /api/v3/coins/markets (vs_currency=usd, order=market_cap_desc)',
        'pages_requested': pages,
        'pages_fetched': pages_fetched,
        'all_requested_pages_returned': pages_fetched == pages,
        'entries_count': len(entries),
        'history_probe_failures': probe_failures,
        'history_probe_failure_count': len(probe_failures),
        'fetched_at': datetime.now(timezone.utc).isoformat(),
        'entries': entries,
    }
    snapshot.update(coverage_facts(snapshot))
    return snapshot


def coverage_facts(snapshot: dict) -> dict:
    """Page/entry coverage of a ranking snapshot, derived from the entries.

    Older snapshots do not carry the coverage fields, so they are recomputed
    from the entry list. The lowest covered rank and market cap are what decide
    whether a pass actually reached below the current expansion floor.
    """
    entries = snapshot.get('entries') or []
    last = entries[-1] if entries else {}
    pages_requested = snapshot.get('pages_requested', snapshot.get('pages_fetched'))
    pages_fetched = snapshot.get('pages_fetched')
    return {
        'pages_requested': pages_requested,
        'pages_fetched': pages_fetched,
        'all_requested_pages_returned': (
            None if pages_requested is None or pages_fetched is None
            else pages_fetched == pages_requested
        ),
        'entries_count': len(entries),
        'lowest_rank_covered': last.get('rank'),
        'lowest_market_cap_usd': last.get('market_cap_usd'),
    }


def coverage_reaches_below_floor(snapshot: dict, floor_mcap: float) -> bool:
    """True when the pass observed at least one name below the expansion floor.

    A pass that stops above the floor cannot see the band the expansion works
    on, so "no eligible name found" means "nothing looked at", not "nothing
    there".
    """
    facts = coverage_facts(snapshot)
    lowest = facts.get('lowest_market_cap_usd')
    if lowest is None or not floor_mcap:
        return False
    return lowest < floor_mcap


def build_scan_record(snapshot: dict, snapshot_path: Path, current_symbols: list,
                      floor_mcap: float, floor_symbol: str, eligible_below: list,
                      batch: list, scanned_at: str) -> dict:
    """Machine-readable record of one ranking pass (PROMPT.md §2.1.5)."""
    facts = coverage_facts(snapshot)
    reaches = coverage_reaches_below_floor(snapshot, floor_mcap)
    if eligible_below:
        state = 'EXPANSION_AVAILABLE'
        next_refresh = None
    elif reaches:
        state = 'AWAITING_NEW_ELIGIBLE_CANDIDATES'
        scanned = datetime.fromisoformat(scanned_at)
        next_refresh = (scanned + timedelta(hours=24)).isoformat()
    else:
        state = 'INCOMPLETE_SCAN'
        next_refresh = datetime.now(timezone.utc).isoformat()
    return {
        'recorded_at': datetime.now(timezone.utc).isoformat(),
        'state': state,
        'snapshot_id': snapshot_path.stem,
        'snapshot_path': str(snapshot_path),
        'snapshot_source': snapshot.get('source'),
        'scanned_at': scanned_at,
        'coverage': facts,
        'coverage_reaches_below_floor': reaches,
        'universe_n': len(current_symbols),
        'expansion_floor': {'symbol': floor_symbol, 'market_cap_usd': floor_mcap},
        'eligible_unseen_below_floor_count': len(eligible_below),
        'eligible_unseen_below_floor': [
            {'rank': e['rank'], 'symbol': e['symbol'], 'name': e.get('name'),
             'market_cap_usd': e['market_cap_usd']} for e in eligible_below],
        'batch_selected': [f"{e['symbol']}/USDT" for e in batch],
        'next_eligible_refresh_at': next_refresh,
    }


def fixture_last_close(ticker: str, fixtures_dir: Path):
    """Last close of the hourly fixture we hold for `ticker`, or None.

    The fixture of a symbol is named after the whole symbol (`BTC/USDT` ->
    `BTC_USDT.csv`), so a caller that only knows the base ticker is served by
    the second candidate. Without it the collision check below silently never
    finds a fixture and falls back to the wrong asset.
    """
    base = Path(fixtures_dir)
    candidates = [base / f'{ticker.replace("/", "_")}.csv']
    stem = ticker.split('/')[0]
    if f'{stem}.csv' != candidates[0].name:
        candidates.append(base / f'{stem}.csv')
    for path in candidates:
        if not path.exists():
            continue
        try:
            with open(path) as f:
                rows = list(csv.DictReader(f))
        except Exception:
            return None
        if not rows:
            return None
        try:
            value = float(rows[-1]['close'])
        except (KeyError, TypeError, ValueError):
            return None
        return value if value > 0 else None
    return None


def match_entry(entries: list, ticker: str, fixtures_dir: Path):
    """Pick the snapshot entry that corresponds to the asset we actually hold.

    Several CoinGecko assets can share one ticker. For an unambiguous ticker the
    single entry is used. For an ambiguous ticker the entry whose quoted price is
    closest to the last close of our own fixture wins - that is the asset the
    grid actually traded.

    `ticker` is the symbol the universe holds (`ONE/USDT`), because the fixture
    that identifies the asset is named after it.
    """
    if not entries:
        return None
    if len(entries) == 1:
        return entries[0]
    close = fixture_last_close(ticker, fixtures_dir)
    if close:
        def price_distance(e):
            price = e.get('price_usd')
            if not price or price <= 0:
                return float('inf')
            return abs(math.log(price / close))
        return min(entries, key=price_distance)
    return entries[0]


def included_market_caps(snapshot: dict, current_symbols: list, fixtures_dir: Path) -> dict:
    """Market cap of every name the working universe already contains.

    The market caps are read from the fresh snapshot, not from the snapshot the
    universe was built from, because the expansion floor is defined by what
    the ranking says *now*: the floor is the lowest market cap among the
    included names, and it moves with the market.

    A ticker can map to several different assets in the CoinGecko ranking, so
    an ambiguous ticker is resolved against the last close of the fixture the
    universe actually holds.
    """
    by_sym = {}
    for e in snapshot.get('entries') or []:
        by_sym.setdefault(e['symbol'], []).append(e)

    included = {}
    for s in current_symbols:
        ticker = s.split('/')[0].upper()
        entry = match_entry(by_sym.get(ticker, []), s, fixtures_dir)
        included[s] = entry.get('market_cap_usd') if entry else None
    return included


def expansion_floor(included_mcaps: dict) -> tuple:
    """(floor_mcap, floor_symbol) of the working universe.

    The floor is the lowest market cap the universe already contains; every
    name added by an expansion has to rank strictly below it.
    """
    known = [m for m in included_mcaps.values() if m]
    if not known:
        return 0, None
    floor_mcap = min(known)
    floor_symbol = min(((m, s) for s, m in included_mcaps.items() if m))[1]
    return floor_mcap, floor_symbol


def select_expansion_candidates(snapshot: dict, current_symbols: list,
                                 floor_mcap: float) -> list:
    """Eligible, unseen names strictly below the floor, in ranking order.

    The snapshot entries are ordered by market cap descending, so the returned
    list is descending too and a batch taken from its head keeps the global
    order of the working universe (PROMPT.md §2.1.2).
    """
    current_set = {s.split('/')[0].upper() for s in current_symbols}
    candidates = []
    seen = set()
    for e in snapshot.get('entries') or []:
        if e.get('exclusion_reason') is not None:
            continue
        if e['symbol'] in current_set or e['symbol'] in seen:
            continue
        if e['market_cap_usd'] >= floor_mcap:
            continue
        candidates.append(e)
        seen.add(e['symbol'])
    return candidates


def main():
    parser = argparse.ArgumentParser(description='Fetch market-cap snapshot and expand universe')
    parser.add_argument('--pages', type=int, default=4, help='CoinGecko pages of 100 to fetch')
    parser.add_argument('--batch-size', type=int, default=10, help='Max new names to append')
    parser.add_argument('--mcap', type=str, default='universe/mcap_rank.json')
    parser.add_argument('--out-dir', type=str, default='universe')
    parser.add_argument('--fixtures-dir', type=str, default='data/fixtures',
                        help='Hourly fixtures used to disambiguate shared tickers')
    parser.add_argument('--apply', action='store_true', default=False,
                        help='Write the expanded ranking to universe/mcap_rank.json')
    parser.add_argument('--apply-from', type=str, default=None,
                        help='Apply the expansion from a previously fetched snapshot file '
                             '(universe/mcap_snapshot_<TS>.json) instead of re-fetching, so the '
                             'batch is exactly the one that was reviewed')
    parser.add_argument('--verify-prices', action='store_true', default=False,
                        help='Check that each eligible candidate\'s KuCoin pair trades the same '
                             'asset the ranking describes (ticker collisions) and mark the '
                             'mismatches in the snapshot before selecting the batch')
    parser.add_argument('--override-gate', action='store_true', default=False,
                        help='Refresh before the recorded 24 h bound has elapsed.')
    parser.add_argument('--override-reason', type=str, default=None,
                        help='Why the 24 h bound is overridden; required with --override-gate.')
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    record_path = out_dir / 'last_scan.json'

    if args.apply_from:
        snapshot_path = Path(args.apply_from)
        snapshot = json.loads(snapshot_path.read_text())
        ts = snapshot_path.stem.replace('mcap_snapshot_', '')
    else:
        # PROMPT.md §2.1.5: the ranking is refreshed at most once per 24 h. The
        # bound is read from the scan record, so the refusal is decided by the
        # state on disk and not by the memory of an agent. Applying an existing
        # snapshot makes no provider call and is therefore not gated.
        state = json.loads(record_path.read_text()) if record_path.exists() else {}
        require_open_gate(state, None, override_reason(args))
        snapshot = build_snapshot(args.pages)
        ts = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
        out_dir.mkdir(parents=True, exist_ok=True)
        snapshot_path = out_dir / f'mcap_snapshot_{ts}.json'
        with open(snapshot_path, 'w') as f:
            json.dump(snapshot, f, indent=2)

    if args.verify_prices:
        mismatches = []
        for e in snapshot['entries']:
            if e.get('exclusion_reason') is not None:
                continue
            if not price_identity_ok(e):
                e['exclusion_reason'] = 'kucoin_pair_trades_a_different_asset'
                mismatches.append(e)
        snapshot['price_verified_at'] = datetime.now(timezone.utc).isoformat()
        with open(snapshot_path, 'w') as f:
            json.dump(snapshot, f, indent=2)
        print(f'Price identity check: {len(mismatches)} candidate(s) excluded as a '
              f'different asset')
        for e in mismatches:
            print(f"  #{e['rank']:>4} {e['symbol']:<8} {e['name']} "
                  f"mcap=${e['market_cap_usd']:,} px={e['price_usd']}")

    # Current working universe
    mcap_path = Path(args.mcap)
    with open(mcap_path) as f:
        current = json.load(f)
    current_symbols = list(current.get('symbols', []))

    # Market cap of each already-included name, from the fresh snapshot.
    # A ticker can map to several different assets in the CoinGecko ranking (e.g.
    # VELO is both "Velo" and "Velodrome Finance"), so a ticker alone is not a
    # safe key: matching the wrong asset moves the expansion floor and silently
    # skips eligible names. Every ambiguous ticker is resolved against the last
    # close of the fixture we actually hold for that symbol.
    fixtures_dir = Path(args.fixtures_dir)
    included_mcaps = included_market_caps(snapshot, current_symbols, fixtures_dir)
    floor_mcap, floor_symbol = expansion_floor(included_mcaps)

    eligible_below = select_expansion_candidates(snapshot, current_symbols, floor_mcap)

    added = eligible_below[:args.batch_size]

    facts = coverage_facts(snapshot)
    reaches_floor = coverage_reaches_below_floor(snapshot, floor_mcap)

    print(f'Snapshot: {snapshot_path}')
    print(f'Coverage: {facts["entries_count"]} entries, '
          f'pages {facts["pages_fetched"]}/{facts["pages_requested"]}, '
          f'lowest covered rank {facts["lowest_rank_covered"]} '
          f'(${facts["lowest_market_cap_usd"]:,})')
    print(f'Current universe ({len(current_symbols)}): {current_symbols}')
    print(f'Included market caps (fresh snapshot): {included_mcaps}')
    print(f'Expansion floor (lowest included mcap): {floor_mcap} ({floor_symbol})')
    if not reaches_floor:
        print(f'WARNING: the ranking pass stops at ${facts["lowest_market_cap_usd"]:,}, '
              f'which is ABOVE the expansion floor ${floor_mcap:,}.')
        print('         The band below the floor was NOT observed, so this pass cannot '
              'answer whether eligible names exist there.')
        print('         Fetch more pages before concluding that no eligible name is left.')
    print(f'Eligible unseen names below the floor: {len(eligible_below)}')
    print(f'New batch ({len(added)}):')
    for e in added:
        print(f"  #{e['rank']:>4} {e['symbol']:<8} mcap=${e['market_cap_usd']:,} "
              f"px={e['price_usd']} name={e['name']}")

    record = build_scan_record(
        snapshot, snapshot_path, current_symbols, floor_mcap, floor_symbol,
        eligible_below, added, snapshot['fetched_at'])
    # The 24 h bound is an invariant of the record: it is the time of the
    # ranking pass plus 24 h, never the end of the expansion. build_scan_record
    # leaves it empty while the band still holds names, and an empty bound
    # reads as "the gate is open" - which would allow a second provider pass
    # inside the window. Applying a frozen snapshot does not refresh the
    # ranking, so the bound of the pass that produced the snapshot applies.
    record['next_eligible_refresh_at'] = bound_after(
        record.get('scanned_at') or snapshot.get('fetched_at'))
    record_path.parent.mkdir(parents=True, exist_ok=True)
    with open(record_path, 'w') as f:
        json.dump(record, f, indent=2)
    print(f'Scan record: {record_path} (state={record["state"]}, '
          f'next eligible refresh {record["next_eligible_refresh_at"]})')

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
        # The record must not contradict the ranking it describes: the names of
        # the batch are in the universe from now on.
        record['universe_n'] = len(expanded)
        with open(record_path, 'w') as f:
            json.dump(record, f, indent=2)
        print(f'\nUpdated {mcap_path}: {len(current_symbols)} -> {len(expanded)} symbols')
    elif not args.apply:
        print('\n(dry run: pass --apply to write the expanded ranking)')


if __name__ == '__main__':
    main()
