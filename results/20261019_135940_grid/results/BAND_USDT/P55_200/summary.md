# EMA Hourly Continuation — BAND/USDT P55_200

**Symbol:** BAND/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6062 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8458 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -2.8686 |
| sortino_ratio | -0.7713 |
| max_drawdown | 0.6086 |
| cagr | -0.3017 |
| net_avg_win | 54.9149 |
| net_avg_loss | -77.1907 |
| avg_hold_time_bars | 22.0083 |
| exposure | 0.3615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
