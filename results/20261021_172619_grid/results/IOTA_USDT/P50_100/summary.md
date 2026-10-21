# EMA Hourly Continuation — IOTA/USDT P50_100

**Symbol:** IOTA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8019 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -2.9070 |
| sortino_ratio | -0.8165 |
| max_drawdown | 0.6446 |
| cagr | -0.3129 |
| net_avg_win | 52.1277 |
| net_avg_loss | -72.3098 |
| avg_hold_time_bars | 8.5476 |
| exposure | 0.1511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
