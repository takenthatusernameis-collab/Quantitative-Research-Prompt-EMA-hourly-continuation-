# EMA Hourly Continuation — CATI/USDT P34_100

**Symbol:** CATI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.5648 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.9117 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -5.2029 |
| sortino_ratio | -1.9553 |
| max_drawdown | 0.8677 |
| cagr | -0.6114 |
| net_avg_win | 40.8889 |
| net_avg_loss | -61.7669 |
| avg_hold_time_bars | 9.4115 |
| exposure | 0.3059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
