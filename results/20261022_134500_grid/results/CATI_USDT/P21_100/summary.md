# EMA Hourly Continuation — CATI/USDT P21_100

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.5648 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8510 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -5.3901 |
| sortino_ratio | -2.0609 |
| max_drawdown | 0.8856 |
| cagr | -0.6306 |
| net_avg_win | 41.1151 |
| net_avg_loss | -59.4392 |
| avg_hold_time_bars | 13.0684 |
| exposure | 0.4398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
