# EMA Hourly Continuation — BOME/USDT P8_100

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.8763 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0224 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -0.8132 |
| sortino_ratio | -0.2620 |
| max_drawdown | 0.3691 |
| cagr | -0.1180 |
| net_avg_win | 74.2477 |
| net_avg_loss | -88.5045 |
| avg_hold_time_bars | 27.0812 |
| exposure | 0.6216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
