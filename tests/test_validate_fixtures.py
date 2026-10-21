"""Tests for the fixture validator (scripts/validate_fixtures.py)."""
import pandas as pd
import pytest

from scripts.validate_fixtures import loader_rows, validate


def _write(tmp_path, name, rows, timestamps=None):
    path = tmp_path / name
    data = {
        'timestamp': timestamps or [f'2024-01-01 {h:02d}:00:00+00:00' for h in range(len(rows))],
        'open': [r[0] for r in rows],
        'high': [r[1] for r in rows],
        'low': [r[2] for r in rows],
        'close': [r[3] for r in rows],
        'volume': [1.0] * len(rows),
    }
    pd.DataFrame(data).to_csv(path, index=False)
    return path


def test_validate_accepts_a_clean_hourly_series(tmp_path):
    """A contiguous, well-formed series passes every check."""
    rows = [(1.0, 1.2, 0.9, 1.1)] * 24
    path = _write(tmp_path, 'AAA_USDT.csv', rows)
    out = validate(path)
    assert out['valid'] is True
    assert out['gap_count'] == 0
    assert out['max_gap_hours'] == 0.0
    assert out['dup_timestamps'] == 0
    assert out['nan_rows'] == 0
    assert out['invalid_ohlc_rows'] == 0
    assert out['cost_to_move_multiple'] is None  # a flat series has no move


def test_validate_flags_a_gap_in_the_hourly_grid(tmp_path):
    """A missing hour is a gap, not a valid series."""
    timestamps = [f'2024-01-01 {h:02d}:00:00+00:00' for h in range(24) if h != 10]
    rows = [(1.0, 1.2, 0.9, 1.1)] * len(timestamps)
    path = _write(tmp_path, 'BBB_USDT.csv', rows, timestamps)
    out = validate(path)
    assert out['valid'] is False
    assert out['gap_count'] == 1
    assert out['max_gap_hours'] == 2.0


def test_validate_flags_duplicate_timestamps(tmp_path):
    """A repeated hour is a duplicate."""
    rows = [(1.0, 1.2, 0.9, 1.1)] * 24
    timestamps = [f'2024-01-01 {h:02d}:00:00+00:00' for h in range(24)]
    timestamps[5] = timestamps[4]
    path = _write(tmp_path, 'CCC_USDT.csv', rows, timestamps)
    out = validate(path)
    assert out['valid'] is False
    assert out['dup_timestamps'] == 1


def test_loader_rows_counts_what_the_data_loader_drops(tmp_path):
    """The grid runs on the loaded series, so dropped rows must be counted."""
    rows = [(1.0, 1.2, 0.9, 1.1)] * 24
    timestamps = [f'2024-01-01 {h:02d}:00:00+00:00' for h in range(24)]
    timestamps[5] = timestamps[4]
    path = _write(tmp_path, 'DDD_USDT.csv', rows, timestamps)
    out = loader_rows(path)
    assert out['raw_rows'] == 24
    assert out['loaded_rows'] == 23
    assert out['dropped_rows'] == 1
