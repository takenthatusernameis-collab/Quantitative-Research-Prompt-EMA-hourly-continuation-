# EMA Hourly Continuation — DASH/USDT P50_100

**Symbol:** DASH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6737 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9155 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -2.2471 |
| sortino_ratio | -0.5901 |
| max_drawdown | 0.5109 |
| cagr | -0.2370 |
| net_avg_win | 63.2286 |
| net_avg_loss | -85.3696 |
| avg_hold_time_bars | 9.0592 |
| exposure | 0.1392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
