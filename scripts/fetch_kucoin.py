#!/usr/bin/env python3
"""Fetch longer hourly OHLCV history from KuCoin public API for top-N market-cap crypto symbols.

KuCoin /api/v1/market/candles returns at most 1500 bars per request, ordered most-recent
first. This script paginates backwards in time to collect months-to-years of hourly bars
per symbol and writes CSV fixtures to data/fixtures/.

Source: KuCoin spot market data API (public, no auth required).
Timezone: all timestamps are UTC epoch seconds (exchange standard).
"""
import argparse
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import pandas as pd
import requests

KUCOIN_CANDLES_URL = "https://api.kucoin.com/api/v1/market/candles"
MAX_PER_REQUEST = 100  # KuCoin public endpoint caps at 100 bars per request
REQUEST_TIMEOUT = 30
PAUSE_SECONDS = 0.4  # be polite to public API

# The public candles endpoint intermittently answers "400100" (symbol does not
# exist) for symbols that do exist - in batch 12 that was transient for all six
# affected names. Transient failures are therefore retried before a symbol is
# treated as unusable.
MAX_RETRIES = 5
RETRY_BACKOFF_SECONDS = 3.0


def fetch_candles(symbol: str, start_at: int = None, end_at: int = None,
                  limit: int = MAX_PER_REQUEST) -> list:
    """Fetch one page of candles. Returns list of [start_time, open, high, low, close, volume, quote_volume]."""
    params = {"symbol": symbol, "type": "1hour", "limit": limit}
    if start_at is not None:
        params["startAt"] = start_at
    if end_at is not None:
        params["endAt"] = end_at
    last_error = None
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(KUCOIN_CANDLES_URL, params=params, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            payload = resp.json()
        except (requests.RequestException, ValueError) as exc:
            last_error = exc
        else:
            if payload.get("code") == "200000":
                return payload.get("data", []) or []
            last_error = RuntimeError(f"KuCoin error for {symbol}: {payload}")
        sleep_for = RETRY_BACKOFF_SECONDS * (2 ** attempt)
        print(f"  retry {attempt + 1}/{MAX_RETRIES} in {sleep_for:.0f}s ({last_error})", flush=True)
        time.sleep(sleep_for)
    raise RuntimeError(f"KuCoin fetch failed for {symbol} after {MAX_RETRIES} attempts: {last_error}")


def fetch_full_history(symbol: str, target_bars: int, end_ts: int = None) -> pd.DataFrame:
    """Paginate backwards from end_ts (or now) until target_bars collected or history exhausted.

    KuCoin does not always honour the requested page size: a `limit=100` request can
    come back with 99 rows (e.g. when the requested end timestamp falls on a bar that
    is excluded from the response). Treating any short page as "end of history" used
    to truncate the download to that first page - CRO/USDT was fetched with only 99
    hourly bars instead of 22 000. Pagination therefore now stops only when the API
    returns nothing, when the oldest bar stops advancing, or when the target is met.
    """
    all_rows = []
    current_end = end_ts
    last_oldest = None
    while len(all_rows) < target_bars:
        rows = fetch_candles(symbol, end_at=current_end, limit=MAX_PER_REQUEST)
        if not rows:
            break
        all_rows.extend(rows)
        oldest_ts = int(rows[-1][0])
        # Guard against an infinite loop if the API keeps returning the same page
        if last_oldest is not None and oldest_ts >= last_oldest:
            break
        last_oldest = oldest_ts
        current_end = oldest_ts - 1
        time.sleep(PAUSE_SECONDS)
    if not all_rows:
        return pd.DataFrame(columns=["timestamp", "open", "high", "low", "close", "volume"])
    # KuCoin candle format: [start, open, close, high, low, volume, quote_amount]
    df = pd.DataFrame(all_rows, columns=["start", "open", "close", "high", "low", "volume", "quote_volume"])
    df["timestamp"] = pd.to_datetime(df["start"].astype(int), unit="s", utc=True)
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["open", "high", "low", "close", "timestamp"])
    df = df.sort_values("timestamp").drop_duplicates(subset=["timestamp"]).reset_index(drop=True)
    return df[["timestamp", "open", "high", "low", "close", "volume"]]


def main():
    parser = argparse.ArgumentParser(description="Fetch hourly OHLCV from KuCoin for crypto symbols")
    parser.add_argument("--symbols", nargs="*", default=["BTC/USDT", "ETH/USDT", "SOL/USDT", "BNB/USDT", "XRP/USDT"])
    parser.add_argument("--target-bars", type=int, default=12000,
                        help="Approximate number of hourly bars to collect per symbol (default 12000 ~ 10 months)")
    parser.add_argument("--output-dir", type=str, default="data/fixtures")
    parser.add_argument("--reconcile-manifest", action="store_true",
                        help="Only rebuild data/fixtures/fetch_manifest.json from the fixtures "
                             "on disk, adding rows for symbols that are missing from it")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.reconcile_manifest:
        reconcile_manifest(out_dir, out_dir / "fetch_manifest.json")
        return

    # Merge with any existing manifest so expanding the universe does not drop
    # provenance rows for symbols fetched in earlier batches.
    manifest_path = out_dir / "fetch_manifest.json"
    manifest = []
    if manifest_path.exists():
        try:
            with open(manifest_path) as f:
                manifest = json.load(f)
        except Exception:
            manifest = []
    manifest_by_symbol = {m.get('symbol'): m for m in manifest if isinstance(m, dict)}

    failed = []
    for sym in args.symbols:
        kucoin_sym = sym.replace("/", "-")
        print(f"Fetching {sym} (KuCoin {kucoin_sym}) target={args.target_bars} bars ...")
        try:
            df = fetch_full_history(kucoin_sym, target_bars=args.target_bars)
        except RuntimeError as exc:
            # One bad symbol must not abort the rest of the batch. The failure is
            # reported so it can be re-queried or documented as ineligible.
            print(f"  ERROR: {exc}")
            failed.append(sym)
            continue
        if df.empty:
            print(f"  WARNING: no data for {sym}")
            failed.append(sym)
            continue
        out_path = out_dir / f"{sym.replace('/', '_')}.csv"
        df.to_csv(out_path, index=False)
        print(f"  -> {out_path} rows={len(df)} span={df['timestamp'].min()} .. {df['timestamp'].max()}")
        manifest_by_symbol[sym] = {
            "symbol": sym,
            "source": "KuCoin public API /api/v1/market/candles",
            "interval": "1hour",
            "timezone": "UTC",
            "rows": len(df),
            "start": str(df["timestamp"].min()),
            "end": str(df["timestamp"].max()),
            "file": str(out_path),
        }
        time.sleep(PAUSE_SECONDS)

    merged = [manifest_by_symbol[k] for k in sorted(manifest_by_symbol)]
    with open(manifest_path, "w") as f:
        json.dump(merged, f, indent=2, default=str)
    print(f"\nManifest written to {manifest_path} ({len(merged)} symbols)")
    if failed:
        print(f"FAILED symbols ({len(failed)}): {failed} - re-query these before "
              f"treating them as ineligible")


def reconcile_manifest(out_dir: Path, manifest_path: Path) -> int:
    """Add manifest rows for fixtures that are missing from the manifest.

    A fixture is only ever written by this script from the KuCoin public
    candles API, so the provenance of an existing file can be recovered from
    the file itself. This keeps the manifest complete when symbols are fetched
    in separate batches.
    """
    manifest = []
    if manifest_path.exists():
        try:
            with open(manifest_path) as f:
                manifest = json.load(f)
        except Exception:
            manifest = []
    by_symbol = {m.get("symbol"): m for m in manifest if isinstance(m, dict)}

    added = 0
    for csv_path in sorted(out_dir.glob("*_USDT.csv")):
        symbol = csv_path.stem.replace("_", "/")
        if symbol in by_symbol:
            continue
        df = pd.read_csv(csv_path)
        if "timestamp" not in df.columns or df.empty:
            continue
        by_symbol[symbol] = {
            "symbol": symbol,
            "source": "KuCoin public API /api/v1/market/candles",
            "interval": "1hour",
            "timezone": "UTC",
            "rows": len(df),
            "start": str(df["timestamp"].min()),
            "end": str(df["timestamp"].max()),
            "file": str(csv_path),
        }
        added += 1
        print(f"  + {symbol} rows={len(df)} span={df['timestamp'].min()} .. {df['timestamp'].max()}")

    merged = [by_symbol[k] for k in sorted(by_symbol)]
    with open(manifest_path, "w") as f:
        json.dump(merged, f, indent=2, default=str)
    print(f"Manifest reconciled: {len(merged)} symbols ({added} added)")
    return added


if __name__ == "__main__":
    main()