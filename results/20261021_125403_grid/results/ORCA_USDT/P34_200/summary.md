# EMA Hourly Continuation — ORCA/USDT P34_200

**Symbol:** ORCA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.7926 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9831 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.2580 |
| sortino_ratio | -0.3145 |
| max_drawdown | 0.3567 |
| cagr | -0.1366 |
| net_avg_win | 76.5333 |
| net_avg_loss | -96.5642 |
| avg_hold_time_bars | 35.6623 |
| exposure | 0.4993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
