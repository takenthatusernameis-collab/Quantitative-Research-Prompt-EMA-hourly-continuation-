# EMA Hourly Continuation — SAND/USDT P26_55

**Symbol:** SAND/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 831 |
| net_profit_factor | 0.4429 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8636 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -7.4118 |
| sortino_ratio | -3.0109 |
| max_drawdown | 0.9784 |
| cagr | -0.7760 |
| net_avg_win | 21.0441 |
| net_avg_loss | -37.9478 |
| avg_hold_time_bars | 5.2347 |
| exposure | 0.1977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
