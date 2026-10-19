# Pooled Cross-Symbol OOS — EMA Hourly Continuation

**Timestamp:** 20261019_015325

**Mode:** pooled cross-symbol out-of-sample (test = trailing 35% of each symbol)

**Symbols (market-cap desc):** BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT

**Config:** rr=1.5, min_risk_atr=True, atr_threshold=0.75, stricter_trend=False, costs=10.0bps+2.0bps per side


## Pooled OOS Metrics

| Metric | Value |
|---|---|
| trade_count | 19 |
| net_profit_factor | 0.2175 |
| net_win_rate | 0.3158 |
| gross_profit_factor | 0.5881 |
| gross_win_rate | 0.3158 |
| sharpe_ratio | -13.2911 |
| sortino_ratio | -6.2363 |
| max_drawdown | 0.0009 |
| cagr | -0.0414 |
| net_avg_win | 1.4687 |
| net_avg_loss | -3.1164 |
| avg_hold_time_bars | 7.5789 |
| exposure | 0.0000 |
| n_symbols | 5 |

## Per-Symbol OOS Metrics (market-cap order)

| Symbol | Test Bars | Test Signals | Trades | Net PF | Net WR | Net Sharpe | Max DD |
|---|---|---|---|---|---|---|---|
| BTC/USDT | 175 | 8 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| ETH/USDT | 175 | 6 | 3 | 0.2264 | 0.3333 | -9.9356 | 0.0037 |
| SOL/USDT | 175 | 5 | 4 | 0.2124 | 0.2500 | -9.6202 | 0.0005 |
| BNB/USDT | 175 | 4 | 4 | 0.1804 | 0.5000 | -9.7677 | 0.0008 |
| XRP/USDT | 175 | 15 | 8 | 0.5869 | 0.2500 | -5.8285 | 0.0000 |

## Signal Sparsity

Most OOS windows produce few/no qualifying signals (EMA stack + pullback cross + ATR min-risk filter). With 500-bar fixtures (~21 days) and a 35% test split, each test window is ~175 bars; after the 100-bar EMA warmup the effective OOS sample is short, which limits trade counts and the statistical power of OOS metrics.
