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


def backtest_symbol(df: pd.DataFrame, symbol: str = 'SYMBOL',
                   taker_fee_bps: float = 10.0, slippage_bps: float = 2.0,
                   one_position: bool = True, rr: float = 1.0,
                   min_risk_atr: bool = False, atr_threshold: float = 1.0,
                   entry_start_index: int = 0, conservative_exit: bool = True) -> tuple:
    """
    Backtest a single symbol.

    Costs: taker fee and slippage per side (default 10 bps + 2 bps per side)
    SL/TP at 1:1 RR where risk = |entry - EMA100[t]| on signal bar
    """
    df = df.copy()
    if min_risk_atr and 'atr14' not in df.columns:
        tr = pd.concat([df['high']-df['low'], (df['high']-df['close'].shift()).abs(), (df['low']-df['close'].shift()).abs()], axis=1).max(axis=1)
        df['atr14'] = tr.rolling(14).mean()
    trades: List[Trade] = []
    equity = 10000.0  # starting equity
    equity_curve = []
    position = 0  # 0 no position, 1 long, -1 short
    entry_trade: Optional[Trade] = None
    position_entry_idx = -1

    # Cost per side
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
                    pnl = (exit_price - entry_trade.entry_price)
                elif tp_hit:
                    exit_price = entry_trade.tp
                    pnl = (exit_price - entry_trade.entry_price)
                    exit_reason = 'tp'
                elif sl_hit:
                    exit_price = entry_trade.sl
                    pnl = (exit_price - entry_trade.entry_price)
                    exit_reason = 'sl'
                else:
                    continue  # no exit yet
                # Calculate net pnl including costs (enter + exit)
                pnl_net = pnl - cost_per_side * entry_trade.entry_price - cost_per_side * exit_price  # rough approximation
                entry_trade.exit_time = exit_time
                entry_trade.exit_price = exit_price
                entry_trade.exit_bar_index = i
                entry_trade.pnl = pnl
                entry_trade.pnl_net = pnl_net
                entry_trade.exit_reason = exit_reason
                trades.append(entry_trade)
                equity += pnl_net  # update equity
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
                    pnl = (entry_trade.entry_price - exit_price)
                elif tp_hit:
                    exit_price = entry_trade.tp
                    pnl = (entry_trade.entry_price - exit_price)
                    exit_reason = 'tp'
                elif sl_hit:
                    exit_price = entry_trade.sl
                    pnl = (entry_trade.entry_price - exit_price)
                    exit_reason = 'sl'
                else:
                    continue
                pnl_net = pnl - cost_per_side * entry_trade.entry_price - cost_per_side * exit_price
                entry_trade.exit_time = exit_time
                entry_trade.exit_price = exit_price
                entry_trade.exit_bar_index = i
                entry_trade.pnl = pnl
                entry_trade.pnl_net = pnl_net
                entry_trade.exit_reason = exit_reason
                trades.append(entry_trade)
                equity += pnl_net
                position = 0
                entry_trade = None
                continue

        # Check for new signals if not in position (or if one_position allows new after close - but we manage)
        if position == 0 and i >= entry_start_index:
            sig = df['signal'].iloc[i]
            if sig != 0:
                entry_price = df['entry_price'].iloc[i]
                ema100_t = df['ema100'].iloc[i] if 'ema100' in df.columns else np.nan
                if pd.isna(entry_price) or pd.isna(ema100_t):
                    continue
                # Calculate risk = |entry - EMA100[t]|
                risk = abs(entry_price - ema100_t)
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
                    bar_index=i
                )
                position = sig
                position_entry_idx = i
                # Deduct entry cost
                equity -= cost_per_side * entry_price

    # If still in position at end, close it
    if position != 0 and entry_trade is not None:
        # Close at last close price
        last_idx = len(df) - 1
        exit_price = df['close'].iloc[last_idx]
        exit_time = df['timestamp'].iloc[last_idx] if 'timestamp' in df.columns else last_idx
        if position == 1:
            pnl = (exit_price - entry_trade.entry_price)
        else:
            pnl = (entry_trade.entry_price - exit_price)
        pnl_net = pnl - cost_per_side * entry_trade.entry_price - cost_per_side * exit_price
        entry_trade.exit_time = exit_time
        entry_trade.exit_price = exit_price
        entry_trade.exit_bar_index = last_idx
        entry_trade.pnl = pnl
        entry_trade.pnl_net = pnl_net
        entry_trade.exit_reason = 'end'
        trades.append(entry_trade)

    equity_df = pd.DataFrame(equity_curve)
    return trades, equity_df
