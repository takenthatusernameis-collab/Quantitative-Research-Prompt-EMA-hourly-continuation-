# EMA Hourly Continuation — ORCA/USDT P55_89

**Symbol:** ORCA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.6632 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -2.2385 |
| sortino_ratio | -0.6104 |
| max_drawdown | 0.5307 |
| cagr | -0.2433 |
| net_avg_win | 55.3874 |
| net_avg_loss | -81.6912 |
| avg_hold_time_bars | 7.1657 |
| exposure | 0.1179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
