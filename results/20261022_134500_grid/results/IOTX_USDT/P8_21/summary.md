# EMA Hourly Continuation — IOTX/USDT P8_21

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1610 |
| net_profit_factor | 0.4939 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.9819 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -10.6329 |
| sortino_ratio | -6.0263 |
| max_drawdown | 0.9995 |
| cagr | -0.9494 |
| net_avg_win | 13.5104 |
| net_avg_loss | -22.2398 |
| avg_hold_time_bars | 3.1019 |
| exposure | 0.2270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
