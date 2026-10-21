# EMA Hourly Continuation — DASH/USDT P21_200

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.7148 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.8838 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -1.7298 |
| sortino_ratio | -0.4140 |
| max_drawdown | 0.4105 |
| cagr | -0.1743 |
| net_avg_win | 71.4127 |
| net_avg_loss | -89.2453 |
| avg_hold_time_bars | 46.4894 |
| exposure | 0.6001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
