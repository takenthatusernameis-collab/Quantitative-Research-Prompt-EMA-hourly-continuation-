# EMA Hourly Continuation — CKB/USDT P144_200

**Symbol:** CKB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.7599 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.0875 |
| gross_win_rate | 0.5256 |
| sharpe_ratio | -1.1873 |
| sortino_ratio | -0.2510 |
| max_drawdown | 0.2590 |
| cagr | -0.1086 |
| net_avg_win | 70.2615 |
| net_avg_loss | -102.4298 |
| avg_hold_time_bars | 6.7349 |
| exposure | 0.0658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
