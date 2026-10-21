# EMA Hourly Continuation — ZIL/USDT P50_100

**Symbol:** ZIL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7046 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9697 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.2565 |
| sortino_ratio | -0.6476 |
| max_drawdown | 0.5658 |
| cagr | -0.2565 |
| net_avg_win | 63.5632 |
| net_avg_loss | -87.1113 |
| avg_hold_time_bars | 8.7406 |
| exposure | 0.1593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
