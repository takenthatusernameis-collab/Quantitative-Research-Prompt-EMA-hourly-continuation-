"""Additional backtest rule tests."""
import pandas as pd
import numpy as np
from backtest.backtest import backtest_symbol


def test_sl_tp_1to1():
    """Test SL/TP uses 1:1 RR with risk = |entry - EMA100|."""
    dates = pd.date_range('2024-01-01', periods=150, freq='h')
    price = [100 + i * 0.1 for i in range(150)]
    df = pd.DataFrame({
        'timestamp': dates,
        'open': price,
        'high': [p + 5 for p in price],  # wide range
        'low': [p - 5 for p in price],
        'volume': 1000,
        'close': price
    })
    from signals.signals import generate_signals
    df_sig = generate_signals(df)
    trades, equity = backtest_symbol(df_sig, taker_fee_bps=0, slippage_bps=0)
    for t in trades:
        risk = t.risk
        if risk > 0:
            # Check 1:1 - TP distance from entry should equal risk
            assert abs((t.tp - t.entry_price) - risk) < 1e-6 or abs((t.entry_price - t.tp) - risk) < 1e-6
