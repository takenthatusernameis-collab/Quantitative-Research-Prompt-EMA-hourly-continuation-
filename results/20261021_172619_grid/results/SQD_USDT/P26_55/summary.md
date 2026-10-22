# EMA Hourly Continuation — SQD/USDT P26_55

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.8604 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0702 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -1.0536 |
| sortino_ratio | -0.3217 |
| max_drawdown | 0.3803 |
| cagr | -0.1397 |
| net_avg_win | 83.8569 |
| net_avg_loss | -103.9289 |
| avg_hold_time_bars | 7.3096 |
| exposure | 0.1498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
