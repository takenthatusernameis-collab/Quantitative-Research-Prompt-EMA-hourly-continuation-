# EMA Hourly Continuation — ZK/USDT P8_50

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1098 |
| net_profit_factor | 0.6822 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9973 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -5.4249 |
| sortino_ratio | -2.6327 |
| max_drawdown | 0.9489 |
| cagr | -0.7108 |
| net_avg_win | 39.0899 |
| net_avg_loss | -51.3647 |
| avg_hold_time_bars | 8.2814 |
| exposure | 0.4433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
