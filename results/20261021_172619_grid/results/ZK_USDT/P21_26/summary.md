# EMA Hourly Continuation — ZK/USDT P21_26

**Symbol:** ZK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 197 |
| net_profit_factor | 0.6176 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8465 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -2.2383 |
| sortino_ratio | -0.4642 |
| max_drawdown | 0.4699 |
| cagr | -0.1921 |
| net_avg_win | 70.5412 |
| net_avg_loss | -96.0705 |
| avg_hold_time_bars | 4.5076 |
| exposure | 0.0433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
