# EMA Hourly Continuation — CWEB/USDT P26_50

**Symbol:** CWEB/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.3207 |
| net_win_rate | 0.3080 |
| gross_profit_factor | 0.7025 |
| gross_win_rate | 0.3255 |
| sharpe_ratio | -13.3626 |
| sortino_ratio | -5.6900 |
| max_drawdown | 0.9996 |
| cagr | -0.9573 |
| net_avg_win | 17.9468 |
| net_avg_loss | -24.9008 |
| avg_hold_time_bars | 5.1850 |
| exposure | 0.2013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
