# Pooled Cross-Symbol OOS — EMA Hourly Continuation

**Timestamp:** 20261019_052323

**Mode:** pooled cross-symbol out-of-sample (test = trailing 35% of each symbol)

**Symbols (market-cap desc):** BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT

**Config:** rr=1.5, min_risk_atr=True, atr_threshold=0.75, stricter_trend=False, costs=10.0bps+2.0bps per side


## Pooled OOS Metrics

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.6239 |
| net_win_rate | 0.3941 |
| gross_profit_factor | 0.9578 |
| gross_win_rate | 0.3941 |
| sharpe_ratio | -3.1408 |
| sortino_ratio | -1.5913 |
| max_drawdown | 0.4401 |
| cagr | -0.5846 |
| net_avg_win | 133.2139 |
| net_avg_loss | -138.9130 |
| avg_hold_time_bars | 10.3221 |
| exposure | 0.2217 |
| n_symbols | 5 |

## Per-Symbol OOS Metrics (market-cap order)

| Symbol | Test Bars | Test Signals | Trades | Net PF | Net WR | Net Sharpe | Max DD |
|---|---|---|---|---|---|---|---|
| BTC/USDT | 5250 | 180 | 70 | 0.6162 | 0.3571 | -0.9555 | 1.8534 |
| ETH/USDT | 5250 | 214 | 82 | 0.8853 | 0.4268 | -1.4806 | 0.0524 |
| SOL/USDT | 5250 | 191 | 93 | 0.6122 | 0.3548 | -3.1277 | 0.0035 |
| BNB/USDT | 5250 | 192 | 107 | 0.5788 | 0.3925 | -4.3132 | 0.0280 |
| XRP/USDT | 5250 | 213 | 92 | 0.6780 | 0.4348 | -2.8792 | 0.0001 |

## Signal Sparsity

Most OOS windows produce few/no qualifying signals (EMA stack + pullback cross + ATR min-risk filter). With 500-bar fixtures (~21 days) and a 35% test split, each test window is ~175 bars; after the 100-bar EMA warmup the effective OOS sample is short, which limits trade counts and the statistical power of OOS metrics.
