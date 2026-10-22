# EMA Hourly Continuation — IOTX/USDT P26_34

**Symbol:** IOTX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.6928 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0250 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.6073 |
| sortino_ratio | -0.3430 |
| max_drawdown | 0.3811 |
| cagr | -0.1442 |
| net_avg_win | 65.1691 |
| net_avg_loss | -98.4662 |
| avg_hold_time_bars | 5.4977 |
| exposure | 0.0547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
