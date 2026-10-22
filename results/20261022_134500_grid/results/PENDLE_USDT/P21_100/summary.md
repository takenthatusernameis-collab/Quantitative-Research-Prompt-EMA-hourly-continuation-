# EMA Hourly Continuation — PENDLE/USDT P21_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.6269 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -3.7985 |
| sortino_ratio | -1.3362 |
| max_drawdown | 0.8062 |
| cagr | -0.4713 |
| net_avg_win | 45.6167 |
| net_avg_loss | -64.0517 |
| avg_hold_time_bars | 16.1290 |
| exposure | 0.4604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
