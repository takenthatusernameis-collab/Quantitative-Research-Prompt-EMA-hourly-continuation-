"""Walk-forward / out-of-sample chronological split utilities."""
from typing import List, Tuple
import pandas as pd


def oos_split(df: pd.DataFrame, test_fraction: float = 0.2) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Chronological train / out-of-sample split.

    Returns (train, test) where train is the leading (1 - test_fraction) of bars
    and test is the trailing test_fraction. No shuffling; order preserved.
    """
    if not 0.0 < test_fraction < 1.0:
        raise ValueError("test_fraction must be between 0 and 1 (exclusive)")
    n = len(df)
    if n < 2:
        raise ValueError("DataFrame must contain at least 2 rows to split")
    cut = int(n * (1.0 - test_fraction))
    if cut < 1:
        cut = 1
    train = df.iloc[:cut].copy()
    test = df.iloc[cut:].copy()
    return train, test


def walk_forward_splits(
    df: pd.DataFrame,
    n_splits: int = 5,
    test_fraction: float = 0.1,
    min_train_bars: int = 100,
) -> List[Tuple[pd.DataFrame, pd.DataFrame]]:
    """Generate expanding-window walk-forward splits.

    Each split trains on data up to a cut point and tests on the immediately
    following block of bars. Windows expand forward in time (no leakage).

    Returns a list of (train, test) DataFrame tuples.
    """
    if n_splits < 1:
        raise ValueError("n_splits must be >= 1")
    if not 0.0 < test_fraction < 1.0:
        raise ValueError("test_fraction must be between 0 and 1 (exclusive)")
    n = len(df)
    if n < 2:
        raise ValueError("DataFrame must contain at least 2 rows")

    splits: List[Tuple[pd.DataFrame, pd.DataFrame]] = []
    test_size = max(1, int(n * test_fraction))
    # Start cut so the first train window is at least min_train_bars
    start_cut = min_train_bars
    if start_cut >= n - test_size:
        start_cut = max(1, n - test_size)

    cut = start_cut
    for _ in range(n_splits):
        if cut + test_size > n:
            break
        train = df.iloc[:cut].copy()
        test = df.iloc[cut:cut + test_size].copy()
        splits.append((train, test))
        cut += test_size  # expanding window: next train includes prior test

    return splits
