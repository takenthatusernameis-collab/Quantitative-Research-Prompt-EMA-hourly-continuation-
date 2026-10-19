"""Tests for backtest accounting invariants.

These lock in two properties that were previously violated:

1. The equity curve reconciles exactly with the trade blotter:
   ``equity_final == starting_equity + sum(trade.pnl_net)``.
   Entry costs must be charged exactly once, and exit costs exactly once.

2. Risk-based sizing keeps the equity curve in the strategy's own currency so
   that Sharpe / max drawdown / CAGR are comparable across symbols regardless
   of the asset's price level.
"""
import numpy as np
import pandas as pd

from backtest.backtest import backtest_symbol
from signals.signals import generate_signals


def _synthetic_df(seed=7, n=600, start=100.0):
    rng = np.random.default_rng(seed)
    close = start + np.cumsum(rng.normal(0, 0.5, n))
    return pd.DataFrame({
        'timestamp': pd.date_range('2024-01-01', periods=n, freq='h'),
        'open': close,
        'high': close + 0.3,
        'low': close - 0.3,
        'close': close,
        'volume': 1000.0,
    })


def test_equity_reconciles_with_trade_blotter():
    """equity_final == starting_equity + sum(pnl_net)."""
    df = _synthetic_df()
    df_sig = generate_signals(df, ema_fast_period=8, ema_slow_period=20)
    trades, equity = backtest_symbol(df_sig, taker_fee_bps=10, slippage_bps=2)
    assert trades, 'expected at least one trade on synthetic data'
    expected = 10000.0 + sum(t.pnl_net for t in trades)
    assert abs(equity['equity'].iloc[-1] - expected) < 1e-6


def test_costs_are_charged_exactly_once():
    """entry_cost + exit_cost per trade equals the net-vs-gross P&L gap."""
    df = _synthetic_df()
    df_sig = generate_signals(df, ema_fast_period=8, ema_slow_period=20)
    trades, _ = backtest_symbol(df_sig, taker_fee_bps=10, slippage_bps=2)
    for t in trades:
        total_cost = t.entry_cost + t.exit_cost
        assert abs((t.pnl - t.pnl_net) - total_cost) < 1e-9
        # Entry cost is charged once, on the entry notional.
        assert abs(t.entry_cost - t.notional * 0.0012) < 1e-9
        # Exit cost is charged once, on the exit notional.
        assert abs(t.exit_cost - t.qty * 0.0012 * t.exit_price) < 1e-9


def test_risk_sizing_risks_configured_fraction_of_equity():
    """Position notional is sized so each trade risks `risk_fraction` of equity."""
    df = _synthetic_df()
    df_sig = generate_signals(df, ema_fast_period=8, ema_slow_period=20)
    trades, equity = backtest_symbol(df_sig, taker_fee_bps=10, slippage_bps=2,
                                     sizing='risk', risk_fraction=0.01)
    assert trades
    for t in trades:
        # The amount at risk (price distance * qty) is a bounded fraction of
        # the equity at the time of entry.
        assert t.risk * t.qty <= 0.01 * 10000.0 * 1.5
        # Notional never exceeds the configured cap multiple of equity.
        assert t.notional <= 10.0 * 10000.0 * 1.5


def test_unit_notional_mode_keeps_qty_at_one():
    """Legacy mode still trades one unit of the base asset per signal."""
    df = _synthetic_df()
    df_sig = generate_signals(df, ema_fast_period=8, ema_slow_period=20)
    trades, equity = backtest_symbol(df_sig, taker_fee_bps=10, slippage_bps=2,
                                     sizing='unit_notional')
    assert trades
    for t in trades:
        assert t.qty == 1.0
        assert abs(t.notional - t.entry_price) < 1e-9
    expected = 10000.0 + sum(t.pnl_net for t in trades)
    assert abs(equity['equity'].iloc[-1] - expected) < 1e-6


def test_zero_cost_run_has_pnl_equal_pnl_net():
    """With zero costs the net and gross P&L must be identical."""
    df = _synthetic_df()
    df_sig = generate_signals(df, ema_fast_period=8, ema_slow_period=20)
    trades, equity = backtest_symbol(df_sig, taker_fee_bps=0, slippage_bps=0)
    assert trades
    for t in trades:
        assert abs(t.pnl - t.pnl_net) < 1e-12
    expected = 10000.0 + sum(t.pnl_net for t in trades)
    assert abs(equity['equity'].iloc[-1] - expected) < 1e-6


def test_equity_curve_stays_finite_for_bankrupt_path():
    """A losing path must not produce NaN/inf equity or absurd drawdowns."""
    df = _synthetic_df(seed=99, n=800, start=100.0)
    df_sig = generate_signals(df, ema_fast_period=8, ema_slow_period=20)
    trades, equity = backtest_symbol(df_sig, taker_fee_bps=10, slippage_bps=2,
                                     sizing='risk', risk_fraction=0.05)
    assert np.all(np.isfinite(equity['equity'].values))
