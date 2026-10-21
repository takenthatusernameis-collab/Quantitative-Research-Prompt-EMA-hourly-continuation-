# EMA Hourly Continuation — PHA/USDT P8_12

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.7667 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0423 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -1.4799 |
| sortino_ratio | -0.3737 |
| max_drawdown | 0.4548 |
| cagr | -0.1575 |
| net_avg_win | 73.2056 |
| net_avg_loss | -99.2790 |
| avg_hold_time_bars | 4.2565 |
| exposure | 0.0596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
