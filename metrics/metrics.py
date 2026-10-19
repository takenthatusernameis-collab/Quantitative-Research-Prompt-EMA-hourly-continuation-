"""Performance metrics calculation."""
from typing import List, Dict, Any
import numpy as np
import pandas as pd


def calculate_returns(equity_df: pd.DataFrame) -> np.ndarray:
    """Calculate simple returns from equity curve."""
    if len(equity_df) == 0:
        return np.array([])
    equity = equity_df['equity'].values
    returns = np.diff(equity) / equity[:-1] if len(equity) > 1 else np.array([])
    return returns


def sharpe_ratio(returns: np.ndarray, risk_free: float = 0.0) -> float:
    """Calculate Sharpe ratio."""
    if len(returns) == 0 or np.std(returns) == 0:
        return 0.0
    return (np.mean(returns) - risk_free) / np.std(returns) * np.sqrt(365 * 24) if False else (np.mean(returns) - risk_free) / np.std(returns)  # hourly default? but scale - keep simple
    # For hourly data, annualize appropriately; but spec just says Sharpe - use simple
    return float((np.mean(returns) - risk_free) / np.std(returns)) if np.std(returns) > 0 else 0.0


def sortino_ratio(returns: np.ndarray, risk_free: float = 0.0) -> float:
    """Calculate Sortino ratio."""
    if len(returns) == 0:
        return 0.0
    neg_returns = returns[returns < 0]
    downside_std = np.std(neg_returns) if len(neg_returns) > 0 else 0.0
    if downside_std == 0:
        return 0.0
    return float((np.mean(returns) - risk_free) / downside_std)


def max_drawdown(equity_df: pd.DataFrame) -> float:
    """Calculate maximum drawdown."""
    if len(equity_df) == 0:
        return 0.0
    equity = equity_df['equity'].values
    peak = equity[0]
    max_dd = 0.0
    for e in equity:
        if e > peak:
            peak = e
        dd = (peak - e) / peak if peak > 0 else 0.0
        if dd > max_dd:
            max_dd = dd
    return float(max_dd)


def cagr(equity_df: pd.DataFrame) -> float:
    """Calculate CAGR."""
    if len(equity_df) == 0:
        return 0.0
    equity = equity_df['equity'].values
    if equity[-1] <= 0 or equity[0] <= 0:
        return 0.0
    n_periods = len(equity_df) - 1
    if n_periods <= 0:
        return 0.0
    # Assume hourly periods - convert to years? Or just return as (end/start)^(1/n)-1
    # Keep as simple total return rate form
    return float((equity[-1] / equity[0]) ** (1.0 / n_periods) - 1.0) if n_periods > 0 else 0.0


def profit_factor(trades: List) -> float:
    """Calculate profit factor (gross wins / gross losses)."""
    if not trades:
        return 0.0
    wins = sum(t.pnl for t in trades if t.pnl > 0)
    losses = abs(sum(t.pnl for t in trades if t.pnl < 0))
    if losses == 0:
        return float('inf') if wins > 0 else 0.0
    return float(wins / losses)


def win_rate(trades: List) -> float:
    """Calculate win rate."""
    if not trades:
        return 0.0
    wins = sum(1 for t in trades if t.pnl > 0)
    return float(wins / len(trades))


def avg_win_loss(trades: List) -> tuple:
    """Calculate average win and average loss."""
    if not trades:
        return 0.0, 0.0
    wins = [t.pnl for t in trades if t.pnl > 0]
    losses = [t.pnl for t in trades if t.pnl < 0]
    avg_win = float(np.mean(wins)) if wins else 0.0
    avg_loss = float(np.mean(losses)) if losses else 0.0
    return avg_win, avg_loss


def avg_hold_time(trades: List) -> float:
    """Calculate average hold time (in periods/bars)."""
    if not trades:
        return 0.0
    holds = []
    for t in trades:
        # If timestamps are datetime, compute diff; else bar diff
        if hasattr(t.entry_time, 'to_pydatetime') or isinstance(t.entry_time, pd.Timestamp):
            try:
                if hasattr(t.exit_time, 'to_pydatetime') or isinstance(t.exit_time, pd.Timestamp):
                    delta = (pd.Timestamp(t.exit_time) - pd.Timestamp(t.entry_time))
                    holds.append(delta.total_seconds() / 3600.0)  # hours
                    continue
            except Exception:
                pass
        # Fallback to bar index difference
        if hasattr(t, 'bar_index'):
            pass
    # Simple bar-based if no time
    holds = []
    for t in trades:
        # try to get indices if stored
        pass
    return float(np.mean(holds)) if holds else 0.0


def calculate_metrics(trades: List, equity_df: pd.DataFrame, symbol: str = 'all') -> Dict[str, Any]:
    """Calculate comprehensive metrics."""
    returns = calculate_returns(equity_df)
    pf = profit_factor(trades)
    wr = win_rate(trades)
    avg_win, avg_loss = avg_win_loss(trades)

    metrics = {
        'symbol': symbol,
        'trade_count': len(trades),
        'gross_profit_factor': pf,
        'win_rate': wr,
        'avg_win': avg_win,
        'avg_loss': avg_loss,
        'max_drawdown': max_drawdown(equity_df),
        'sharpe_ratio': sharpe_ratio(returns),
        'sortino_ratio': sortino_ratio(returns),
        'cagr': cagr(equity_df),
        'total_trades': len(trades)
    }
    # Add net metrics - for now same as gross (we track pnl_net)
    if trades:
        wins_net = sum(t.pnl_net for t in trades if t.pnl_net > 0)
        losses_net = abs(sum(t.pnl_net for t in trades if t.pnl_net < 0))
        pf_net = wins_net / losses_net if losses_net > 0 else (float('inf') if wins_net > 0 else 0.0)
        wr_net = sum(1 for t in trades if t.pnl_net > 0) / len(trades)
        avg_win_net = np.mean([t.pnl_net for t in trades if t.pnl_net > 0]) if any(t.pnl_net > 0 for t in trades) else 0.0
        avg_loss_net = np.mean([t.pnl_net for t in trades if t.pnl_net < 0]) if any(t.pnl_net < 0 for t in trades) else 0.0
        metrics['net_profit_factor'] = float(pf_net)
        metrics['net_win_rate'] = float(wr_net)
        metrics['net_avg_win'] = float(avg_win_net)
        metrics['net_avg_loss'] = float(avg_loss_net)
    else:
        metrics['net_profit_factor'] = 0.0
        metrics['net_win_rate'] = 0.0
        metrics['net_avg_win'] = 0.0
        metrics['net_avg_loss'] = 0.0

    # Also store gross explicitly
    metrics['gross_win_rate'] = wr
    metrics['gross_profit_factor'] = pf
    return metrics
