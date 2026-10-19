"""Signal generation for EMA hourly continuation strategy."""
from typing import Optional, List, Dict
import pandas as pd
import numpy as np


def generate_signals(df: pd.DataFrame, ema50_period: int = 50, ema100_period: int = 100) -> pd.DataFrame:
    """
    Generate long/short signals based on EMA cross strategy.

    Rules (confirmed closed-bar only):
    - Long: bullish regime (EMA50 > EMA100) and close[t-1] <= EMA50[t-1] and close[t] > EMA50[t]
    - Short: bearish regime (EMA50 < EMA100) and close[t-1] >= EMA50[t-1] and close[t] < EMA50[t]
    - No signals if EMAs equal or warm-up insufficient (< 100 bars)
    """
    df = df.copy()

    # Calculate EMAs
    df['ema50'] = df['close'].ewm(span=ema50_period, adjust=False).mean()
    df['ema100'] = df['close'].ewm(span=ema100_period, adjust=False).mean()

    df['signal'] = 0  # 0 = no signal, 1 = long, -1 = short
    df['entry_price'] = np.nan

    # Need at least 100 bars for warm-up
    for i in range(ema100_period, len(df)):
        ema50_t = df['ema50'].iloc[i]
        ema100_t = df['ema100'].iloc[i]
        close_t = df['close'].iloc[i]
        close_t1 = df['close'].iloc[i - 1]
        ema50_t1 = df['ema50'].iloc[i - 1]
        ema100_t1 = df['ema100'].iloc[i - 1]

        # Check warm-up - EMAs must be fully defined
        # After ema100_period bars, EMAs are defined

        # No entry if EMAs are equal (or effectively equal)
        if abs(ema50_t - ema100_t) < 1e-12 or pd.isna(ema50_t) or pd.isna(ema100_t):
            continue

        # Long entry: bullish regime EMA50 > EMA100 and cross above
        if ema50_t > ema100_t:
            # Price cross above EMA50: close[t-1] <= EMA50[t-1] and close[t] > EMA50[t]
            if close_t1 <= ema50_t1 + 1e-12 and close_t > ema50_t:  # allow for small numerical
                df.at[i, 'signal'] = 1
                df.at[i, 'entry_price'] = close_t

        # Short entry: bearish regime EMA50 < EMA100 and cross below
        elif ema50_t < ema100_t:
            # Price cross below EMA50: close[t-1] >= EMA50[t-1] and close[t] < EMA50[t]
            if close_t1 >= ema50_t1 - 1e-12 and close_t < ema50_t:
                df.at[i, 'signal'] = -1
                df.at[i, 'entry_price'] = close_t

    return df
