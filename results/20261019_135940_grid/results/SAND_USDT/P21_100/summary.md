# EMA Hourly Continuation — SAND/USDT P21_100

**Symbol:** SAND/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.5307 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.8549 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -5.1612 |
| sortino_ratio | -1.8114 |
| max_drawdown | 0.8978 |
| cagr | -0.5857 |
| net_avg_win | 36.2250 |
| net_avg_loss | -54.0639 |
| avg_hold_time_bars | 14.2734 |
| exposure | 0.4081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
