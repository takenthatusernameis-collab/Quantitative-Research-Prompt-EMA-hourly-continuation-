# EMA Hourly Continuation — EIGEN/USDT P89_100

**Symbol:** EIGEN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.4039 |
| net_win_rate | 0.4144 |
| gross_profit_factor | 0.8553 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -7.9798 |
| sortino_ratio | -2.8848 |
| max_drawdown | 0.9527 |
| cagr | -0.7739 |
| net_avg_win | 29.6113 |
| net_avg_loss | -51.8882 |
| avg_hold_time_bars | 1.8099 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
