# EMA Hourly Continuation — AIOZ/USDT P26_34

**Symbol:** AIOZ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1148 |
| net_profit_factor | 0.3623 |
| net_win_rate | 0.3754 |
| gross_profit_factor | 0.7660 |
| gross_win_rate | 0.4129 |
| sharpe_ratio | -12.4475 |
| sortino_ratio | -6.0156 |
| max_drawdown | 0.9996 |
| cagr | -0.9564 |
| net_avg_win | 13.1755 |
| net_avg_loss | -21.8617 |
| avg_hold_time_bars | 2.2805 |
| exposure | 0.1190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
