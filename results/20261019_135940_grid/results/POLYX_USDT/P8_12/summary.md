# EMA Hourly Continuation — POLYX/USDT P8_12

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1635 |
| net_profit_factor | 0.2650 |
| net_win_rate | 0.3755 |
| gross_profit_factor | 0.7839 |
| gross_win_rate | 0.4398 |
| sharpe_ratio | -16.0585 |
| sortino_ratio | -9.3855 |
| max_drawdown | 1.0000 |
| cagr | -0.9924 |
| net_avg_win | 5.8727 |
| net_avg_loss | -13.3259 |
| avg_hold_time_bars | 2.4061 |
| exposure | 0.1788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
