# EMA Hourly Continuation — IOTA/USDT P20_50

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.5267 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.9959 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -7.0905 |
| sortino_ratio | -3.1394 |
| max_drawdown | 0.9791 |
| cagr | -0.7849 |
| net_avg_win | 24.0427 |
| net_avg_loss | -38.6548 |
| avg_hold_time_bars | 4.9200 |
| exposure | 0.2210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
