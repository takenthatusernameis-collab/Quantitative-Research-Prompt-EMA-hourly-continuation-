"""Signal generation for EMA hourly continuation strategy."""
from typing import Optional, List, Dict
import pandas as pd
import numpy as np


def generate_signals(df: pd.DataFrame, ema50_period: int = 50, ema100_period: int = 100, stricter_trend: bool = False) -> pd.DataFrame:
    df = df.copy()
    df['ema50'] = df['close'].ewm(span=ema50_period, adjust=False).mean()
    df['ema100'] = df['close'].ewm(span=ema100_period, adjust=False).mean()
    df['signal'] = 0
    df['entry_price'] = np.nan

    for i in range(ema100_period, len(df)):
        ema50_t = df['ema50'].iloc[i]
        ema100_t = df['ema100'].iloc[i]
        close_t = df['close'].iloc[i]
        close_t1 = df['close'].iloc[i - 1]
        ema50_t1 = df['ema50'].iloc[i - 1]

        if abs(ema50_t - ema100_t) < 1e-12 or pd.isna(ema50_t) or pd.isna(ema100_t):
            continue

        if ema50_t > ema100_t:
            if close_t1 <= ema50_t1 + 1e-12 and close_t > ema50_t:
                if stricter_trend and not (close_t > ema100_t):
                    continue
                df.at[i, 'signal'] = 1
                df.at[i, 'entry_price'] = close_t
        elif ema50_t < ema100_t:
            if close_t1 >= ema50_t1 - 1e-12 and close_t < ema50_t:
                if stricter_trend and not (close_t < ema100_t):
                    continue
                df.at[i, 'signal'] = -1
                df.at[i, 'entry_price'] = close_t

    return df
