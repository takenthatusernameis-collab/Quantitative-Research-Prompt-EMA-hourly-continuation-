# Pooled Cross-Symbol OOS — EMA Hourly Continuation

**Timestamp:** 20261019_062711

**Mode:** pooled cross-symbol out-of-sample (test = trailing 35% of each symbol)

**Symbols (market-cap desc):** BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT

**Config:** rr=1.5, min_risk_atr=True, atr_threshold=1.0, stricter_trend=False, costs=10.0bps+2.0bps per side


## Pooled OOS Metrics

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6501 |
| net_win_rate | 0.3965 |
| gross_profit_factor | 0.9183 |
| gross_win_rate | 0.3965 |
| sharpe_ratio | -2.0586 |
| sortino_ratio | -0.9915 |
| max_drawdown | 0.6852 |
| cagr | -0.6318 |
| net_avg_win | 229.8864 |
| net_avg_loss | -232.3481 |
| avg_hold_time_bars | 13.4371 |
| exposure | 0.2358 |
| n_symbols | 5 |

## Per-Symbol OOS Metrics (market-cap order)

| Symbol | Test Bars | Test Signals | Trades | Net PF | Net WR | Net Sharpe | Max DD |
|---|---|---|---|---|---|---|---|
| BTC/USDT | 8750 | 313 | 105 | 0.6457 | 0.3524 | -1.9285 | 3.0767 |
| ETH/USDT | 7700 | 294 | 91 | 0.7779 | 0.4066 | -1.6303 | 0.0760 |
| SOL/USDT | 7700 | 287 | 95 | 0.8911 | 0.3474 | -0.8454 | 0.0030 |
| BNB/USDT | 7700 | 287 | 117 | 0.7285 | 0.3932 | -2.2531 | 0.0267 |
| XRP/USDT | 7700 | 312 | 109 | 0.8410 | 0.4771 | -1.3900 | 0.0001 |

## Signal Sparsity

Most OOS windows produce few/no qualifying signals (EMA stack + pullback cross + ATR min-risk filter). With 500-bar fixtures (~21 days) and a 35% test split, each test window is ~175 bars; after the 100-bar EMA warmup the effective OOS sample is short, which limits trade counts and the statistical power of OOS metrics.
