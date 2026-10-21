# EMA Hourly Continuation — IOTA/USDT P8_100

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8893 |
| net_win_rate | 0.5219 |
| gross_profit_factor | 1.0801 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -0.7454 |
| sortino_ratio | -0.2405 |
| max_drawdown | 0.2907 |
| cagr | -0.1090 |
| net_avg_win | 77.1662 |
| net_avg_loss | -94.7250 |
| avg_hold_time_bars | 28.7908 |
| exposure | 0.6570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
