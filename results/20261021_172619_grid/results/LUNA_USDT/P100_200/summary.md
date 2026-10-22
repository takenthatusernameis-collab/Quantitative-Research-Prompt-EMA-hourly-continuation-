# EMA Hourly Continuation — LUNA/USDT P100_200

**Symbol:** LUNA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6352 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8310 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -2.1832 |
| sortino_ratio | -0.5081 |
| max_drawdown | 0.4528 |
| cagr | -0.2084 |
| net_avg_win | 62.8579 |
| net_avg_loss | -84.5202 |
| avg_hold_time_bars | 14.1086 |
| exposure | 0.1712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
