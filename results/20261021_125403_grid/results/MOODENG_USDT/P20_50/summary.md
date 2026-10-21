# EMA Hourly Continuation — MOODENG/USDT P20_50

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7770 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.9094 |
| sortino_ratio | -0.6262 |
| max_drawdown | 0.4728 |
| cagr | -0.2511 |
| net_avg_win | 73.1349 |
| net_avg_loss | -92.3990 |
| avg_hold_time_bars | 8.1481 |
| exposure | 0.1948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
