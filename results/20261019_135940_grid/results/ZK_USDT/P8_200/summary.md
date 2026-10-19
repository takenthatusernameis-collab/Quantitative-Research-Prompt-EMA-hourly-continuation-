# EMA Hourly Continuation — ZK/USDT P8_200

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7692 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9971 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.5328 |
| sortino_ratio | -0.4379 |
| max_drawdown | 0.4170 |
| cagr | -0.1849 |
| net_avg_win | 67.7873 |
| net_avg_loss | -87.6594 |
| avg_hold_time_bars | 43.5733 |
| exposure | 0.7966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
