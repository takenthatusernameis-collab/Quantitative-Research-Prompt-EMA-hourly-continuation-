# Pooled Cross-Symbol OOS — EMA Hourly Continuation

**Timestamp:** 20261019_062621

**Mode:** pooled cross-symbol out-of-sample (test = trailing 35% of each symbol)

**Symbols (market-cap desc):** BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT

**Config:** rr=1.5, min_risk_atr=True, atr_threshold=0.5, stricter_trend=False, costs=10.0bps+2.0bps per side


## Pooled OOS Metrics

| Metric | Value |
|---|---|
| trade_count | 826 |
| net_profit_factor | 0.6354 |
| net_win_rate | 0.4068 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.4080 |
| sharpe_ratio | -2.1419 |
| sortino_ratio | -1.3561 |
| max_drawdown | 0.8122 |
| cagr | -0.7725 |
| net_avg_win | 165.2770 |
| net_avg_loss | -178.3751 |
| avg_hold_time_bars | 9.3172 |
| exposure | 0.2218 |
| n_symbols | 5 |

## Per-Symbol OOS Metrics (market-cap order)

| Symbol | Test Bars | Test Signals | Trades | Net PF | Net WR | Net Sharpe | Max DD |
|---|---|---|---|---|---|---|---|
| BTC/USDT | 8750 | 313 | 149 | 0.6319 | 0.3691 | 0.9669 | 3.7346 |
| ETH/USDT | 7700 | 294 | 161 | 0.7260 | 0.4348 | -2.6506 | 0.1179 |
| SOL/USDT | 7700 | 287 | 166 | 0.8081 | 0.3675 | -1.7797 | 0.0048 |
| BNB/USDT | 7700 | 287 | 170 | 0.6970 | 0.4176 | -3.0589 | 0.0365 |
| XRP/USDT | 7700 | 312 | 180 | 0.7534 | 0.4389 | -2.5313 | 0.0001 |

## Signal Sparsity

Most OOS windows produce few/no qualifying signals (EMA stack + pullback cross + ATR min-risk filter). With 500-bar fixtures (~21 days) and a 35% test split, each test window is ~175 bars; after the 100-bar EMA warmup the effective OOS sample is short, which limits trade counts and the statistical power of OOS metrics.
