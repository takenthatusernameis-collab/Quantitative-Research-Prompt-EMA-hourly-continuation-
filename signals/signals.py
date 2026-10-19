"""Signal generation for EMA hourly continuation strategy."""
from typing import Optional, List, Dict
import pandas as pd
import numpy as np


def generate_signals(df: pd.DataFrame, ema_fast_period: int = 50, ema_slow_period: int = 100,
                     stricter_trend: bool = False) -> pd.DataFrame:
    df = df.copy()
    df['ema_fast'] = df['close'].ewm(span=ema_fast_period, adjust=False).mean()
    df['ema_slow'] = df['close'].ewm(span=ema_slow_period, adjust=False).mean()
    df['signal'] = 0
    df['entry_price'] = np.nan

    warmup = max(ema_fast_period, ema_slow_period)
    for i in range(warmup, len(df)):
        ema_fast_t = df['ema_fast'].iloc[i]
        ema_slow_t = df['ema_slow'].iloc[i]
        close_t = df['close'].iloc[i]
        close_t1 = df['close'].iloc[i - 1]
        ema_fast_t1 = df['ema_fast'].iloc[i - 1]

        if abs(ema_fast_t - ema_slow_t) < 1e-12 or pd.isna(ema_fast_t) or pd.isna(ema_slow_t):
            continue

        if ema_fast_t > ema_slow_t:
            if close_t1 <= ema_fast_t1 + 1e-12 and close_t > ema_fast_t:
                if stricter_trend and not (close_t > ema_slow_t):
                    continue
                df.at[i, 'signal'] = 1
                df.at[i, 'entry_price'] = close_t
        elif ema_fast_t < ema_slow_t:
            if close_t1 >= ema_fast_t1 - 1e-12 and close_t < ema_fast_t:
                if stricter_trend and not (close_t < ema_slow_t):
                    continue
                df.at[i, 'signal'] = -1
                df.at[i, 'entry_price'] = close_t

    return df
