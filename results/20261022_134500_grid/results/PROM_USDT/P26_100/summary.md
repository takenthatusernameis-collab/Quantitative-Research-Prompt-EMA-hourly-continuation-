# EMA Hourly Continuation — PROM/USDT P26_100

**Symbol:** PROM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.4833 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.8463 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -6.3292 |
| sortino_ratio | -2.3177 |
| max_drawdown | 0.9473 |
| cagr | -0.6838 |
| net_avg_win | 30.2503 |
| net_avg_loss | -45.8101 |
| avg_hold_time_bars | 11.1534 |
| exposure | 0.3503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
