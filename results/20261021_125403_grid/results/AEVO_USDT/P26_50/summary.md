# EMA Hourly Continuation — AEVO/USDT P26_50

**Symbol:** AEVO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6411 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -3.1065 |
| sortino_ratio | -0.9987 |
| max_drawdown | 0.6959 |
| cagr | -0.3669 |
| net_avg_win | 51.3552 |
| net_avg_loss | -70.0941 |
| avg_hold_time_bars | 6.1529 |
| exposure | 0.1420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
