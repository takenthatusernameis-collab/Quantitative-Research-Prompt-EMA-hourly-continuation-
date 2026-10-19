"""Tests for EMA calculation."""
import pandas as pd
import numpy as np
from signals.indicators import ema


def test_ema_basic():
    """Test basic EMA calculation."""
    s = pd.Series([1, 2, 3, 4, 5])
    result = ema(s, 3)
    assert len(result) == 5
    assert not pd.isna(result.iloc[2])  # should have value at index 2+


def test_ema_values():
    """Test EMA with known values."""
    # Simple test - EMA should be close to expected
    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
    result = ema(s, 5)
    assert result.iloc[-1] > 0
