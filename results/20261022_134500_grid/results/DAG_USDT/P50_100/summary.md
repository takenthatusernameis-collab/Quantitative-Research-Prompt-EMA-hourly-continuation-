# EMA Hourly Continuation — DAG/USDT P50_100

**Symbol:** DAG/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.4674 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.7238 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -6.1529 |
| sortino_ratio | -2.2346 |
| max_drawdown | 0.9370 |
| cagr | -0.6674 |
| net_avg_win | 28.8567 |
| net_avg_loss | -45.9378 |
| avg_hold_time_bars | 5.1452 |
| exposure | 0.1562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
