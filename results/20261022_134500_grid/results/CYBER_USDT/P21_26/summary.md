# EMA Hourly Continuation — CYBER/USDT P21_26

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1168 |
| net_profit_factor | 0.2434 |
| net_win_rate | 0.3596 |
| gross_profit_factor | 0.6970 |
| gross_win_rate | 0.4152 |
| sharpe_ratio | -13.8671 |
| sortino_ratio | -6.8906 |
| max_drawdown | 0.9999 |
| cagr | -0.9722 |
| net_avg_win | 7.6594 |
| net_avg_loss | -17.6681 |
| avg_hold_time_bars | 2.6130 |
| exposure | 0.1387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
