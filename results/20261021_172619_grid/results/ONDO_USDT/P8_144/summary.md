# EMA Hourly Continuation — ONDO/USDT P8_144

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.9245 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0718 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -0.4607 |
| sortino_ratio | -0.1340 |
| max_drawdown | 0.3282 |
| cagr | -0.0646 |
| net_avg_win | 89.2124 |
| net_avg_loss | -103.8439 |
| avg_hold_time_bars | 36.0244 |
| exposure | 0.6697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
