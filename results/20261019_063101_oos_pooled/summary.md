# Pooled Cross-Symbol OOS — EMA Hourly Continuation

**Timestamp:** 20261019_063101

**Mode:** pooled cross-symbol out-of-sample (test = trailing 35% of each symbol)

**Symbols (market-cap desc):** BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT

**Config:** rr=1.5, min_risk_atr=True, atr_threshold=0.75, stricter_trend=False, costs=10.0bps+2.0bps per side


## Pooled OOS Metrics

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.6952 |
| net_win_rate | 0.4099 |
| gross_profit_factor | 1.0107 |
| gross_win_rate | 0.4099 |
| sharpe_ratio | -1.9169 |
| sortino_ratio | -1.0191 |
| max_drawdown | 0.6544 |
| cagr | -0.5946 |
| net_avg_win | 198.1942 |
| net_avg_loss | -198.0506 |
| avg_hold_time_bars | 10.8859 |
| exposure | 0.2087 |
| n_symbols | 5 |

## Per-Symbol OOS Metrics (market-cap order)

| Symbol | Test Bars | Test Signals | Trades | Net PF | Net WR | Net Sharpe | Max DD |
|---|---|---|---|---|---|---|---|
| BTC/USDT | 8750 | 313 | 124 | 0.6920 | 0.3871 | 0.4027 | 2.9443 |
| ETH/USDT | 7700 | 294 | 119 | 0.7967 | 0.4370 | -1.8072 | 0.0817 |
| SOL/USDT | 7700 | 287 | 132 | 0.8792 | 0.3712 | -1.1395 | 0.0039 |
| BNB/USDT | 7700 | 287 | 150 | 0.6955 | 0.3933 | -2.8661 | 0.0341 |
| XRP/USDT | 7700 | 312 | 141 | 0.8006 | 0.4610 | -1.8986 | 0.0001 |

## Signal Sparsity

Most OOS windows produce few/no qualifying signals (EMA stack + pullback cross + ATR min-risk filter). With 500-bar fixtures (~21 days) and a 35% test split, each test window is ~175 bars; after the 100-bar EMA warmup the effective OOS sample is short, which limits trade counts and the statistical power of OOS metrics.
