# EMA Hourly Continuation — DAG/USDT P21_50

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.7924 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0048 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -1.3156 |
| sortino_ratio | -0.3594 |
| max_drawdown | 0.3702 |
| cagr | -0.1532 |
| net_avg_win | 70.8106 |
| net_avg_loss | -91.8557 |
| avg_hold_time_bars | 7.7328 |
| exposure | 0.1276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
