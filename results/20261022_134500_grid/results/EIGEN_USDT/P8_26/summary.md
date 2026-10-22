# EMA Hourly Continuation — EIGEN/USDT P8_26

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1263 |
| net_profit_factor | 0.5579 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -7.8357 |
| sortino_ratio | -4.3202 |
| max_drawdown | 0.9878 |
| cagr | -0.8775 |
| net_avg_win | 21.6476 |
| net_avg_loss | -32.4311 |
| avg_hold_time_bars | 3.6738 |
| exposure | 0.2582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
