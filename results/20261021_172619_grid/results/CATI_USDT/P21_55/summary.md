# EMA Hourly Continuation — CATI/USDT P21_55

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6126 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.7881 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -3.6394 |
| sortino_ratio | -1.1444 |
| max_drawdown | 0.6815 |
| cagr | -0.4126 |
| net_avg_win | 59.1531 |
| net_avg_loss | -75.1551 |
| avg_hold_time_bars | 9.7311 |
| exposure | 0.2182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
