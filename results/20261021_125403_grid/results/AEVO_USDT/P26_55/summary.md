# EMA Hourly Continuation — AEVO/USDT P26_55

**Symbol:** AEVO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6942 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -2.6652 |
| sortino_ratio | -0.8700 |
| max_drawdown | 0.6445 |
| cagr | -0.3288 |
| net_avg_win | 57.1279 |
| net_avg_loss | -76.2443 |
| avg_hold_time_bars | 6.7557 |
| exposure | 0.1602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
