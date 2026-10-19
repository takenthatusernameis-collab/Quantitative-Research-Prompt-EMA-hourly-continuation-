"""Robustness tests: same-bar conflict, pathological risk, missing/duplicate data."""
import pandas as pd
import numpy as np
import tempfile
import os

from backtest.backtest import backtest_symbol
from data.data_loader import load_ohlcv_csv


def _make_df(n=120):
    dates = pd.date_range('2024-01-01', periods=n, freq='h')
    price = [100.0] * n
    df = pd.DataFrame({
        'timestamp': dates,
        'open': price,
        'high': price,
        'low': price,
        'close': price,
        'volume': [1000] * n,
    })
    df['ema50'] = 100.0
    df['ema100'] = 100.0
    df['signal'] = 0
    df['entry_price'] = np.nan
    return df


def test_same_bar_conflict_prioritizes_sl_long():
    """Long: both TP and SL hit same bar -> SL (adverse) wins."""
    df = _make_df()
    # Long signal at index 100: entry 100, EMA100 99 -> risk 1, SL 99, TP 101
    df.at[100, 'signal'] = 1
    df.at[100, 'entry_price'] = 100.0
    df.at[100, 'ema100'] = 99.0
    # Bar 101: high >= TP(101) and low <= SL(99) -> conflict
    df.at[101, 'high'] = 101.0
    df.at[101, 'low'] = 99.0
    df.at[101, 'close'] = 100.0

    trades, _ = backtest_symbol(df, taker_fee_bps=0.0, slippage_bps=0.0)
    assert len(trades) == 1
    assert trades[0].exit_reason == 'sl'
    assert trades[0].exit_price == 99.0


def test_same_bar_conflict_prioritizes_sl_short():
    """Short: both TP and SL hit same bar -> SL (adverse) wins."""
    df = _make_df()
    # Short signal at index 100: entry 100, EMA100 101 -> risk 1, SL 101, TP 99
    df.at[100, 'signal'] = -1
    df.at[100, 'entry_price'] = 100.0
    df.at[100, 'ema100'] = 101.0
    # Bar 101: high >= SL(101) and low <= TP(99) -> conflict
    df.at[101, 'high'] = 101.0
    df.at[101, 'low'] = 99.0
    df.at[101, 'close'] = 100.0

    trades, _ = backtest_symbol(df, taker_fee_bps=0.0, slippage_bps=0.0)
    assert len(trades) == 1
    assert trades[0].exit_reason == 'sl'
    assert trades[0].exit_price == 101.0


def test_risk_zero_skips_trade():
    """entry == EMA100 -> risk 0 -> trade skipped."""
    df = _make_df()
    df.at[100, 'signal'] = 1
    df.at[100, 'entry_price'] = 100.0
    df.at[100, 'ema100'] = 100.0  # risk = 0

    trades, _ = backtest_symbol(df, taker_fee_bps=0.0, slippage_bps=0.0)
    assert len(trades) == 0


def test_pathological_risk_skips_trade():
    """entry almost on EMA100 (tiny risk) -> trade skipped."""
    df = _make_df()
    df.at[100, 'signal'] = 1
    df.at[100, 'entry_price'] = 100.0
    df.at[100, 'ema100'] = 100.0 + 1e-12  # risk below threshold

    trades, _ = backtest_symbol(df, taker_fee_bps=0.0, slippage_bps=0.0)
    assert len(trades) == 0


def test_data_loader_drops_nan_and_duplicates():
    """NaN rows dropped, duplicate timestamps deduped."""
    rows = [
        "timestamp,open,high,low,close,volume",
        "2024-01-01 00:00:00,100,101,99,100,1000",
        "2024-01-01 01:00:00,101,102,100,101,1000",
        "2024-01-01 01:00:00,101,102,100,101,1000",  # duplicate timestamp
        "2024-01-01 02:00:00,,102,100,101,1000",     # NaN open -> dropped
        "2024-01-01 03:00:00,102,103,101,102,1000",
    ]
    with tempfile.NamedTemporaryFile('w', suffix='.csv', delete=False) as f:
        f.write('\n'.join(rows))
        tmp = f.name
    try:
        df = load_ohlcv_csv(tmp)
        ts = set(df['timestamp'])
        # 00:00, 01:00 (deduped), 03:00 survive; 02:00 dropped (NaN)
        assert len(df) == 3
        assert pd.Timestamp('2024-01-01 02:00:00') not in ts
        # no duplicate timestamps
        assert df['timestamp'].duplicated().sum() == 0
    finally:
        os.unlink(tmp)
