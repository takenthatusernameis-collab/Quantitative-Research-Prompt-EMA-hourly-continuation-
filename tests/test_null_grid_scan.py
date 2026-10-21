"""Tests for the randomized-entry null harness (scripts/null_grid_scan.py)."""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from backtest.backtest import backtest_symbol
from signals.signals import generate_signals, generate_signals_vectorized
from scripts.null_grid_scan import (apply_entries, binomial_tail, cell_seed,
                                    eligible_bars, null_entries, passes_gate,
                                    pooled_ratio, survivor_cells, window_stats)

FIXTURES = Path('data/fixtures')


def _frame(n=600, seed=7):
    """A synthetic hourly frame with a moving price."""
    rng = np.random.default_rng(seed)
    close = 100.0 + np.cumsum(rng.normal(0, 0.4, n))
    return pd.DataFrame({
        'timestamp': pd.date_range('2024-01-01', periods=n, freq='h'),
        'open': close,
        'high': close + 0.2,
        'low': close - 0.2,
        'close': close,
        'volume': 1000.0,
    })


def test_vectorized_signals_match_the_reference_generator():
    """The fast generator must be an exact twin, not an approximation."""
    df = _frame()
    for fast, slow in ((8, 12), (20, 26), (50, 100)):
        ref = generate_signals(df.copy(), fast, slow)
        vec = generate_signals_vectorized(df.copy(), fast, slow)
        assert np.array_equal(ref['signal'].to_numpy(), vec['signal'].to_numpy())
        assert np.array_equal(ref['entry_price'].to_numpy(),
                              vec['entry_price'].to_numpy(), equal_nan=True)


def test_vectorized_signals_match_the_reference_on_a_real_fixture():
    """The equivalence also holds on real market data, not just on a toy frame."""
    path = FIXTURES / 'ADA_USDT.csv'
    if not path.exists():
        pytest.skip('fixture not available')
    from data.data_loader import load_ohlcv_csv
    df = load_ohlcv_csv(path).iloc[:4000].reset_index(drop=True)
    for fast, slow in ((8, 12), (50, 100)):
        ref = generate_signals(df.copy(), fast, slow)
        vec = generate_signals_vectorized(df.copy(), fast, slow)
        assert np.array_equal(ref['signal'].to_numpy(), vec['signal'].to_numpy())


def test_eligible_bars_start_at_the_warm_up_bar():
    """A null entry can never be placed before the EMAs are defined."""
    assert eligible_bars(100, 8, 12)[0] == 12
    assert eligible_bars(300, 50, 100)[0] == 100
    assert len(eligible_bars(100, 8, 12)) == 88
    # A series shorter than the warm-up leaves no eligible bar at all.
    assert len(eligible_bars(100, 50, 100)) == 0


def test_timing_null_keeps_the_entry_count_and_moves_the_entries():
    """The timing null keeps the number of entries and the direction mix."""
    entry_idx = np.array([5, 20, 33, 47])
    sides = np.array([1.0, -1.0, 1.0, 1.0])
    eligible = eligible_bars(100, 8, 12)
    rng = np.random.default_rng(0)
    positions, directions = null_entries(entry_idx, sides, eligible, rng, 'timing')
    assert positions.size == entry_idx.size
    assert sorted(directions.tolist()) == sorted(sides.tolist())
    # The null entries are drawn from the eligible bars, never before warm-up.
    assert positions.min() >= 12
    assert set(positions.tolist()).issubset(set(eligible.tolist()))
    # And they are not the original entries.
    assert not np.array_equal(np.sort(positions), entry_idx)


def test_timing_null_is_reproducible_from_its_seed():
    """The same cell and mode always produce the same null."""
    entry_idx = np.array([5, 20, 33])
    sides = np.array([1.0, -1.0, 1.0])
    eligible = eligible_bars(100, 8, 12)
    first = null_entries(entry_idx, sides, eligible,
                         np.random.default_rng(cell_seed('ADA/USDT', 8, 12, 'timing', 0)),
                         'timing')
    second = null_entries(entry_idx, sides, eligible,
                          np.random.default_rng(cell_seed('ADA/USDT', 8, 12, 'timing', 0)),
                          'timing')
    assert np.array_equal(first[0], second[0])
    assert np.array_equal(first[1], second[1])
    # A different cell or replicate gets a different draw.
    other = null_entries(entry_idx, sides, eligible,
                         np.random.default_rng(cell_seed('ADA/USDT', 8, 12, 'timing', 1)),
                         'timing')
    assert not np.array_equal(first[0], other[0])


def test_block_null_keeps_the_entry_count_and_stays_inside_the_block():
    """The local null moves the entries inside their own block."""
    entry_idx = np.array([250, 260, 700, 705, 710])
    sides = np.array([1.0, -1.0, 1.0, 1.0, -1.0])
    eligible = eligible_bars(1000, 8, 12)
    rng = np.random.default_rng(3)
    positions, directions = null_entries(entry_idx, sides, eligible, rng, 'block',
                                         block_bars=240)
    assert positions.size == entry_idx.size
    assert sorted(directions.tolist()) == sorted(sides.tolist())
    # Every entry stays inside the block it came from.
    for original, moved in zip(entry_idx, np.sort(positions)):
        assert original // 240 == moved // 240
    # And the entries are no longer the original bars.
    assert not np.array_equal(np.sort(positions), entry_idx)


def test_block_null_is_reproducible_from_its_seed():
    """The block null is deterministic for a given cell and replicate."""
    entry_idx = np.array([250, 260, 700])
    sides = np.array([1.0, -1.0, 1.0])
    eligible = eligible_bars(1000, 8, 12)
    first = null_entries(entry_idx, sides, eligible,
                         np.random.default_rng(cell_seed('A/USDT', 8, 12, 'block', 0)),
                         'block')
    second = null_entries(entry_idx, sides, eligible,
                          np.random.default_rng(cell_seed('A/USDT', 8, 12, 'block', 0)),
                          'block')
    assert np.array_equal(first[0], second[0])
    assert np.array_equal(first[1], second[1])


def test_sign_null_keeps_the_entry_bars_and_flips_the_directions():
    """The sign null keeps the timing and randomizes the direction."""
    entry_idx = np.array([5, 20, 33, 47])
    sides = np.array([1.0, -1.0, 1.0, 1.0])
    eligible = eligible_bars(100, 8, 12)
    rng = np.random.default_rng(1)
    positions, directions = null_entries(entry_idx, sides, eligible, rng, 'sign')
    assert np.array_equal(positions, entry_idx)
    assert set(directions.tolist()) <= {1.0, -1.0}
    assert directions.size == sides.size


def test_apply_entries_writes_the_signal_and_the_entry_price():
    """The null frame carries the null entries into the engine."""
    df = _frame(50)
    positions = np.array([10, 20])
    directions = np.array([1.0, -1.0])
    null = apply_entries(df, positions, directions)
    assert null['signal'].sum() == 0.0
    assert null.loc[10, 'signal'] == 1.0
    assert null.loc[20, 'signal'] == -1.0
    assert null.loc[10, 'entry_price'] == df['close'].iloc[10]
    assert null['entry_price'].isna().sum() == len(df) - 2


def test_passes_gate_applies_the_out_of_sample_leg():
    """A cell needs PF, Sharpe, trade count and the cost stress."""
    good = {'trades': 40, 'net_pf': 1.2, 'sharpe': 0.3, 'stress_net_pf': 1.05}
    assert passes_gate(good, 30) is True
    assert passes_gate({**good, 'trades': 10}, 30) is False
    assert passes_gate({**good, 'net_pf': 0.9}, 30) is False
    assert passes_gate({**good, 'sharpe': -0.1}, 30) is False
    assert passes_gate({**good, 'stress_net_pf': 0.9}, 30) is False


def test_window_stats_matches_a_full_history_run_on_the_same_window():
    """Restricting the data to the window equals gating the entries there."""
    df = _frame(800)
    config = {
        'taker_fee_bps': 10.0, 'slippage_bps': 2.0, 'rr': 1.0,
        'stricter_trend': False, 'min_risk_atr': False, 'atr_threshold': 1.0,
        'conservative_exit': True, 'sizing': 'risk', 'risk_fraction': 0.01,
        'max_notional_multiple': 10.0, 'stress_multiplier': 2.0,
    }
    frame = generate_signals_vectorized(df.copy(), 8, 20)
    entry_start = 520
    windowed = window_stats(frame, entry_start, config, 'T/USDT')

    window = frame.iloc[entry_start:].reset_index(drop=True)
    trades, equity_df = backtest_symbol(
        window, symbol='T/USDT', taker_fee_bps=10.0, slippage_bps=2.0, rr=1.0,
        entry_start_index=0, conservative_exit=True, sizing='risk',
        risk_fraction=0.01, max_notional_multiple=10.0)
    assert windowed['trades'] == len(trades)
    assert windowed['net_pf'] == pytest.approx(
        float(np.sum([t.pnl_net for t in trades if t.pnl_net > 0]) /
              -np.sum([t.pnl_net for t in trades if t.pnl_net < 0])))


def test_binomial_tail_is_two_sided_and_symmetric():
    """The sign test is symmetric around an even split."""
    assert binomial_tail(0, 0) == 1.0
    assert binomial_tail(10, 10) == pytest.approx(binomial_tail(0, 10))
    # An even split is exactly what a fair coin produces.
    assert binomial_tail(50, 100) == pytest.approx(1.0)
    # A lopsided split is not.
    assert binomial_tail(90, 100) < 0.05
    assert binomial_tail(10, 100) < 0.05


def test_binomial_tail_survives_trials_where_the_direct_sum_overflows():
    """math.comb(9900, i) overflows, so the log-space path must still run.

    The grid-wide leg scores 9900 cells, and the direct implementation of
    this p-value raised OverflowError on it. The values below are the exact
    two-sided binomial tail computed in 60-digit Decimal arithmetic.
    """
    # Median of a fair coin over 9900 trials: indistinguishable from 1.
    assert binomial_tail(4950, 9900) == 1.0
    # A small deviation from the median is still not significant (exact 0.8486).
    assert binomial_tail(4960, 9900) == pytest.approx(0.8485603509, rel=1e-6)
    # A strong minority: astronomically small. It is not exactly zero, but it
    # underflows to 0 in float, which is what the grid leg consumes.
    assert binomial_tail(1759, 9900) == 0.0
    # Zero successes: 2 * 0.5**9900 underflows to 0.
    assert binomial_tail(0, 9900) == 0.0
    assert binomial_tail(9900, 9900) == 0.0


def test_pooled_ratio_uses_trade_pnl_not_a_mean_of_ratios():
    """A thin cell must not get the same weight as a thick one."""
    rows = [
        {'real': {'net_pf': 2.0, 'net_pnl': 100.0}},
        {'real': {'net_pf': 0.5, 'net_pnl': -100.0}},
        {'real': {'net_pf': 1.0, 'net_pnl': 0.0}},
    ]
    assert pooled_ratio(rows, 'real') == pytest.approx(1.0)


def test_survivor_cells_reads_the_audit_artifact(tmp_path):
    """The survivor list comes from the out-of-sample audit, not from a guess."""
    rows = [
        {'symbol': 'A/USDT', 'P_fast': 8, 'P_slow': 20, 'oos_trades': 40, 'oos_net_pf': 1.3},
        {'symbol': 'B/USDT', 'P_fast': 8, 'P_slow': 20, 'oos_trades': 40, 'oos_net_pf': 0.8},
        {'symbol': 'C/USDT', 'P_fast': 8, 'P_slow': 20, 'oos_trades': 5, 'oos_net_pf': 1.9},
    ]
    path = tmp_path / 'cells.jsonl'
    with open(path, 'w') as fh:
        for row in rows:
            fh.write(json.dumps(row) + '\n')
    assert survivor_cells(tmp_path, min_trades=30, min_pf=1.0) == [('A/USDT', 8, 20)]
