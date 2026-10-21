# EMA Hourly Continuation — EIGEN/USDT P50_89

**Symbol:** EIGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8973 |
| net_win_rate | 0.5288 |
| gross_profit_factor | 1.1097 |
| gross_win_rate | 0.5288 |
| sharpe_ratio | -0.5642 |
| sortino_ratio | -0.1502 |
| max_drawdown | 0.1556 |
| cagr | -0.0700 |
| net_avg_win | 82.1587 |
| net_avg_loss | -102.7490 |
| avg_hold_time_bars | 7.4245 |
| exposure | 0.1149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
