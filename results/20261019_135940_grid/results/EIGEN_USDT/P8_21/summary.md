# EMA Hourly Continuation — EIGEN/USDT P8_21

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1364 |
| net_profit_factor | 0.5145 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8349 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -9.8642 |
| sortino_ratio | -5.6559 |
| max_drawdown | 0.9969 |
| cagr | -0.9389 |
| net_avg_win | 17.6052 |
| net_avg_loss | -26.8727 |
| avg_hold_time_bars | 2.7471 |
| exposure | 0.2085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
