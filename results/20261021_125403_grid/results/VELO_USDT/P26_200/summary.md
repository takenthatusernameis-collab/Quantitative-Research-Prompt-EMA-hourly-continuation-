# EMA Hourly Continuation — VELO/USDT P26_200

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.9249 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0558 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -0.3882 |
| sortino_ratio | -0.1012 |
| max_drawdown | 0.2616 |
| cagr | -0.0497 |
| net_avg_win | 87.1287 |
| net_avg_loss | -100.7207 |
| avg_hold_time_bars | 36.3161 |
| exposure | 0.5431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
