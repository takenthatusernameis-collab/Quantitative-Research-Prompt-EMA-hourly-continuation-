# EMA Hourly Continuation — PHA/USDT P8_21

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.7572 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -2.2856 |
| sortino_ratio | -0.8068 |
| max_drawdown | 0.6236 |
| cagr | -0.3095 |
| net_avg_win | 62.9318 |
| net_avg_loss | -81.2204 |
| avg_hold_time_bars | 5.8731 |
| exposure | 0.1620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
