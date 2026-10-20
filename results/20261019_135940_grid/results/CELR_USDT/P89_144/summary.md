# EMA Hourly Continuation — CELR/USDT P89_144

**Symbol:** CELR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.5213 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8489 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -4.5472 |
| sortino_ratio | -1.4405 |
| max_drawdown | 0.8253 |
| cagr | -0.4939 |
| net_avg_win | 39.5407 |
| net_avg_loss | -63.0224 |
| avg_hold_time_bars | 5.5482 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
