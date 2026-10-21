# EMA Hourly Continuation — 1INCH/USDT P50_55

**Symbol:** 1INCH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 135 |
| net_profit_factor | 0.5468 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.8461 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -2.1601 |
| sortino_ratio | -0.3604 |
| max_drawdown | 0.3499 |
| cagr | -0.1525 |
| net_avg_win | 66.1542 |
| net_avg_loss | -102.7602 |
| avg_hold_time_bars | 4.2519 |
| exposure | 0.0261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
