# EMA Hourly Continuation — EIGEN/USDT P12_50

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.8040 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.7142 |
| sortino_ratio | -0.6029 |
| max_drawdown | 0.4525 |
| cagr | -0.2440 |
| net_avg_win | 73.7121 |
| net_avg_loss | -88.4033 |
| avg_hold_time_bars | 11.1374 |
| exposure | 0.3068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
