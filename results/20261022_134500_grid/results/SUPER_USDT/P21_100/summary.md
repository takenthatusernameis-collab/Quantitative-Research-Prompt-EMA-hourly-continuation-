# EMA Hourly Continuation — SUPER/USDT P21_100

**Symbol:** SUPER/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.6948 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -2.7620 |
| sortino_ratio | -1.0099 |
| max_drawdown | 0.7178 |
| cagr | -0.3804 |
| net_avg_win | 47.1016 |
| net_avg_loss | -69.0213 |
| avg_hold_time_bars | 13.3836 |
| exposure | 0.4076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
