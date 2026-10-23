# EMA Hourly Continuation — DYDX/USDT P100_200

**Symbol:** DYDX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.5534 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -3.5607 |
| sortino_ratio | -0.9946 |
| max_drawdown | 0.7081 |
| cagr | -0.3825 |
| net_avg_win | 47.7945 |
| net_avg_loss | -73.1073 |
| avg_hold_time_bars | 9.5063 |
| exposure | 0.1715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
