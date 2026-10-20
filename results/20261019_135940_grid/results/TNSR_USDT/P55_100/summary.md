# EMA Hourly Continuation — TNSR/USDT P55_100

**Symbol:** TNSR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.6133 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.9728 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -4.4593 |
| sortino_ratio | -1.5667 |
| max_drawdown | 0.8552 |
| cagr | -0.5317 |
| net_avg_win | 45.5208 |
| net_avg_loss | -66.5981 |
| avg_hold_time_bars | 6.0032 |
| exposure | 0.1706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
