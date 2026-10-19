# EMA Hourly Continuation — JST/USDT P50_100

**Symbol:** JST/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.3321 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 1.0231 |
| gross_win_rate | 0.5209 |
| sharpe_ratio | -6.4056 |
| sortino_ratio | -2.1148 |
| max_drawdown | 0.9356 |
| cagr | -0.6610 |
| net_avg_win | 18.3691 |
| net_avg_loss | -47.2790 |
| avg_hold_time_bars | 7.4117 |
| exposure | 0.1841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
