# EMA Hourly Continuation — FLIP/USDT P26_100

**Symbol:** FLIP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.5046 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.8230 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -4.7571 |
| sortino_ratio | -1.4372 |
| max_drawdown | 0.8286 |
| cagr | -0.4983 |
| net_avg_win | 42.5560 |
| net_avg_loss | -63.4154 |
| avg_hold_time_bars | 17.4139 |
| exposure | 0.3633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
