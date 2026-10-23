# EMA Hourly Continuation — FLIP/USDT P21_26

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.1864 |
| net_win_rate | 0.3114 |
| gross_profit_factor | 0.7396 |
| gross_win_rate | 0.4095 |
| sharpe_ratio | -13.9859 |
| sortino_ratio | -6.1644 |
| max_drawdown | 0.9998 |
| cagr | -0.9658 |
| net_avg_win | 8.4813 |
| net_avg_loss | -20.5827 |
| avg_hold_time_bars | 3.9008 |
| exposure | 0.1537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
