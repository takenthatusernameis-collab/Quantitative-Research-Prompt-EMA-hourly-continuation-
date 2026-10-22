# EMA Hourly Continuation — OSMO/USDT P26_34

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.4960 |
| net_win_rate | 0.3987 |
| gross_profit_factor | 0.7749 |
| gross_win_rate | 0.3987 |
| sharpe_ratio | -4.5004 |
| sortino_ratio | -1.1270 |
| max_drawdown | 0.7395 |
| cagr | -0.4069 |
| net_avg_win | 58.9360 |
| net_avg_loss | -78.7870 |
| avg_hold_time_bars | 4.7549 |
| exposure | 0.0661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
