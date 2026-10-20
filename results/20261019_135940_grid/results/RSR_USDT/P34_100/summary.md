# EMA Hourly Continuation — RSR/USDT P34_100

**Symbol:** RSR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.6594 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9519 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -3.5893 |
| sortino_ratio | -1.2571 |
| max_drawdown | 0.7857 |
| cagr | -0.4513 |
| net_avg_win | 51.2729 |
| net_avg_loss | -70.3370 |
| avg_hold_time_bars | 9.5880 |
| exposure | 0.2698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
