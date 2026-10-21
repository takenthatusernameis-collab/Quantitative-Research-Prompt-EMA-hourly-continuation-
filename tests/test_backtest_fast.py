"""Equivalence tests for the array-based backtest engine.

`backtest_symbol_fast` is only allowed to exist if it is a drop-in twin of
`backtest_symbol`: same trades, same equity curve, same metrics. These tests
assert that on synthetic frames (where the interesting paths - same-bar
conflicts, the ATR filter, the notional cap, the end-of-sample close - can be
triggered on purpose) and on real fixtures.
"""
import math
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from backtest.backtest import backtest_symbol, backtest_symbol_fast

FIXTURE_DIR = Path('data/fixtures')

TRADE_FIELDS = ('symbol', 'side', 'entry_price', 'exit_price', 'sl', 'tp',
                'risk', 'pnl', 'pnl_net', 'exit_reason', 'bar_index',
                'exit_bar_index', 'qty', 'notional', 'entry_cost', 'exit_cost',
                'risk_pct')


def _frame(prices, signals, ema_slow=None, highs=None, lows=None):
    """Build a frame the engine can consume directly."""
    n = len(prices)
    closes = list(prices)
    highs = list(highs) if highs is not None else [p + 0.5 for p in closes]
    lows = list(lows) if lows is not None else [p - 0.5 for p in closes]
    if ema_slow is None:
        ema_slow = [p - 1.0 for p in closes]
    return pd.DataFrame({
        'timestamp': pd.date_range('2024-01-01', periods=n, freq='h'),
        'open': closes,
        'high': highs,
        'low': lows,
        'close': closes,
        'volume': [1000.0] * n,
        'signal': signals,
        'entry_price': [c if s != 0 else np.nan for c, s in zip(closes, signals)],
        'ema_slow': ema_slow,
    })


def _assert_same(result_ref, result_fast):
    trades_ref, equity_ref = result_ref
    trades_fast, equity_fast = result_fast
    assert len(trades_ref) == len(trades_fast)
    for a, b in zip(trades_ref, trades_fast):
        for field in TRADE_FIELDS:
            left, right = getattr(a, field), getattr(b, field)
            if isinstance(left, float) and isinstance(right, float):
                assert left == pytest.approx(right, rel=1e-12, abs=1e-12), field
            else:
                assert left == right, field
        assert a.entry_time == b.entry_time
        assert a.exit_time == b.exit_time
    assert list(equity_ref.columns) == list(equity_fast.columns)
    assert len(equity_ref) == len(equity_fast)
    for column in ('equity', 'position', 'index'):
        left = equity_ref[column].to_numpy()
        right = equity_fast[column].to_numpy()
        assert np.array_equal(left, right), column
    assert equity_ref['timestamp'].tolist() == equity_fast['timestamp'].tolist()


def test_long_trade_take_profit():
    df = _frame([100.0] * 6, [0, 1, 0, 0, 0, 0],
                highs=[100.5, 100.5, 100.5, 102.5, 102.5, 102.5],
                lows=[99.5, 99.5, 99.5, 99.5, 99.5, 99.5])
    _assert_same(backtest_symbol(df, symbol='X'), backtest_symbol_fast(df, symbol='X'))


def test_short_trade_stop_loss():
    df = _frame([100.0] * 6, [0, -1, 0, 0, 0, 0],
                highs=[100.5, 100.5, 100.5, 102.5, 102.5, 102.5],
                lows=[99.5, 99.5, 99.5, 99.5, 99.5, 99.5])
    _assert_same(backtest_symbol(df, symbol='X'), backtest_symbol_fast(df, symbol='X'))


def test_same_bar_conflict_is_adverse_first():
    # The bar after the entry touches both SL and TP: the conservative rule
    # exits at the stop.
    df = _frame([100.0] * 5, [0, 1, 0, 0, 0],
                highs=[100.5, 100.5, 102.5, 100.5, 100.5],
                lows=[99.5, 99.5, 98.5, 99.5, 99.5])
    ref = backtest_symbol(df, symbol='X', conservative_exit=True)
    fast = backtest_symbol_fast(df, symbol='X', conservative_exit=True)
    _assert_same(ref, fast)
    assert ref[0][0].exit_reason == 'sl'

    ref_aggressive = backtest_symbol(df, symbol='X', conservative_exit=False)
    fast_aggressive = backtest_symbol_fast(df, symbol='X', conservative_exit=False)
    _assert_same(ref_aggressive, fast_aggressive)
    assert ref_aggressive[0][0].exit_reason == 'tp'


def test_end_of_sample_close():
    df = _frame([100.0] * 8, [0, 1, 0, 0, 0, 0, 0, 0])
    _assert_same(backtest_symbol(df, symbol='X'), backtest_symbol_fast(df, symbol='X'))
    assert backtest_symbol(df)[0][-1].exit_reason == 'end'


def test_no_reentry_on_the_exit_bar():
    # A fresh signal on the bar the position exits must not open a new one.
    df = _frame([100.0] * 6, [0, 1, 1, 0, 0, 0],
                highs=[100.5, 100.5, 102.5, 100.5, 100.5, 100.5],
                lows=[99.5, 99.5, 99.5, 99.5, 99.5, 99.5])
    _assert_same(backtest_symbol(df, symbol='X'), backtest_symbol_fast(df, symbol='X'))


def test_atr_min_risk_filter():
    # The ATR filter drops the trade when the stop is narrower than the ATR.
    df = _frame([100.0] * 40, [0] + [1] * 39,
                ema_slow=[99.9] * 40)
    df.loc[1, 'signal'] = 1
    df.loc[1, 'entry_price'] = 100.0
    _assert_same(backtest_symbol(df, symbol='X', min_risk_atr=True),
                 backtest_symbol_fast(df, symbol='X', min_risk_atr=True))
    assert backtest_symbol(df, min_risk_atr=True)[0] == []
    # Without the filter the same frame trades.
    assert backtest_symbol(df)[0] != []


def test_atr_filter_keeps_wide_stops():
    n = 40
    prices = [100.0] * n
    ema_slow = [100.0 - 5.0] * n  # a 5 % stop, far above the flat-bar ATR
    df = _frame(prices, [0] * n, ema_slow=ema_slow)
    # The signal has to fire after the ATR is defined (bar 13).
    df.loc[20, 'signal'] = 1
    df.loc[20, 'entry_price'] = 100.0
    _assert_same(backtest_symbol(df, symbol='X', min_risk_atr=True),
                 backtest_symbol_fast(df, symbol='X', min_risk_atr=True))
    assert backtest_symbol(df, min_risk_atr=True)[0] != []


def test_unit_notional_sizing():
    df = _frame([100.0] * 6, [0, 1, 0, 0, 0, 0],
                highs=[100.5, 100.5, 100.5, 102.5, 102.5, 102.5])
    _assert_same(backtest_symbol(df, symbol='X', sizing='unit_notional'),
                 backtest_symbol_fast(df, symbol='X', sizing='unit_notional'))


def test_notional_cap_binds():
    # A very tight stop would lever the position far past the notional cap.
    df = _frame([100.0] * 6, [0, 1, 0, 0, 0, 0],
                ema_slow=[99.999] * 6,
                highs=[100.5, 100.5, 100.5, 102.5, 102.5, 102.5])
    _assert_same(backtest_symbol(df, symbol='X', max_notional_multiple=10.0),
                 backtest_symbol_fast(df, symbol='X', max_notional_multiple=10.0))
    trade = backtest_symbol_fast(df, max_notional_multiple=10.0)[0][0]
    assert trade.notional <= 10.0 * 10000.0 + 1e-6


def test_entry_start_index_restricts_entries():
    df = _frame([100.0] * 10, [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                highs=[100.5, 100.5, 102.5, 100.5, 100.5, 102.5, 100.5, 100.5, 100.5, 100.5],
                lows=[99.5] * 10)
    _assert_same(backtest_symbol(df, symbol='X', entry_start_index=5),
                 backtest_symbol_fast(df, symbol='X', entry_start_index=5))


def test_empty_frame():
    df = _frame([], [])
    ref = backtest_symbol(df)
    fast = backtest_symbol_fast(df)
    assert ref[0] == fast[0] == []
    assert len(ref[1]) == len(fast[1]) == 0


@pytest.mark.parametrize('atr', [False, True])
@pytest.mark.parametrize('sizing', ['risk', 'unit_notional'])
def test_real_fixture_equivalence(atr, sizing):
    """The equivalence has to hold on real hourly data, not only on synthetic
    frames."""
    path = FIXTURE_DIR / '1INCH_USDT.csv'
    if not path.exists():
        pytest.skip('fixture not available')
    from data.data_loader import load_ohlcv_csv
    from signals.signals import generate_signals

    df = load_ohlcv_csv(str(path))
    for fast_period, slow_period in ((8, 200), (50, 100)):
        signals = generate_signals(df.copy(), fast_period, slow_period)
        _assert_same(
            backtest_symbol(signals, symbol='1INCH/USDT', min_risk_atr=atr,
                            sizing=sizing),
            backtest_symbol_fast(signals, symbol='1INCH/USDT', min_risk_atr=atr,
                                 sizing=sizing),
        )
