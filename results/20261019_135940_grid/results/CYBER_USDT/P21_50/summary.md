# EMA Hourly Continuation — CYBER/USDT P21_50

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 935 |
| net_profit_factor | 0.5314 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.8972 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -7.2261 |
| sortino_ratio | -3.1215 |
| max_drawdown | 0.9778 |
| cagr | -0.7798 |
| net_avg_win | 27.1039 |
| net_avg_loss | -39.6611 |
| avg_hold_time_bars | 5.7123 |
| exposure | 0.2428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
