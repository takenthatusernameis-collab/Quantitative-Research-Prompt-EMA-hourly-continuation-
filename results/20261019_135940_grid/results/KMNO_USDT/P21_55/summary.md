# EMA Hourly Continuation — KMNO/USDT P21_55

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.5287 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8769 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -6.0335 |
| sortino_ratio | -2.4261 |
| max_drawdown | 0.9480 |
| cagr | -0.6962 |
| net_avg_win | 29.0449 |
| net_avg_loss | -45.2812 |
| avg_hold_time_bars | 5.8605 |
| exposure | 0.2192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
