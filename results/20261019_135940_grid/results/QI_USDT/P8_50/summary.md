# EMA Hourly Continuation — QI/USDT P8_50

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.6196 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.9764 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -6.0730 |
| sortino_ratio | -2.7086 |
| max_drawdown | 0.9632 |
| cagr | -0.7276 |
| net_avg_win | 34.2986 |
| net_avg_loss | -45.7476 |
| avg_hold_time_bars | 9.8554 |
| exposure | 0.4504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
