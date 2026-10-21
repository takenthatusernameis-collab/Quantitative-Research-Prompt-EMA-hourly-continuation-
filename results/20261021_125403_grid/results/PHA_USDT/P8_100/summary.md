# EMA Hourly Continuation — PHA/USDT P8_100

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.8182 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -1.4747 |
| sortino_ratio | -0.4695 |
| max_drawdown | 0.4593 |
| cagr | -0.1961 |
| net_avg_win | 78.5030 |
| net_avg_loss | -90.3424 |
| avg_hold_time_bars | 27.7034 |
| exposure | 0.6284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
