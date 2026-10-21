# EMA Hourly Continuation — OSMO/USDT P8_100

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.8509 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.0589 |
| gross_win_rate | 0.5141 |
| sharpe_ratio | -1.1601 |
| sortino_ratio | -0.3708 |
| max_drawdown | 0.4645 |
| cagr | -0.1597 |
| net_avg_win | 79.2616 |
| net_avg_loss | -98.5573 |
| avg_hold_time_bars | 29.6552 |
| exposure | 0.6686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
