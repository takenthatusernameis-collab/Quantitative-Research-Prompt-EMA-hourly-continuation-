# EMA Hourly Continuation — EIGEN/USDT P50_100

**Symbol:** EIGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.9381 |
| net_win_rate | 0.5336 |
| gross_profit_factor | 1.1343 |
| gross_win_rate | 0.5336 |
| sharpe_ratio | -0.3121 |
| sortino_ratio | -0.0817 |
| max_drawdown | 0.1653 |
| cagr | -0.0414 |
| net_avg_win | 88.1263 |
| net_avg_loss | -107.4638 |
| avg_hold_time_bars | 10.2836 |
| exposure | 0.1534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
