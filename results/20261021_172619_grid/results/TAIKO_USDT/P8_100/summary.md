# EMA Hourly Continuation — TAIKO/USDT P8_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.8351 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0217 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.2162 |
| sortino_ratio | -0.3880 |
| max_drawdown | 0.4497 |
| cagr | -0.1655 |
| net_avg_win | 74.3723 |
| net_avg_loss | -92.1506 |
| avg_hold_time_bars | 29.5000 |
| exposure | 0.6632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
