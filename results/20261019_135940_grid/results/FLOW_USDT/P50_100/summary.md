# EMA Hourly Continuation — FLOW/USDT P50_100

**Symbol:** FLOW/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.4672 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8405 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -5.9149 |
| sortino_ratio | -2.1368 |
| max_drawdown | 0.9292 |
| cagr | -0.6480 |
| net_avg_win | 27.9473 |
| net_avg_loss | -47.9512 |
| avg_hold_time_bars | 5.1865 |
| exposure | 0.1542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
