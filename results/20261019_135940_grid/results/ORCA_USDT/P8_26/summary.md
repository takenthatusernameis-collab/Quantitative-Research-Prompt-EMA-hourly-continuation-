# EMA Hourly Continuation — ORCA/USDT P8_26

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1378 |
| net_profit_factor | 0.6059 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 1.0202 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -7.1493 |
| sortino_ratio | -3.7282 |
| max_drawdown | 0.9904 |
| cagr | -0.8380 |
| net_avg_win | 23.2970 |
| net_avg_loss | -34.6339 |
| avg_hold_time_bars | 4.7837 |
| exposure | 0.2996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
