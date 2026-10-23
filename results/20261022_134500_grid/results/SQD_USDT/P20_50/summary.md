# EMA Hourly Continuation — SQD/USDT P20_50

**Symbol:** SQD/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.6776 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 1.0204 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -4.5562 |
| sortino_ratio | -1.9875 |
| max_drawdown | 0.9017 |
| cagr | -0.6111 |
| net_avg_win | 42.2805 |
| net_avg_loss | -58.3476 |
| avg_hold_time_bars | 5.1168 |
| exposure | 0.2225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
