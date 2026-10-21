# EMA Hourly Continuation — ASTR/USDT P50_200

**Symbol:** ASTR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7833 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 1.0037 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -1.2941 |
| sortino_ratio | -0.3117 |
| max_drawdown | 0.3528 |
| cagr | -0.1346 |
| net_avg_win | 77.2078 |
| net_avg_loss | -99.2648 |
| avg_hold_time_bars | 33.4807 |
| exposure | 0.4318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
