# EMA Hourly Continuation — RSR/USDT P26_55

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.4938 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -6.7842 |
| sortino_ratio | -2.8292 |
| max_drawdown | 0.9712 |
| cagr | -0.7559 |
| net_avg_win | 23.8602 |
| net_avg_loss | -38.9893 |
| avg_hold_time_bars | 4.2396 |
| exposure | 0.1713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
