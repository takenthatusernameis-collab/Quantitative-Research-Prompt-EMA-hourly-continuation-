"""Backtesting engine."""
from typing import Dict, List, Any, Optional
import pandas as pd
import numpy as np
from dataclasses import dataclass, asdict
import datetime


@dataclass
class Trade:
    symbol: str
    entry_time: Any
    exit_time: Any
    side: str  # 'long' or 'short'
    entry_price: float
    exit_price: float
    sl: float
    tp: float
    risk: float
    pnl: float
    pnl_net: float
    exit_reason: str  # 'tp', 'sl', 'end'
    bar_index: int
    exit_bar_index: int = -1
    qty: float = 0.0
    notional: float = 0.0
    entry_cost: float = 0.0
    exit_cost: float = 0.0
    risk_pct: float = 0.0


def backtest_symbol(df: pd.DataFrame, symbol: str = 'SYMBOL',
                   taker_fee_bps: float = 10.0, slippage_bps: float = 2.0,
                   one_position: bool = True, rr: float = 1.0,
                   min_risk_atr: bool = False, atr_threshold: float = 1.0,
                   entry_start_index: int = 0, conservative_exit: bool = True,
                   sizing: str = 'risk', risk_fraction: float = 0.01,
                   max_notional_multiple: float = 10.0,
                   starting_equity: float = 10000.0) -> tuple:
    """
    Backtest a single symbol.

    Costs: taker fee and slippage per side (default 10 bps + 2 bps per side)
    SL/TP at 1:1 RR where risk = |entry - EMA_slow[t]| on signal bar

    Sizing
    ------
    `sizing='risk'` (default) is risk-based: each trade risks `risk_fraction`
    of the equity available at entry, so the position notional is
    ``qty = equity * risk_fraction / risk_distance``. The equity curve is then
    a real compounding curve in the strategy's own currency, and Sharpe /
    max drawdown / CAGR are comparable across symbols regardless of the
    asset's price level.

    `sizing='unit_notional'` is the legacy mode: one unit of the base asset per
    trade. Trade-level gross P&L is identical in both modes; only the
    notional scaling differs.

    Entry costs are charged exactly once (at entry) and exit costs exactly
    once (at exit), so the equity curve reconciles with the trade blotter:
    ``equity_final == starting_equity + sum(trade.pnl_net)``.
    """
    df = df.copy()
    if min_risk_atr and 'atr14' not in df.columns:
        tr = pd.concat([df['high']-df['low'], (df['high']-df['close'].shift()).abs(), (df['low']-df['close'].shift()).abs()], axis=1).max(axis=1)
        df['atr14'] = tr.rolling(14).mean()
    trades: List[Trade] = []
    equity = float(starting_equity)
    equity_curve = []
    position = 0  # 0 no position, 1 long, -1 short
    entry_trade: Optional[Trade] = None
    position_entry_idx = -1

    # Cost per side (as a fraction of traded notional)
    cost_per_side = (taker_fee_bps + slippage_bps) / 10000.0

    for i in range(len(df)):
        # Record equity
        equity_curve.append({
            'index': i,
            'timestamp': df['timestamp'].iloc[i] if 'timestamp' in df.columns else i,
            'equity': equity,
            'position': position
        })

        # Check if in position - look for exit
        if position != 0 and entry_trade is not None:
            high = df['high'].iloc[i]
            low = df['low'].iloc[i]
            close = df['close'].iloc[i]
            exit_time = df['timestamp'].iloc[i] if 'timestamp' in df.columns else i

            if position == 1:  # long position
                # Check TP first, then SL? Or based on which hits first
                # For same-bar conflict, treat as adverse first - but need to define
                # Check if both hit? If high >= tp and low <= sl, it's a conflict
                # Conservative: if TP and SL both in same bar range, define - e.g. SL hit first if moving against? Or as specified
                tp_hit = high >= entry_trade.tp
                sl_hit = low <= entry_trade.sl
                if tp_hit and sl_hit:
                    # Same-bar conflict: conservative = SL first (adverse), aggressive = TP first (favorable)
                    if conservative_exit:
                        exit_price = entry_trade.sl
                        exit_reason = 'sl'
                    else:
                        exit_price = entry_trade.tp
                        exit_reason = 'tp'
                    pnl_per_unit = (exit_price - entry_trade.entry_price)
                elif tp_hit:
                    exit_price = entry_trade.tp
                    pnl_per_unit = (exit_price - entry_trade.entry_price)
                    exit_reason = 'tp'
                elif sl_hit:
                    exit_price = entry_trade.sl
                    pnl_per_unit = (exit_price - entry_trade.entry_price)
                    exit_reason = 'sl'
                else:
                    continue  # no exit yet
                # Scale the per-unit P&L to the traded notional
                pnl = pnl_per_unit * entry_trade.qty
                exit_cost = entry_trade.qty * cost_per_side * exit_price
                # pnl_net is the full round-trip net of this trade (entry + exit
                # costs). The equity curve charges the entry cost at entry and
                # the exit cost here, so the two reconcile exactly.
                pnl_net = pnl - entry_trade.entry_cost - exit_cost
                entry_trade.exit_time = exit_time
                entry_trade.exit_price = exit_price
                entry_trade.exit_bar_index = i
                entry_trade.pnl = pnl
                entry_trade.pnl_net = pnl_net
                entry_trade.exit_cost = exit_cost
                entry_trade.exit_reason = exit_reason
                trades.append(entry_trade)
                equity += pnl - exit_cost  # entry cost already taken at entry
                position = 0
                entry_trade = None
                continue

            elif position == -1:  # short position
                tp_hit = low <= entry_trade.tp  # for short, TP is below
                sl_hit = high >= entry_trade.sl  # for short, SL is above
                if tp_hit and sl_hit:
                    # Same-bar conflict: conservative = SL first (adverse), aggressive = TP first (favorable)
                    if conservative_exit:
                        exit_price = entry_trade.sl
                        exit_reason = 'sl'
                    else:
                        exit_price = entry_trade.tp
                        exit_reason = 'tp'
                    pnl_per_unit = (entry_trade.entry_price - exit_price)
                elif tp_hit:
                    exit_price = entry_trade.tp
                    pnl_per_unit = (entry_trade.entry_price - exit_price)
                    exit_reason = 'tp'
                elif sl_hit:
                    exit_price = entry_trade.sl
                    pnl_per_unit = (entry_trade.entry_price - exit_price)
                    exit_reason = 'sl'
                else:
                    continue
                pnl = pnl_per_unit * entry_trade.qty
                exit_cost = entry_trade.qty * cost_per_side * exit_price
                pnl_net = pnl - entry_trade.entry_cost - exit_cost
                entry_trade.exit_time = exit_time
                entry_trade.exit_price = exit_price
                entry_trade.exit_bar_index = i
                entry_trade.pnl = pnl
                entry_trade.pnl_net = pnl_net
                entry_trade.exit_cost = exit_cost
                entry_trade.exit_reason = exit_reason
                trades.append(entry_trade)
                equity += pnl - exit_cost
                position = 0
                entry_trade = None
                continue

        # Check for new signals if not in position (or if one_position allows new after close - but we manage)
        if position == 0 and i >= entry_start_index and equity > 0:
            sig = df['signal'].iloc[i]
            if sig != 0:
                entry_price = df['entry_price'].iloc[i]
                ema_slow_t = df['ema_slow'].iloc[i] if 'ema_slow' in df.columns else (df['ema100'].iloc[i] if 'ema100' in df.columns else np.nan)
                if pd.isna(entry_price) or pd.isna(ema_slow_t):
                    continue
                # Calculate risk = |entry - EMA_slow[t]|
                risk = abs(entry_price - ema_slow_t)
                # Skip if risk <= 0 or pathological
                if risk <= 1e-10:
                    continue
                if min_risk_atr:
                    atr_val = df['atr14'].iloc[i] if 'atr14' in df.columns else float('nan')
                    if pd.isna(atr_val) or risk < atr_val * atr_threshold:
                        continue
                # Calculate SL/TP
                if sig == 1:  # long
                    sl = entry_price - risk
                    tp = entry_price + rr * risk
                    side = 'long'
                elif sig == -1:  # short
                    sl = entry_price + risk
                    tp = entry_price - rr * risk
                    side = 'short'
                else:
                    continue
                # Position sizing
                if sizing == 'unit_notional':
                    qty = 1.0
                else:
                    qty = (equity * risk_fraction) / risk
                    # Cap the notional so a very tight stop cannot lever up
                    # beyond max_notional_multiple x equity.
                    max_notional = max_notional_multiple * equity
                    if qty * entry_price > max_notional:
                        qty = max_notional / entry_price
                notional = qty * entry_price
                entry_cost = notional * cost_per_side
                # Enter position
                entry_trade = Trade(
                    symbol=symbol,
                    entry_time=df['timestamp'].iloc[i] if 'timestamp' in df.columns else i,
                    exit_time=None,
                    side=side,
                    entry_price=float(entry_price),
                    exit_price=0.0,
                    sl=float(sl),
                    tp=float(tp),
                    risk=float(risk),
                    pnl=0.0,
                    pnl_net=0.0,
                    exit_reason='',
                    bar_index=i,
                    qty=float(qty),
                    notional=float(notional),
                    entry_cost=float(entry_cost),
                    exit_cost=0.0,
                    risk_pct=float(risk / entry_price) if entry_price else 0.0,
                )
                position = sig
                position_entry_idx = i
                # Charge the entry cost exactly once
                equity -= entry_cost

    # If still in position at end, close it
    if position != 0 and entry_trade is not None:
        # Close at last close price
        last_idx = len(df) - 1
        exit_price = df['close'].iloc[last_idx]
        exit_time = df['timestamp'].iloc[last_idx] if 'timestamp' in df.columns else last_idx
        if position == 1:
            pnl_per_unit = (exit_price - entry_trade.entry_price)
        else:
            pnl_per_unit = (entry_trade.entry_price - exit_price)
        pnl = pnl_per_unit * entry_trade.qty
        exit_cost = entry_trade.qty * cost_per_side * exit_price
        pnl_net = pnl - entry_trade.entry_cost - exit_cost
        entry_trade.exit_time = exit_time
        entry_trade.exit_price = exit_price
        entry_trade.exit_bar_index = last_idx
        entry_trade.pnl = pnl
        entry_trade.pnl_net = pnl_net
        entry_trade.exit_cost = exit_cost
        entry_trade.exit_reason = 'end'
        trades.append(entry_trade)
        equity += pnl - exit_cost

    # The last equity row was recorded before the final close, so refresh it
    # with the settled equity.
    if equity_curve:
        equity_curve[-1]['equity'] = equity

    equity_df = pd.DataFrame(equity_curve)
    return trades, equity_df
