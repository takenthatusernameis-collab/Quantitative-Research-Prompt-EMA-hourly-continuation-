# EMA Hourly Continuation — VELO/USDT P21_50

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.5360 |
| net_win_rate | 0.4546 |
| gross_profit_factor | 0.8231 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -6.3734 |
| sortino_ratio | -2.9181 |
| max_drawdown | 0.9719 |
| cagr | -0.7537 |
| net_avg_win | 23.3045 |
| net_avg_loss | -36.2445 |
| avg_hold_time_bars | 4.1389 |
| exposure | 0.1990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
