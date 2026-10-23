# EMA Hourly Continuation — DAG/USDT P8_200

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.6092 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8273 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -3.4391 |
| sortino_ratio | -1.1341 |
| max_drawdown | 0.7516 |
| cagr | -0.4140 |
| net_avg_win | 46.4391 |
| net_avg_loss | -63.0141 |
| avg_hold_time_bars | 28.9526 |
| exposure | 0.7212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
