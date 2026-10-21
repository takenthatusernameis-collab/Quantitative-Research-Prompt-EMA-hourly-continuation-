# EMA Hourly Continuation — RSR/USDT P26_50

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8030 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0533 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.3296 |
| sortino_ratio | -0.3790 |
| max_drawdown | 0.3743 |
| cagr | -0.1604 |
| net_avg_win | 71.7170 |
| net_avg_loss | -94.4516 |
| avg_hold_time_bars | 6.1272 |
| exposure | 0.1095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
