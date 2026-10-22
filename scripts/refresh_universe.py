#!/usr/bin/env python3
"""Gated universe refresh and grid expansion (PROMPT.md §2.1).

The working universe of this program is append-only, and its refresh is
bounded: PROMPT.md §2.1.5 requires the market-cap ranking to be refreshed at
least once every 24 h and not more often than that while the program waits
for new candidates. This script is the single entry point for that work, so
the bound is enforced by code instead of by memory, and one refresh cycle is
reproducible from the command line.

Phases (in this order, or `all` for the whole cycle):

  plan      Offline. Reports the recorded state, whether a refresh is allowed
            right now, and which symbols still need a fixture or a grid. Never
            touches the network.
  fetch     Exactly one CoinGecko ranking pass. Freezes the snapshot to
            universe/mcap_snapshot_<TS>.json, appends the selected batch to
            universe/mcap_rank.json (append-only, descending market cap) and
            writes the scan record. Refuses to run before the recorded bound
            has elapsed.
  fixtures  Hourly KuCoin fixtures for the NEW symbols only. The fixture of a
            symbol the grid already ran is never re-fetched: that would move
            the bar sequence and make the stored cells stale (see
            scripts/verify_grid_repro.py).
  grid      Expands the grid with the new symbols through the repository's own
            resume path (scripts/run_grid.py --resume), one symbol at a time,
            in descending market-cap order.
  state     Verifies the grid and rewrites universe/last_scan.json.
  log       Appends the expansion to universe/mcap_expansion_log.md.
  all       fetch -> fixtures -> grid -> state -> log.

Usage:
    PYTHONPATH=. python3 scripts/refresh_universe.py plan
    PYTHONPATH=. python3 scripts/refresh_universe.py fetch --pages 10 --batch-size 10
    PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
    PYTHONPATH=. python3 scripts/refresh_universe.py grid
    PYTHONPATH=. python3 scripts/refresh_universe.py state
    PYTHONPATH=. python3 scripts/refresh_universe.py all
"""
import argparse
import json
import math
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from scripts import fetch_kucoin as fk
from scripts import fetch_mcap_snapshot as fms
from scripts.run_grid import GRID_PAIRS

DEFAULT_SCAN_PATH = 'universe/last_scan.json'
DEFAULT_RANKING_PATH = 'universe/mcap_rank.json'
DEFAULT_SNAPSHOT_DIR = 'universe'
DEFAULT_FIXTURE_DIR = 'data/fixtures'
DEFAULT_GRID_RUN = 'results/20261019_135940_grid'
DEFAULT_LOG_PATH = 'universe/mcap_expansion_log.md'

# PROMPT.md §2.1.5: refresh the ranking at least once every 24 h, and not on
# every agent activation.
REFRESH_INTERVAL_HOURS = 24

DEFAULT_PAGES = 10
DEFAULT_BATCH_SIZE = 10

# The hourly history a new symbol needs: the same depth as the existing
# universe (2 years = 17 520 hourly bars), which is what
# fetch_mcap_snapshot.MIN_HISTORY_YEARS checks before a name is eligible.
DEFAULT_TARGET_BARS = 22000
MIN_REQUIRED_BARS = 17520

# |log(kucoin price / ranked price)| tolerance for the price-identity check.
PRICE_MATCH_TOLERANCE = 0.20

HOUR = timedelta(hours=1)


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------

def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_iso(value):
    """Parse an ISO-8601 timestamp into an aware UTC datetime."""
    if value is None:
        return None
    text = str(value).strip()
    if text.endswith('Z'):
        text = text[:-1] + '+00:00'
    stamp = datetime.fromisoformat(text)
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return stamp.astimezone(timezone.utc)


def iso(stamp) -> str:
    return stamp.astimezone(timezone.utc).isoformat()


def read_json(path):
    path = Path(path)
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def write_json(path, payload) -> None:
    """Write JSON atomically; a half-written state file must never be read."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(payload, indent=2))
    tmp.replace(path)


# --------------------------------------------------------------------------
# the refresh gate
# --------------------------------------------------------------------------

def gate_status(state: dict, now=None) -> dict:
    """Is a market-cap refresh allowed at `now`?

    `next_eligible_refresh_at` is the bound of PROMPT.md §2.1.5: 24 h after
    the last pass, while the program waits for new candidates. A record
    without a bound means the ranking band was not exhausted at the last pass,
    so the next pass may run at any time - the frozen snapshot of that pass is
    what the expansion works on.
    """
    now = now or datetime.now(timezone.utc)
    bound = state.get('next_eligible_refresh_at')
    if not bound:
        return {'eligible': True, 'bound': None, 'now': iso(now),
                'reason': 'no refresh bound recorded (the ranking band was not exhausted)'}
    due = parse_iso(bound)
    if now >= due:
        return {'eligible': True, 'bound': bound, 'now': iso(now),
                'reason': f'the 24 h refresh bound {bound} has elapsed'}
    return {'eligible': False, 'bound': bound, 'now': iso(now),
            'reason': f'the 24 h refresh bound {bound} has not elapsed yet'}


def require_open_gate(state: dict, now=None, override_reason=None) -> dict:
    """Raise SystemExit unless a refresh is allowed right now."""
    gate = gate_status(state, now)
    if gate['eligible']:
        return gate
    if not override_reason:
        raise SystemExit(
            f'refresh refused: {gate["reason"]}. The ranking must not be queried '
            f'more than once per 24 h (PROMPT.md §2.1.5). Use --override-gate '
            f'"<reason>" to override this deliberately.')
    return gate


# --------------------------------------------------------------------------
# what is still missing
# --------------------------------------------------------------------------

def fixture_path(fixture_dir, symbol: str) -> Path:
    return Path(fixture_dir) / f"{symbol.replace('/', '_')}.csv"


def cell_dir(grid_run, symbol: str, fast: int, slow: int) -> Path:
    return Path(grid_run) / 'results' / symbol.replace('/', '_') / f'P{fast}_{slow}'


def symbols_without_fixture(ranking_symbols, fixture_dir) -> list:
    """Ranking symbols that have no hourly fixture on disk yet."""
    return [s for s in ranking_symbols
            if not fixture_path(fixture_dir, s).exists()]


def symbol_cell_status(grid_run, symbol: str, pairs=GRID_PAIRS) -> dict:
    """How many grid cells of one symbol exist, and how many are blocked."""
    done = 0
    blocked = 0
    missing = []
    for (fast, slow) in pairs:
        cell = cell_dir(grid_run, symbol, fast, slow)
        if (cell / 'summary.json').exists():
            done += 1
        elif (cell / 'blocked.json').exists():
            blocked += 1
        else:
            missing.append(f'P{fast}_{slow}')
    return {'symbol': symbol, 'cells': done, 'blocked': blocked,
            'missing': missing, 'expected': len(pairs)}


def symbols_without_cells(ranking_symbols, grid_run, pairs=GRID_PAIRS) -> list:
    """Ranking symbols whose grid is not complete yet."""
    return [s for s in ranking_symbols
            if symbol_cell_status(grid_run, s, pairs)['cells'] < len(pairs)]


def snapshot_price(snapshot: dict, symbol: str):
    """The ranked price of a symbol in the frozen snapshot (None when unknown)."""
    ticker = symbol.split('/')[0].upper()
    entries = [e for e in (snapshot.get('entries') or [])
               if e.get('symbol') == ticker and e.get('exclusion_reason') is None]
    if not entries:
        entries = [e for e in (snapshot.get('entries') or [])
                   if e.get('symbol') == ticker]
    if not entries:
        return None
    return entries[0].get('price_usd')


# --------------------------------------------------------------------------
# fixture integrity
# --------------------------------------------------------------------------

def validate_fixture(df, snapshot_price=None, min_bars=MIN_REQUIRED_BARS,
                     tolerance=PRICE_MATCH_TOLERANCE) -> dict:
    """Integrity checks for a freshly fetched hourly fixture.

    These are the checks the expansion log records for every batch: enough
    bars for the grid, no duplicate timestamps, a contiguous hourly grid, valid
    OHLC rows, and - when the ranked price is known - that the fetched pair
    trades the asset the ranking described.
    """
    rows = int(len(df))
    checks = {'rows': rows, 'min_bars': min_bars, 'enough_bars': rows >= min_bars}

    if rows:
        timestamps = pd.to_datetime(df['timestamp'], utc=True)
        checks['duplicate_timestamps'] = int(timestamps.duplicated().sum())
        diffs = timestamps.diff().dropna()
        checks['non_hourly_steps'] = int((diffs != HOUR).sum()) if len(diffs) else 0
    else:
        checks['duplicate_timestamps'] = 0
        checks['non_hourly_steps'] = 0

    invalid = 0
    if rows:
        o = df['open'].astype(float)
        h = df['high'].astype(float)
        lo = df['low'].astype(float)
        c = df['close'].astype(float)
        bad = ((h < lo) | (h < o) | (h < c) | (lo > o) | (lo > c)
               | (o <= 0) | (c <= 0) | (h <= 0) | (lo <= 0)
               | df[['open', 'high', 'low', 'close']].isna().any(axis=1))
        invalid = int(bad.sum())
    checks['invalid_ohlc_rows'] = invalid

    last_close = float(df['close'].iloc[-1]) if rows else 0.0
    checks['last_close'] = last_close
    if snapshot_price and last_close > 0 and float(snapshot_price) > 0:
        ratio = abs(math.log(last_close / float(snapshot_price)))
        checks['price_identity_log_ratio'] = ratio
        checks['price_identity_ok'] = ratio <= tolerance
    else:
        checks['price_identity_log_ratio'] = None
        checks['price_identity_ok'] = None

    checks['ok'] = bool(
        checks['enough_bars']
        and checks['duplicate_timestamps'] == 0
        and checks['non_hourly_steps'] == 0
        and checks['invalid_ohlc_rows'] == 0
        and checks['price_identity_ok'] is not False)
    return checks


def update_manifest(fixture_dir, symbol: str, df, path) -> dict:
    """Add or refresh the provenance row of one fixture."""
    manifest_path = Path(fixture_dir) / 'fetch_manifest.json'
    rows = read_json(manifest_path) if manifest_path.exists() else []
    by_symbol = {r.get('symbol'): r for r in rows if isinstance(r, dict)}
    row = {
        'symbol': symbol,
        'source': 'KuCoin public API /api/v1/market/candles',
        'interval': '1hour',
        'timezone': 'UTC',
        'rows': int(len(df)),
        'start': str(df['timestamp'].min()),
        'end': str(df['timestamp'].max()),
        'file': str(path),
    }
    by_symbol[symbol] = row
    merged = [by_symbol[k] for k in sorted(by_symbol)]
    write_json(manifest_path, merged)
    return row


# --------------------------------------------------------------------------
# phases
# --------------------------------------------------------------------------

def phase_plan(args) -> dict:
    state = read_json(args.scan)
    ranking = read_json(args.ranking)
    symbols = list(ranking.get('symbols', []))
    gate = gate_status(state, args.now)
    pending_fixtures = symbols_without_fixture(symbols, args.fixture_dir)
    pending_cells = symbols_without_cells(symbols, args.grid_run)
    report = {
        'scan_state': state.get('state'),
        'universe_n': len(symbols),
        'expansion_floor': state.get('expansion_floor'),
        'snapshot_id': state.get('snapshot_id'),
        'next_eligible_refresh_at': state.get('next_eligible_refresh_at'),
        'refresh_allowed_now': gate['eligible'],
        'refresh_reason': gate['reason'],
        'symbols_without_fixture': pending_fixtures,
        'symbols_without_grid_cells': pending_cells,
        'grid_run': str(args.grid_run),
    }
    print(json.dumps(report, indent=2))
    return report


def phase_fetch(args) -> dict:
    """One ranking pass, one frozen snapshot, one append-only expansion."""
    state = read_json(args.scan)
    gate = require_open_gate(state, args.now, args.override_reason)

    ranking = read_json(args.ranking)
    current_symbols = list(ranking.get('symbols', []))
    fixtures_dir = Path(args.fixture_dir)

    snapshot = fms.build_snapshot(args.pages)
    now = args.now or datetime.now(timezone.utc)
    snapshot_path = Path(args.snapshot_dir) / f'mcap_snapshot_{now.strftime("%Y%m%d_%H%M%S")}.json'
    write_json(snapshot_path, snapshot)

    included = fms.included_market_caps(snapshot, current_symbols, fixtures_dir)
    floor_mcap, floor_symbol = fms.expansion_floor(included)
    eligible = fms.select_expansion_candidates(snapshot, current_symbols, floor_mcap)
    batch = eligible[:args.batch_size]

    record = fms.build_scan_record(snapshot, snapshot_path, current_symbols, floor_mcap,
                                   floor_symbol, eligible, batch, snapshot['fetched_at'])
    scanned_at = parse_iso(snapshot['fetched_at'])
    # One pass per refresh cycle: the bound is recorded even when the band
    # still holds names, because the batch below is expanded from this frozen
    # snapshot and not from a second ranking pass.
    record['next_eligible_refresh_at'] = iso(scanned_at + timedelta(hours=REFRESH_INTERVAL_HOURS))
    record['refresh_gate'] = {'eligible': gate['eligible'], 'reason': gate['reason'],
                               'override_reason': args.override_reason}
    write_json(args.scan, record)

    print(f'Snapshot: {snapshot_path}')
    print(f'Coverage: {record["coverage"]["entries_count"]} entries, '
          f'pages {record["coverage"]["pages_fetched"]}/{record["coverage"]["pages_requested"]}, '
          f'lowest covered rank {record["coverage"]["lowest_rank_covered"]} '
          f'(${record["coverage"]["lowest_market_cap_usd"]:,})')
    print(f'Expansion floor: ${floor_mcap:,} ({floor_symbol})')
    print(f'Eligible unseen names below the floor: {len(eligible)}')
    print(f'Batch selected: {len(batch)}')
    for e in batch:
        print(f"  #{e['rank']:>4} {e['symbol']:<8} mcap=${e['market_cap_usd']:,} "
              f"px={e['price_usd']} name={e['name']}")
    print(f'Next eligible refresh: {record["next_eligible_refresh_at"]}')

    if not batch:
        record['universe_n'] = len(current_symbols)
        write_json(args.scan, record)
        print('No eligible new name below the floor: the band is exhausted, the '
              'program waits for the next refresh.')
        return record

    added = [f"{e['symbol']}/USDT" for e in batch]
    payload = {
        'updated_at': iso(now),
        'snapshot_id': snapshot_path.stem,
        'snapshot_source': snapshot['source'],
        'snapshot_fetched_at': snapshot['fetched_at'],
        'n_symbols': len(current_symbols) + len(added),
        'added_in_this_expansion': added,
        'added_market_caps_usd': {e['symbol']: e['market_cap_usd'] for e in batch},
        'symbols': current_symbols + added,
    }
    write_json(args.ranking, payload)
    record['universe_n'] = len(current_symbols) + len(added)
    write_json(args.scan, record)
    print(f'Ranking updated: {len(current_symbols)} -> {len(current_symbols) + len(added)} symbols')
    return record


def phase_fixtures(args) -> dict:
    """Hourly fixtures for the new symbols only."""
    ranking = read_json(args.ranking)
    symbols = list(ranking.get('symbols', []))
    pending = symbols_without_fixture(symbols, args.fixture_dir)
    state = read_json(args.scan)
    snapshot = read_json(state.get('snapshot_path') or '')

    print(f'Symbols without a fixture: {len(pending)}')
    results = []
    for symbol in pending:
        price = snapshot_price(snapshot, symbol)
        print(f'Fetching {symbol} (KuCoin {symbol.replace("/", "-")}) '
              f'target={args.target_bars} bars ...')
        try:
            df = fk.fetch_full_history(symbol.replace('/', '-'),
                                       target_bars=args.target_bars)
        except Exception as exc:
            print(f'  ERROR {symbol}: {exc}')
            results.append({'symbol': symbol, 'ok': False, 'error': str(exc)})
            continue
        if df is None or df.empty:
            print(f'  WARNING {symbol}: no data')
            results.append({'symbol': symbol, 'ok': False, 'error': 'no data'})
            continue

        checks = validate_fixture(df, price, min_bars=args.min_bars)
        if not checks['ok']:
            print(f'  REJECTED {symbol}: {checks}')
            results.append({'symbol': symbol, 'ok': False, 'checks': checks})
            continue

        path = fixture_path(args.fixture_dir, symbol)
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
        update_manifest(args.fixture_dir, symbol, df, path)
        print(f'  -> {path} rows={len(df)} span={df["timestamp"].min()} .. {df["timestamp"].max()}')
        results.append({'symbol': symbol, 'ok': True, 'checks': checks,
                        'rows': int(len(df))})

    state['fixtures'] = {
        'fetched_at': iso(args.now or datetime.now(timezone.utc)),
        'target_bars': args.target_bars,
        'results': results,
    }
    write_json(args.scan, state)
    failed = [r['symbol'] for r in results if not r['ok']]
    if failed:
        print(f'FAILED symbols (re-query before treating them as ineligible): {failed}')
    return {'results': results, 'failed': failed}


def phase_grid(args) -> dict:
    """Expand the grid with the new symbols through the repository's resume path."""
    ranking = read_json(args.ranking)
    symbols = list(ranking.get('symbols', []))
    state = read_json(args.scan)
    pending = symbols_without_cells(symbols, args.grid_run)
    previous_n = len(symbols) - len(pending)

    print(f'Symbols without a complete grid: {len(pending)}')
    env = dict(os.environ)
    env['PYTHONPATH'] = str(repo_root())
    outcomes = []
    for symbol in pending:
        index = symbols.index(symbol)
        note = (f'universe expansion: N {previous_n} -> {len(symbols)} '
                f'({symbol}, 66-pair EMA grid); snapshot {state.get("snapshot_id")}')
        cmd = [sys.executable, 'scripts/run_grid.py', '--resume', str(args.grid_run),
               '--n', str(index + 1), '--note', note]
        print(f'Running: {" ".join(cmd)}')
        subprocess.run(cmd, check=True, cwd=str(repo_root()), env=env)
        status = symbol_cell_status(args.grid_run, symbol)
        print(f'  {symbol}: {status["cells"]}/{status["expected"]} cells, '
              f'{status["blocked"]} blocked')
        outcomes.append(status)

    state['grid_expansion'] = {
        'run': str(args.grid_run),
        'expanded_at': iso(args.now or datetime.now(timezone.utc)),
        'previous_n': previous_n,
        'new_n': len(symbols),
        'symbols': [s for s in pending],
        'outcomes': outcomes,
    }
    write_json(args.scan, state)
    return {'outcomes': outcomes}


def phase_state(args) -> dict:
    """Verify the grid and rewrite the scan record."""
    ranking = read_json(args.ranking)
    symbols = list(ranking.get('symbols', []))
    state = read_json(args.scan)
    snapshot = read_json(state.get('snapshot_path') or '')

    total_cells = 0
    blocked = 0
    incomplete = []
    for symbol in symbols:
        status = symbol_cell_status(args.grid_run, symbol)
        total_cells += status['cells']
        blocked += status['blocked']
        if status['missing']:
            incomplete.append({'symbol': symbol, 'missing': status['missing']})

    included = fms.included_market_caps(snapshot, symbols, Path(args.fixture_dir))
    floor_mcap, floor_symbol = fms.expansion_floor(included)
    remaining = fms.select_expansion_candidates(snapshot, symbols, floor_mcap)

    now = args.now or datetime.now(timezone.utc)
    state['universe_n'] = len(symbols)
    state['expansion_floor'] = {'symbol': floor_symbol, 'market_cap_usd': floor_mcap}
    state['eligible_unseen_below_floor_count'] = len(remaining)
    state['eligible_unseen_below_floor'] = [
        {'rank': e['rank'], 'symbol': e['symbol'], 'name': e.get('name'),
         'market_cap_usd': e['market_cap_usd']} for e in remaining]
    state['state'] = ('EXPANSION_AVAILABLE' if remaining
                      else 'AWAITING_NEW_ELIGIBLE_CANDIDATES')
    # The 24 h bound of the refresh cycle is an invariant of the record: it is
    # always the time of the last pass plus 24 h, never the end of the
    # expansion. A record that lost it would allow a second ranking pass
    # inside the window.
    if not state.get('next_eligible_refresh_at') and state.get('scanned_at'):
        state['next_eligible_refresh_at'] = iso(
            parse_iso(state['scanned_at']) + timedelta(hours=REFRESH_INTERVAL_HOURS))
    state['grid_verification'] = {
        'run': str(args.grid_run),
        'verified_at': iso(now),
        'symbols': len(symbols),
        'cells_complete': total_cells,
        'cells_expected': len(symbols) * len(GRID_PAIRS),
        'cells_blocked': blocked,
        'incomplete_symbols': incomplete,
    }
    state['last_verified_at'] = iso(now)
    state['last_verification_note'] = args.verification_note or state.get('last_verification_note', '')
    write_json(args.scan, state)

    print(f'Universe N: {len(symbols)}')
    print(f'Grid cells: {total_cells}/{len(symbols) * len(GRID_PAIRS)}, blocked: {blocked}')
    if incomplete:
        print(f'Incomplete symbols: {[i["symbol"] for i in incomplete]}')
    print(f'Expansion floor: ${floor_mcap:,} ({floor_symbol})')
    print(f'Eligible unseen names below the floor: {len(remaining)}')
    print(f'State: {state["state"]}')
    print(f'Next eligible refresh: {state.get("next_eligible_refresh_at")}')
    return state


def symbol_outcome(grid_run, symbol: str) -> dict:
    """Summary of one symbol's grid cells (net of costs)."""
    cells = 0
    trades = 0
    pfs = []
    above_one = 0
    for (fast, slow) in GRID_PAIRS:
        summary = cell_dir(grid_run, symbol, fast, slow) / 'summary.json'
        if not summary.exists():
            continue
        data = read_json(summary)
        cells += 1
        trades += int(data.get('trade_count') or 0)
        pf = data.get('net_profit_factor')
        if pf is not None:
            pfs.append(float(pf))
            if float(pf) > 1.0:
                above_one += 1
    return {
        'symbol': symbol,
        'cells': cells,
        'trades': trades,
        'mean_net_pf': (sum(pfs) / len(pfs)) if pfs else None,
        'best_net_pf': max(pfs) if pfs else None,
        'cells_net_pf_above_1': above_one,
    }


def phase_log(args) -> str:
    """Append the expansion to the universe expansion log (PROMPT.md §2.1.6)."""
    ranking = read_json(args.ranking)
    symbols = list(ranking.get('symbols', []))
    state = read_json(args.scan)
    snapshot = read_json(state.get('snapshot_path') or '')
    expansion = state.get('grid_expansion') or {}
    added = list(ranking.get('added_in_this_expansion') or [])
    market_caps = ranking.get('added_market_caps_usd') or {}

    entries_by_symbol = {e['symbol']: e for e in (snapshot.get('entries') or [])}
    manifest = read_json(Path(args.fixture_dir) / 'fetch_manifest.json')
    rows_by_symbol = {row.get('symbol'): row.get('rows')
                      for row in (manifest if isinstance(manifest, list) else [])
                      if isinstance(row, dict)}
    lines = ['']
    lines.append('---')
    lines.append('')
    title = ', '.join(s.split('/')[0] for s in added) if added else '(no new names)'
    lines.append(f"## Expansion {state.get('snapshot_id')} - {title} "
                 f"(N {expansion.get('previous_n', len(symbols) - len(added))} -> {len(symbols)})")
    lines.append('')
    lines.append(f"**Source snapshot:** `{state.get('snapshot_path')}` "
                 f"({state.get('snapshot_source')}, fetched {state.get('scanned_at')}).")
    lines.append('')
    lines.append(f"**Expansion floor after the batch:** "
                 f"`{state.get('expansion_floor', {}).get('symbol')}` "
                 f"${state.get('expansion_floor', {}).get('market_cap_usd')}. "
                 f"`universe/last_scan.json` reports `universe_n={state.get('universe_n')}`, "
                 f"`eligible_unseen_below_floor_count={state.get('eligible_unseen_below_floor_count')}`.")
    lines.append('')
    lines.append('### Selection (descending market cap, strictly below the previous floor)')
    lines.append('')
    lines.append('| Rank in snapshot | Universe rank | Symbol | Name | Market cap (USD) | Fixture |')
    lines.append('|---|---|---|---|---|---|')
    for symbol in added:
        ticker = symbol.split('/')[0]
        entry = entries_by_symbol.get(ticker, {})
        mcap = market_caps.get(ticker)
        mcap_text = f'{mcap:,}' if isinstance(mcap, int) else 'n/a'
        lines.append(f"| {entry.get('rank', 'n/a')} | {symbols.index(symbol) + 1} | {symbol} | "
                     f"{entry.get('name', 'n/a')} | {mcap_text} | "
                     f"`{fixture_path(args.fixture_dir, symbol)}` "
                     f"({rows_by_symbol.get(symbol, 'n/a')} rows) |")
    lines.append('')
    lines.append('### Grid outcome (66 pairs per symbol, net of costs)')
    lines.append('')
    lines.append('| Symbol | Cells | Trades | Mean net PF | Best net PF | Cells net PF > 1 |')
    lines.append('|---|---|---|---|---|---|')
    for symbol in added:
        outcome = symbol_outcome(args.grid_run, symbol)
        mean_pf = ('n/a' if outcome['mean_net_pf'] is None
                  else f"{outcome['mean_net_pf']:.4f}")
        best_pf = ('n/a' if outcome['best_net_pf'] is None
                   else f"{outcome['best_net_pf']:.4f}")
        lines.append(f"| {symbol} | {outcome['cells']} | {outcome['trades']} | "
                     f"{mean_pf} | {best_pf} | {outcome['cells_net_pf_above_1']} |")
    lines.append('')
    verification = state.get('grid_verification') or {}
    lines.append('### Cumulative state after the batch')
    lines.append('')
    lines.append(f"- **{verification.get('cells_complete', 0)} / "
                 f"{verification.get('cells_expected', 0)} cells** complete "
                 f"({verification.get('symbols', len(symbols))} symbols x 66 EMA pairs), "
                 f"{verification.get('cells_blocked', 0)} blocked.")
    lines.append(f"- Eligible unseen names below the floor: "
                 f"**{state.get('eligible_unseen_below_floor_count')}**.")
    lines.append(f"- Next eligible refresh: **{state.get('next_eligible_refresh_at')}**.")
    lines.append('- The pooled report over the whole universe is produced with '
                 '`PYTHONPATH=. python3 scripts/aggregate_grid.py --run '
                 f'{args.grid_run}`.')
    lines.append('')

    section = '\n'.join(lines)
    log_path = Path(args.log)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, 'a') as fh:
        fh.write(section)
    print(f'Appended the expansion to {log_path}')
    return section


PHASES = {
    'plan': phase_plan,
    'fetch': phase_fetch,
    'fixtures': phase_fixtures,
    'grid': phase_grid,
    'state': phase_state,
    'log': phase_log,
}


def run_phase(name, args) -> dict:
    return PHASES[name](args)


def main():
    parser = argparse.ArgumentParser(description='Gated universe refresh and grid expansion')
    parser.add_argument('phase', choices=list(PHASES) + ['all'])
    parser.add_argument('--scan', type=str, default=DEFAULT_SCAN_PATH)
    parser.add_argument('--ranking', type=str, default=DEFAULT_RANKING_PATH)
    parser.add_argument('--snapshot-dir', type=str, default=DEFAULT_SNAPSHOT_DIR)
    parser.add_argument('--fixture-dir', type=str, default=DEFAULT_FIXTURE_DIR)
    parser.add_argument('--grid-run', type=str, default=DEFAULT_GRID_RUN)
    parser.add_argument('--log', type=str, default=DEFAULT_LOG_PATH)
    parser.add_argument('--pages', type=int, default=DEFAULT_PAGES)
    parser.add_argument('--batch-size', type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument('--target-bars', type=int, default=DEFAULT_TARGET_BARS)
    parser.add_argument('--min-bars', type=int, default=MIN_REQUIRED_BARS,
                        help='Minimum hourly bars a new fixture must carry to be eligible.')
    parser.add_argument('--now', type=str, default=None,
                        help='Override the current time (ISO-8601). Used by the tests.')
    parser.add_argument('--override-gate', action='store_true', default=False,
                        help='Refresh before the recorded 24 h bound has elapsed.')
    parser.add_argument('--override-reason', type=str, default=None,
                        help='Why the 24 h bound is overridden; required with --override-gate.')
    parser.add_argument('--verification-note', type=str, default=None)
    args = parser.parse_args()

    if args.now:
        args.now = parse_iso(args.now)

    if args.phase == 'all':
        for name in ('fetch', 'fixtures', 'grid', 'state', 'log'):
            print(f'=== phase {name} ===')
            run_phase(name, args)
        return

    run_phase(args.phase, args)


if __name__ == '__main__':
    main()
