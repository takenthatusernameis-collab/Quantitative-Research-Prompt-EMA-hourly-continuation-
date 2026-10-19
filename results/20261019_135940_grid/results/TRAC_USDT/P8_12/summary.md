# EMA Hourly Continuation — TRAC/USDT P8_12

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1483 |
| net_profit_factor | 0.2059 |
| net_win_rate | 0.3554 |
| gross_profit_factor | 0.7292 |
| gross_win_rate | 0.4201 |
| sharpe_ratio | -15.6681 |
| sortino_ratio | -8.6625 |
| max_drawdown | 1.0000 |
| cagr | -0.9903 |
| net_avg_win | 4.9209 |
| net_avg_loss | -13.1728 |
| avg_hold_time_bars | 2.5893 |
| exposure | 0.1745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
