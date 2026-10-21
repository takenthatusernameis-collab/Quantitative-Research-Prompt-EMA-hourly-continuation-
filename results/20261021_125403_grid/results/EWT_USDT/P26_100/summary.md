# EMA Hourly Continuation — EWT/USDT P26_100

**Symbol:** EWT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.6938 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8570 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -2.2496 |
| sortino_ratio | -0.6684 |
| max_drawdown | 0.6009 |
| cagr | -0.2656 |
| net_avg_win | 59.6297 |
| net_avg_loss | -75.9395 |
| avg_hold_time_bars | 13.2334 |
| exposure | 0.2629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
