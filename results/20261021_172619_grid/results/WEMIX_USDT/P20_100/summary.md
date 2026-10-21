# EMA Hourly Continuation — WEMIX/USDT P20_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.5754 |
| net_win_rate | 0.4125 |
| gross_profit_factor | 0.7281 |
| gross_win_rate | 0.4125 |
| sharpe_ratio | -3.8343 |
| sortino_ratio | -1.1066 |
| max_drawdown | 0.7287 |
| cagr | -0.4008 |
| net_avg_win | 57.0124 |
| net_avg_loss | -69.5640 |
| avg_hold_time_bars | 23.3837 |
| exposure | 0.4432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
