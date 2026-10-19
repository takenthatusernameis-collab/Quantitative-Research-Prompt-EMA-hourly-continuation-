"""Tests for walk-forward / OOS split utilities."""
import pandas as pd
from backtest.walkforward import oos_split, walk_forward_splits


def _make_df(n=200):
    dates = pd.date_range('2024-01-01', periods=n, freq='h')
    return pd.DataFrame({
        'timestamp': dates,
        'close': [100.0 + i * 0.01 for i in range(n)],
    })


def test_oos_split_preserves_order_and_covers_all():
    df = _make_df(200)
    train, test = oos_split(df, test_fraction=0.2)
    assert len(train) + len(test) == 200
    assert len(train) == 160
    assert len(test) == 40
    # Chronological: all train timestamps before all test timestamps
    assert train['timestamp'].iloc[-1] <= test['timestamp'].iloc[0]


def test_oos_split_invalid_fraction():
    df = _make_df(100)
    for bad in (0.0, 1.0, -0.1, 1.5):
        try:
            oos_split(df, test_fraction=bad)
        except ValueError:
            continue
        else:
            raise AssertionError(f"expected ValueError for test_fraction={bad}")


def test_walk_forward_splits():
    df = _make_df(200)
    splits = walk_forward_splits(df, n_splits=4, test_fraction=0.1, min_train_bars=100)
    assert len(splits) == 4
    for train, test in splits:
        assert len(train) > 0
        assert len(test) > 0
        assert train['timestamp'].iloc[-1] <= test['timestamp'].iloc[0]
    # Expanding: each train window should grow
    lens = [len(t) for t, _ in splits]
    assert all(lens[i] <= lens[i + 1] for i in range(len(lens) - 1))


def test_walk_forward_no_leakage():
    """Test set never overlaps train set within a split."""
    df = _make_df(200)
    splits = walk_forward_splits(df, n_splits=3, test_fraction=0.1, min_train_bars=100)
    for train, test in splits:
        train_ts = set(train['timestamp'])
        test_ts = set(test['timestamp'])
        assert train_ts.isdisjoint(test_ts)
