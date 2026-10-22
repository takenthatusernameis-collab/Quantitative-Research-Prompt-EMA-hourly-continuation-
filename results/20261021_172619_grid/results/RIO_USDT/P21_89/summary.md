# EMA Hourly Continuation — RIO/USDT P21_89

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8258 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9428 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -1.4539 |
| sortino_ratio | -0.4571 |
| max_drawdown | 0.4942 |
| cagr | -0.1923 |
| net_avg_win | 84.1904 |
| net_avg_loss | -94.2279 |
| avg_hold_time_bars | 14.4990 |
| exposure | 0.3215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
