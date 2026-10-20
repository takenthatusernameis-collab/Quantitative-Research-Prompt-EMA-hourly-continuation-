# EMA Hourly Continuation — SQD/USDT P12_200

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7578 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9578 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -1.8525 |
| sortino_ratio | -0.5598 |
| max_drawdown | 0.5421 |
| cagr | -0.2297 |
| net_avg_win | 68.6127 |
| net_avg_loss | -86.5041 |
| avg_hold_time_bars | 33.0434 |
| exposure | 0.6803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
