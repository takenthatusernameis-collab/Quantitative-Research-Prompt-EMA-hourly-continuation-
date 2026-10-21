# EMA Hourly Continuation — NEAR/USDT P34_100

**Symbol:** NEAR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7214 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8860 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -1.9583 |
| sortino_ratio | -0.5458 |
| max_drawdown | 0.5051 |
| cagr | -0.2222 |
| net_avg_win | 66.9415 |
| net_avg_loss | -83.1463 |
| avg_hold_time_bars | 13.7807 |
| exposure | 0.2399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
