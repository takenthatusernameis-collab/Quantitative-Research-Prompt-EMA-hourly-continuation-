# EMA Hourly Continuation — AEVO/USDT P50_55

**Symbol:** AEVO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 876 |
| net_profit_factor | 0.3210 |
| net_win_rate | 0.3847 |
| gross_profit_factor | 0.8689 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -11.1525 |
| sortino_ratio | -4.7660 |
| max_drawdown | 0.9982 |
| cagr | -0.9173 |
| net_avg_win | 14.0010 |
| net_avg_loss | -27.2722 |
| avg_hold_time_bars | 2.0148 |
| exposure | 0.0799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
