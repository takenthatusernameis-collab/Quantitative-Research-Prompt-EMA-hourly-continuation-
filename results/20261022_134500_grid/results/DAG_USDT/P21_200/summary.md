# EMA Hourly Continuation — DAG/USDT P21_200

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6438 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8695 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.7560 |
| sortino_ratio | -0.8268 |
| max_drawdown | 0.6534 |
| cagr | -0.3272 |
| net_avg_win | 53.2528 |
| net_avg_loss | -72.8399 |
| avg_hold_time_bars | 27.2582 |
| exposure | 0.5662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
