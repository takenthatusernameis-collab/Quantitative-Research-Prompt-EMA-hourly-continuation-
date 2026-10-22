# EMA Hourly Continuation — ZRO/USDT P55_200

**Symbol:** ZRO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.7722 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0356 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -1.6349 |
| sortino_ratio | -0.4675 |
| max_drawdown | 0.4366 |
| cagr | -0.1992 |
| net_avg_win | 71.7610 |
| net_avg_loss | -94.9205 |
| avg_hold_time_bars | 17.3148 |
| exposure | 0.3203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
