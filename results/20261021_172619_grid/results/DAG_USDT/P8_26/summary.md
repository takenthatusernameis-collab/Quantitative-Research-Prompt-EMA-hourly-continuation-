# EMA Hourly Continuation — DAG/USDT P8_26

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6820 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -2.3827 |
| sortino_ratio | -0.7257 |
| max_drawdown | 0.5953 |
| cagr | -0.2834 |
| net_avg_win | 56.5555 |
| net_avg_loss | -73.3675 |
| avg_hold_time_bars | 7.6441 |
| exposure | 0.1591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
