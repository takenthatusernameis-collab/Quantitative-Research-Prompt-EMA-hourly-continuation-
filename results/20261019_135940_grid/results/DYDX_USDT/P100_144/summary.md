# EMA Hourly Continuation — DYDX/USDT P100_144

**Symbol:** DYDX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.5501 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9771 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -4.3617 |
| sortino_ratio | -1.4192 |
| max_drawdown | 0.8218 |
| cagr | -0.4926 |
| net_avg_win | 39.8467 |
| net_avg_loss | -66.5979 |
| avg_hold_time_bars | 3.8168 |
| exposure | 0.0909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
