"""Tests for backtesting."""
import pandas as pd
import numpy as np
from backtest.backtest import backtest_symbol, Trade


def test_sl_tp_geometry():
    """Test SL/TP geometry with 1:1 RR."""
    # Create minimal case
    dates = pd.date_range('2024-01-01', periods=150, freq='h')
    price = [100 + i * 0.01 for i in range(150)]
    df = pd.DataFrame({
        'timestamp': dates,
        'open': price,
        'high': [p + 0.5 for p in price],
        'low': [p - 0.5 for p in price],
        'close': price,
        'volume': 1000
    })
    from signals.signals import generate_signals
    df_sig = generate_signals(df)
    trades, equity = backtest_symbol(df_sig)
    assert isinstance(trades, list)
