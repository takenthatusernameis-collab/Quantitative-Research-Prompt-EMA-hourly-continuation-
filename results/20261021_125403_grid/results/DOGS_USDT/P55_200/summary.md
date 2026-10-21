# EMA Hourly Continuation — DOGS/USDT P55_200

**Symbol:** DOGS/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.8200 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9744 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -1.0950 |
| sortino_ratio | -0.2642 |
| max_drawdown | 0.3068 |
| cagr | -0.1156 |
| net_avg_win | 88.1802 |
| net_avg_loss | -104.0658 |
| avg_hold_time_bars | 27.9959 |
| exposure | 0.3624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
