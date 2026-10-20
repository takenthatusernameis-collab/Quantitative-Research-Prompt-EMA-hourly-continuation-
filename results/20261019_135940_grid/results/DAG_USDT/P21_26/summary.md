# EMA Hourly Continuation — DAG/USDT P21_26

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1189 |
| net_profit_factor | 0.2415 |
| net_win_rate | 0.2969 |
| gross_profit_factor | 0.6344 |
| gross_win_rate | 0.3272 |
| sharpe_ratio | -16.5523 |
| sortino_ratio | -8.3707 |
| max_drawdown | 1.0000 |
| cagr | -0.9907 |
| net_avg_win | 9.0195 |
| net_avg_loss | -15.7701 |
| avg_hold_time_bars | 1.8116 |
| exposure | 0.0979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
