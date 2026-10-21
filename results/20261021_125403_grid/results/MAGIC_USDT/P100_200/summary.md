# EMA Hourly Continuation — MAGIC/USDT P100_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.6383 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.8219 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -2.2957 |
| sortino_ratio | -0.5433 |
| max_drawdown | 0.4846 |
| cagr | -0.2216 |
| net_avg_win | 65.3965 |
| net_avg_loss | -85.4965 |
| avg_hold_time_bars | 13.7184 |
| exposure | 0.1727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
