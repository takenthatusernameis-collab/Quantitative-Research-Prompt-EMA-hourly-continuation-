# EMA Hourly Continuation — SATS/USDT P21_50

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 885 |
| net_profit_factor | 0.5454 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -6.3039 |
| sortino_ratio | -2.6356 |
| max_drawdown | 0.9602 |
| cagr | -0.7179 |
| net_avg_win | 29.5791 |
| net_avg_loss | -42.5311 |
| avg_hold_time_bars | 5.1288 |
| exposure | 0.2054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
