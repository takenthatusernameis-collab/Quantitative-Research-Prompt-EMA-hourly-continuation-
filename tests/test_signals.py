"""Tests for signal generation."""
import pandas as pd
import numpy as np
from signals.signals import generate_signals


def create_test_data(n=150):
    """Create synthetic test data."""
    # Create simple uptrend then cross
    dates = pd.date_range('2024-01-01', periods=n, freq='h')
    # Build price series
    price = []
    np.random.seed(42)
    for i in range(n):
        # gradual uptrend with small noise
        base = 100 + i * 0.1
        noise = np.random.randn() * 0.5
        price.append(max(1, base + noise))
    df = pd.DataFrame({
        'timestamp': dates,
        'open': price,
        'high': [p * 1.01 for p in price],
        'low': [p * 0.99 for p in price],
        'close': price,
        'volume': 1000
    })
    return df


def test_generate_signals_basic():
    """Test signal generation runs."""
    df = create_test_data(120)
    result = generate_signals(df)
    assert 'signal' in result.columns
    assert 'ema50' in result.columns
    assert 'ema100' in result.columns
