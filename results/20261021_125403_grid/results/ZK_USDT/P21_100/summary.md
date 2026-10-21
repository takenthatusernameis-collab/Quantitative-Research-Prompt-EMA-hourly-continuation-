# EMA Hourly Continuation — ZK/USDT P21_100

**Symbol:** ZK/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.8309 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0111 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.4118 |
| sortino_ratio | -0.4604 |
| max_drawdown | 0.4537 |
| cagr | -0.1928 |
| net_avg_win | 80.0832 |
| net_avg_loss | -96.3812 |
| avg_hold_time_bars | 16.7955 |
| exposure | 0.3963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
