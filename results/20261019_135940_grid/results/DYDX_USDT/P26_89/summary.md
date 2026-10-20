# EMA Hourly Continuation — DYDX/USDT P26_89

**Symbol:** DYDX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.6646 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -3.6609 |
| sortino_ratio | -1.3469 |
| max_drawdown | 0.8074 |
| cagr | -0.4696 |
| net_avg_win | 47.9753 |
| net_avg_loss | -67.8574 |
| avg_hold_time_bars | 10.9602 |
| exposure | 0.3383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
