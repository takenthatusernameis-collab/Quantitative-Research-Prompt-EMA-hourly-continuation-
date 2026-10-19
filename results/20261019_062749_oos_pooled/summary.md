# Pooled Cross-Symbol OOS — EMA Hourly Continuation

**Timestamp:** 20261019_062749

**Mode:** pooled cross-symbol out-of-sample (test = trailing 35% of each symbol)

**Symbols (market-cap desc):** BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT

**Config:** rr=1.5, min_risk_atr=True, atr_threshold=1.5, stricter_trend=False, costs=10.0bps+2.0bps per side


## Pooled OOS Metrics

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.7922 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 1.0641 |
| gross_win_rate | 0.4139 |
| sharpe_ratio | -1.2193 |
| sortino_ratio | -0.4347 |
| max_drawdown | 0.4467 |
| cagr | -0.3606 |
| net_avg_win | 318.0055 |
| net_avg_loss | -283.5012 |
| avg_hold_time_bars | 18.0232 |
| exposure | 0.1974 |
| n_symbols | 5 |

## Per-Symbol OOS Metrics (market-cap order)

| Symbol | Test Bars | Test Signals | Trades | Net PF | Net WR | Net Sharpe | Max DD |
|---|---|---|---|---|---|---|---|
| BTC/USDT | 8750 | 313 | 67 | 0.7916 | 0.4328 | -1.8982 | 1.8809 |
| ETH/USDT | 7700 | 294 | 50 | 0.7894 | 0.3800 | -1.0934 | 0.0564 |
| SOL/USDT | 7700 | 287 | 48 | 1.1715 | 0.3750 | 0.3048 | 0.0021 |
| BNB/USDT | 7700 | 287 | 67 | 0.8126 | 0.3881 | -1.2244 | 0.0174 |
| XRP/USDT | 7700 | 312 | 70 | 0.7749 | 0.4714 | -1.3102 | 0.0000 |

## Signal Sparsity

Most OOS windows produce few/no qualifying signals (EMA stack + pullback cross + ATR min-risk filter). With 500-bar fixtures (~21 days) and a 35% test split, each test window is ~175 bars; after the 100-bar EMA warmup the effective OOS sample is short, which limits trade counts and the statistical power of OOS metrics.
