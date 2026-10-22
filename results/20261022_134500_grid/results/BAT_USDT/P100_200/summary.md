# EMA Hourly Continuation — BAT/USDT P100_200

**Symbol:** BAT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.4784 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8762 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -4.0228 |
| sortino_ratio | -1.1502 |
| max_drawdown | 0.7480 |
| cagr | -0.4201 |
| net_avg_win | 37.3697 |
| net_avg_loss | -64.3864 |
| avg_hold_time_bars | 7.9432 |
| exposure | 0.1462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
