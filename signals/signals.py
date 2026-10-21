"""Signal generation for EMA hourly continuation strategy."""
from typing import Optional, List, Dict
import pandas as pd
import numpy as np

# Cross tolerance of the reference implementation: the previous bar's close may
# sit within this distance of the fast EMA and still count as a cross.
CROSS_TOLERANCE = 1e-12

# A flat stack (|EMAfast - EMAslow| below this) is treated as "no regime".
REGIME_TOLERANCE = 1e-12


def generate_signals_vectorized(df: pd.DataFrame, ema_fast_period: int = 50,
                                ema_slow_period: int = 100,
                                stricter_trend: bool = False) -> pd.DataFrame:
    """Vectorized twin of `generate_signals`.

    The reference implementation walks the bar-by-bar Python loop, which costs
    ~0.9 s per cell on a 22 000-bar series - too slow to run the grid's
    randomization null over all 17 556 cells. This function computes exactly
    the same signals with array operations.

    Equivalence is not approximate: the EMA definition, the warm-up boundary,
    the regime test, the cross test and the tolerances are all identical to
    the reference, and `tests/test_signals.py` asserts that both
    implementations return the same signal and entry-price series on real
    fixtures. The reference function stays the research path; this one is used
    by the null harness only.
    """
    df = df.copy()
    df['ema_fast'] = df['close'].ewm(span=ema_fast_period, adjust=False).mean()
    df['ema_slow'] = df['close'].ewm(span=ema_slow_period, adjust=False).mean()

    close = df['close'].to_numpy(dtype=float)
    ema_fast = df['ema_fast'].to_numpy(dtype=float)
    ema_slow = df['ema_slow'].to_numpy(dtype=float)

    close_prev = np.empty_like(close)
    ema_fast_prev = np.empty_like(ema_fast)
    close_prev[0] = np.nan
    ema_fast_prev[0] = np.nan
    close_prev[1:] = close[:-1]
    ema_fast_prev[1:] = ema_fast[:-1]

    with np.errstate(invalid='ignore'):
        defined = ~(np.isnan(ema_fast) | np.isnan(ema_slow))
        # The reference skips a bar when the stack is flat or undefined.
        stacked = defined & (np.abs(ema_fast - ema_slow) >= REGIME_TOLERANCE)
        regime_up = stacked & (ema_fast > ema_slow)
        regime_down = stacked & (ema_fast < ema_slow)

        cross_up = ((close_prev <= ema_fast_prev + CROSS_TOLERANCE)
                    & (close > ema_fast))
        cross_down = ((close_prev >= ema_fast_prev - CROSS_TOLERANCE)
                      & (close < ema_fast))

        if stricter_trend:
            regime_up = regime_up & (close > ema_slow)
            regime_down = regime_down & (close < ema_slow)

    signal = np.zeros(len(df), dtype=float)
    signal[regime_up & cross_up] = 1.0
    signal[regime_down & cross_down] = -1.0
    # The reference loop starts at the warm-up bar, so nothing fires before it.
    warmup = max(ema_fast_period, ema_slow_period)
    signal[:warmup] = 0.0

    df['signal'] = signal
    df['entry_price'] = np.where(signal != 0, close, np.nan)
    return df


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
