# EMA Hourly Continuation — COMP/USDT P8_20

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.5464 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8206 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -5.0396 |
| sortino_ratio | -1.9129 |
| max_drawdown | 0.8927 |
| cagr | -0.5858 |
| net_avg_win | 33.7408 |
| net_avg_loss | -51.2695 |
| avg_hold_time_bars | 4.8302 |
| exposure | 0.1539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
