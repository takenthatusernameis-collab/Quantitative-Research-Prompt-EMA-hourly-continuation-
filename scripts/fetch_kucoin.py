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


def fetch_candles(symbol: str, start_at: int = None, end_at: int = None,
                  limit: int = MAX_PER_REQUEST) -> list:
    """Fetch one page of candles. Returns list of [start_time, open, high, low, close, volume, quote_volume]."""
    params = {"symbol": symbol, "type": "1hour", "limit": limit}
    if start_at is not None:
        params["startAt"] = start_at
    if end_at is not None:
        params["endAt"] = end_at
    resp = requests.get(KUCOIN_CANDLES_URL, params=params, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("code") != "200000":
        raise RuntimeError(f"KuCoin error for {symbol}: {payload}")
    return payload.get("data", []) or []


def fetch_full_history(symbol: str, target_bars: int, end_ts: int = None) -> pd.DataFrame:
    """Paginate backwards from end_ts (or now) until target_bars collected or history exhausted."""
    all_rows = []
    current_end = end_ts
    last_oldest = None
    while len(all_rows) < target_bars:
        rows = fetch_candles(symbol, end_at=current_end, limit=MAX_PER_REQUEST)
        if not rows:
            break
        all_rows.extend(rows)
        oldest_ts = int(rows[-1][0])
        # If the API returned fewer than requested, we've likely hit the beginning of history
        if len(rows) < MAX_PER_REQUEST:
            break
        # Guard against infinite loop if the same oldest bar repeats
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
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = []
    for sym in args.symbols:
        kucoin_sym = sym.replace("/", "-")
        print(f"Fetching {sym} (KuCoin {kucoin_sym}) target={args.target_bars} bars ...")
        df = fetch_full_history(kucoin_sym, target_bars=args.target_bars)
        if df.empty:
            print(f"  WARNING: no data for {sym}")
            continue
        out_path = out_dir / f"{sym.replace('/', '_')}.csv"
        df.to_csv(out_path, index=False)
        print(f"  -> {out_path} rows={len(df)} span={df['timestamp'].min()} .. {df['timestamp'].max()}")
        manifest.append({
            "symbol": sym,
            "source": "KuCoin public API /api/v1/market/candles",
            "interval": "1hour",
            "timezone": "UTC",
            "rows": len(df),
            "start": str(df["timestamp"].min()),
            "end": str(df["timestamp"].max()),
            "file": str(out_path),
        })
        time.sleep(PAUSE_SECONDS)

    manifest_path = out_dir / "fetch_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2, default=str)
    print(f"\nManifest written to {manifest_path}")


if __name__ == "__main__":
    main()