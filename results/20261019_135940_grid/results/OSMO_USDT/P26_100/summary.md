# EMA Hourly Continuation — OSMO/USDT P26_100

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.6354 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 1.0284 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -4.1046 |
| sortino_ratio | -1.4538 |
| max_drawdown | 0.8324 |
| cagr | -0.5047 |
| net_avg_win | 48.1418 |
| net_avg_loss | -67.0497 |
| avg_hold_time_bars | 12.5321 |
| exposure | 0.3640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
