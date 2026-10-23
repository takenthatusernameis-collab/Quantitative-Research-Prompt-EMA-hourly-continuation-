# EMA Hourly Continuation — ORCA/USDT P34_50

**Symbol:** ORCA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 796 |
| net_profit_factor | 0.4348 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.9204 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -7.9574 |
| sortino_ratio | -3.1832 |
| max_drawdown | 0.9829 |
| cagr | -0.7970 |
| net_avg_win | 22.0862 |
| net_avg_loss | -38.2625 |
| avg_hold_time_bars | 3.7688 |
| exposure | 0.1364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
