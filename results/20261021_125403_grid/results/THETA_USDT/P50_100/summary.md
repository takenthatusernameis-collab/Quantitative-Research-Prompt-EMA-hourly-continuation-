# EMA Hourly Continuation — THETA/USDT P50_100

**Symbol:** THETA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7823 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.3366 |
| sortino_ratio | -0.3525 |
| max_drawdown | 0.3476 |
| cagr | -0.1497 |
| net_avg_win | 70.2970 |
| net_avg_loss | -92.5693 |
| avg_hold_time_bars | 9.1098 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
