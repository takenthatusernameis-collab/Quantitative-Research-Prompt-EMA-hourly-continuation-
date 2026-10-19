"""Performance metrics calculation."""
from typing import List, Dict, Any
import numpy as np
import pandas as pd


def calculate_returns(equity_df: pd.DataFrame) -> np.ndarray:
    """Calculate simple returns from equity curve.

    Barred at a non-positive equity: once the equity is exhausted the strategy
    is bankrupt and the return series is undefined (and would otherwise produce
    sign-flipped, meaningless values).
    """
    if len(equity_df) == 0:
        return np.array([])
    equity = equity_df['equity'].values
    if len(equity) < 2:
        return np.array([])
    denom = equity[:-1]
    valid = denom > 0
    if not np.any(valid):
        return np.array([])
    return np.diff(equity)[valid] / denom[valid]


HOURLY_PERIODS_PER_YEAR = 24 * 365


def sharpe_ratio(returns: np.ndarray, risk_free: float = 0.0, periods_per_year: int = HOURLY_PERIODS_PER_YEAR) -> float:
    """Calculate annualized Sharpe ratio (hourly bars)."""
    if len(returns) == 0 or np.std(returns) == 0:
        return 0.0
    return float((np.mean(returns) - risk_free) / np.std(returns) * np.sqrt(periods_per_year))


def sortino_ratio(returns: np.ndarray, risk_free: float = 0.0, periods_per_year: int = HOURLY_PERIODS_PER_YEAR) -> float:
    """Calculate annualized Sortino ratio (hourly bars)."""
    if len(returns) == 0:
        return 0.0
    neg_returns = returns[returns < 0]
    downside_std = np.std(neg_returns) if len(neg_returns) > 0 else 0.0
    if downside_std == 0:
        return 0.0
    return float((np.mean(returns) - risk_free) / downside_std * np.sqrt(periods_per_year))


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
        if peak <= 0:
            # Equity exhausted; the drawdown from the peak to zero is total.
            max_dd = max(max_dd, 1.0)
            continue
        dd = (peak - e) / peak
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
    years = n_periods / HOURLY_PERIODS_PER_YEAR
    if years <= 0:
        return 0.0
    return float((equity[-1] / equity[0]) ** (1.0 / years) - 1.0)


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
    """Calculate average hold time (in bars)."""
    if not trades:
        return 0.0
    holds = []
    for t in trades:
        entry_bar = getattr(t, 'bar_index', None)
        exit_bar = getattr(t, 'exit_bar_index', None)
        if entry_bar is not None and exit_bar is not None and exit_bar >= 0:
            holds.append(float(exit_bar - entry_bar))
            continue
        # Fallback to datetime difference in hours
        if hasattr(t.entry_time, 'to_pydatetime') or isinstance(t.entry_time, pd.Timestamp):
            try:
                if hasattr(t.exit_time, 'to_pydatetime') or isinstance(t.exit_time, pd.Timestamp):
                    delta = (pd.Timestamp(t.exit_time) - pd.Timestamp(t.entry_time))
                    holds.append(delta.total_seconds() / 3600.0)
                    continue
            except Exception:
                pass
    return float(np.mean(holds)) if holds else 0.0


def exposure(equity_df: pd.DataFrame) -> float:
    """Fraction of bars with an open position (exposure)."""
    if len(equity_df) == 0 or 'position' not in equity_df.columns:
        return 0.0
    pos = equity_df['position'].values
    return float(np.mean(pos != 0))


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
    metrics['avg_hold_time_bars'] = float(avg_hold_time(trades))
    metrics['exposure'] = float(exposure(equity_df))
    return metrics
