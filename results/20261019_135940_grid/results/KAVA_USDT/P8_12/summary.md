# EMA Hourly Continuation — KAVA/USDT P8_12

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1888 |
| net_profit_factor | 0.1490 |
| net_win_rate | 0.3231 |
| gross_profit_factor | 0.6333 |
| gross_win_rate | 0.4084 |
| sharpe_ratio | -20.5352 |
| sortino_ratio | -13.1953 |
| max_drawdown | 1.0000 |
| cagr | -0.9992 |
| net_avg_win | 2.8714 |
| net_avg_loss | -9.1953 |
| avg_hold_time_bars | 2.4195 |
| exposure | 0.2076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
