"""Data loading utilities for OHLCV data."""
from typing import Optional, Dict, Any
import pandas as pd
from pathlib import Path


def load_ohlcv_csv(path: str | Path, timestamp_col: str = 'timestamp') -> pd.DataFrame:
    """
    Load OHLCV data from CSV.

    Expected columns: timestamp/date/time, open, high, low, close, volume
    """
    path = Path(path)
    df = pd.read_csv(path)

    # Normalize column names
    col_map = {}
    for c in df.columns:
        cl = c.lower()
        if cl in ('timestamp', 'date', 'time', 'datetime'):
            col_map[c] = 'timestamp'
        elif cl == 'open':
            col_map[c] = 'open'
        elif cl == 'high':
            col_map[c] = 'high'
        elif cl == 'low':
            col_map[c] = 'low'
        elif cl == 'close':
            col_map[c] = 'close'
        elif cl in ('volume', 'vol'):
            col_map[c] = 'volume'

    if col_map:
        df = df.rename(columns=col_map)

    # Ensure required columns exist
    required = ['open', 'high', 'low', 'close']
    for r in required:
        if r not in df.columns:
            raise ValueError(f"Missing required column: {r}")

    if 'timestamp' in df.columns:
        try:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
        except Exception:
            pass

    # Sort by timestamp if present
    if 'timestamp' in df.columns:
        df = df.sort_values('timestamp').reset_index(drop=True)
    else:
        df = df.reset_index(drop=True)

    # Ensure numeric types
    for col in ['open', 'high', 'low', 'close', 'volume']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna(subset=['open', 'high', 'low', 'close'])
    return df
