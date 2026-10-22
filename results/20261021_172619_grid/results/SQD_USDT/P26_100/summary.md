# EMA Hourly Continuation — SQD/USDT P26_100

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.8476 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1667 |
| sortino_ratio | -0.3578 |
| max_drawdown | 0.4122 |
| cagr | -0.1543 |
| net_avg_win | 83.7461 |
| net_avg_loss | -98.8029 |
| avg_hold_time_bars | 15.3536 |
| exposure | 0.3204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
