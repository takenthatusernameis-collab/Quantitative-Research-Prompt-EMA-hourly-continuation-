# EMA Hourly Continuation — SATS/USDT P21_50

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.6516 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8623 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -3.5529 |
| sortino_ratio | -1.1495 |
| max_drawdown | 0.7488 |
| cagr | -0.4138 |
| net_avg_win | 59.1542 |
| net_avg_loss | -73.5034 |
| avg_hold_time_bars | 7.5621 |
| exposure | 0.1790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
