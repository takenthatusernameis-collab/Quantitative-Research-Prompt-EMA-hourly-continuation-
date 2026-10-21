# EMA Hourly Continuation — CETUS/USDT P21_55

**Symbol:** CETUS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7323 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -2.5245 |
| sortino_ratio | -0.8292 |
| max_drawdown | 0.6311 |
| cagr | -0.3173 |
| net_avg_win | 66.5784 |
| net_avg_loss | -82.7686 |
| avg_hold_time_bars | 7.9625 |
| exposure | 0.1921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
