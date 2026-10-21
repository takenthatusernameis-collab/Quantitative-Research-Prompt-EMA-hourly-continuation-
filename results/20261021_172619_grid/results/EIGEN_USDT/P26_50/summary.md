# EMA Hourly Continuation — EIGEN/USDT P26_50

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7939 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9914 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.4502 |
| sortino_ratio | -0.4105 |
| max_drawdown | 0.3916 |
| cagr | -0.1730 |
| net_avg_win | 78.1983 |
| net_avg_loss | -97.8805 |
| avg_hold_time_bars | 6.3856 |
| exposure | 0.1133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
