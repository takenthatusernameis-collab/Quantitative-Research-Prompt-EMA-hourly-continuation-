# EMA Hourly Continuation — OSMO/USDT P8_12

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6754 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 1.0691 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -3.1492 |
| sortino_ratio | -0.9095 |
| max_drawdown | 0.7217 |
| cagr | -0.3397 |
| net_avg_win | 68.7181 |
| net_avg_loss | -96.3408 |
| avg_hold_time_bars | 4.7692 |
| exposure | 0.0874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
