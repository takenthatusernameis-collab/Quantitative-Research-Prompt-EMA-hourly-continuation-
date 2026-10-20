# EMA Hourly Continuation — MOODENG/USDT P8_50

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 904 |
| net_profit_factor | 0.6552 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -4.7418 |
| sortino_ratio | -2.2061 |
| max_drawdown | 0.8899 |
| cagr | -0.6526 |
| net_avg_win | 39.2839 |
| net_avg_loss | -54.1548 |
| avg_hold_time_bars | 9.0874 |
| exposure | 0.4545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
