# EMA Hourly Continuation — CFX/USDT P50_100

**Symbol:** CFX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.7310 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9599 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -1.8005 |
| sortino_ratio | -0.4874 |
| max_drawdown | 0.4486 |
| cagr | -0.2001 |
| net_avg_win | 66.2649 |
| net_avg_loss | -88.1433 |
| avg_hold_time_bars | 9.1261 |
| exposure | 0.1481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
