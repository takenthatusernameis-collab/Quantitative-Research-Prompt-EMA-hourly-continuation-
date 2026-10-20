# EMA Hourly Continuation — TAIKO/USDT P26_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.5320 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.9355 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -6.6411 |
| sortino_ratio | -2.7167 |
| max_drawdown | 0.9608 |
| cagr | -0.7408 |
| net_avg_win | 29.1611 |
| net_avg_loss | -48.0141 |
| avg_hold_time_bars | 4.8527 |
| exposure | 0.1867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
