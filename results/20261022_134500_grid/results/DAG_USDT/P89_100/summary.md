# EMA Hourly Continuation — DAG/USDT P89_100

**Symbol:** DAG/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.2150 |
| net_win_rate | 0.3328 |
| gross_profit_factor | 0.5162 |
| gross_win_rate | 0.3577 |
| sharpe_ratio | -10.7957 |
| sortino_ratio | -3.9754 |
| max_drawdown | 0.9960 |
| cagr | -0.8888 |
| net_avg_win | 12.7483 |
| net_avg_loss | -29.5756 |
| avg_hold_time_bars | 1.9549 |
| exposure | 0.0571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
