# EMA Hourly Continuation — DEEP/USDT P20_34

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.8727 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -7.7959 |
| sortino_ratio | -3.5649 |
| max_drawdown | 0.9732 |
| cagr | -0.8312 |
| net_avg_win | 29.7095 |
| net_avg_loss | -43.7112 |
| avg_hold_time_bars | 2.7845 |
| exposure | 0.1346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
