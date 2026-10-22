# EMA Hourly Continuation — MAGIC/USDT P50_89

**Symbol:** MAGIC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7320 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 1.0197 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -2.2124 |
| sortino_ratio | -0.6415 |
| max_drawdown | 0.5371 |
| cagr | -0.2552 |
| net_avg_win | 70.3711 |
| net_avg_loss | -94.7308 |
| avg_hold_time_bars | 7.0465 |
| exposure | 0.1310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
