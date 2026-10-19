"""Detailed tests for signal generation per spec."""
import pandas as pd
import numpy as np
from signals.signals import generate_signals


def test_no_signals_when_emas_equal():
    """No entries when EMAs equal."""
    # Create flat price so EMAs converge
    n = 120
    dates = pd.date_range('2024-01-01', periods=n, freq='h')
    price = [100.0] * n
    df = pd.DataFrame({
        'timestamp': dates,
        'open': price,
        'high': price,
        'low': price,
        'close': price,
        'volume': 1000
    })
    result = generate_signals(df)
    # After warmup, if equal, no signals
    signals = result['signal'].iloc[100:].tolist()
    assert all(s == 0 for s in signals)


def test_warmup_enforced():
    """No signals until warmup (>=100 bars)."""
    n = 90
    dates = pd.date_range('2024-01-01', periods=n, freq='h')
    # Create a clear cross
    price = list(range(90))  # increasing
    df = pd.DataFrame({
        'timestamp': dates,
        'open': price,
        'high': price,
        'low': price,
        'close': price,
        'volume': 1000
    })
    result = generate_signals(df)
    # No signals before index 100 (but we only have up to 89)
    assert result['signal'].sum() == 0
