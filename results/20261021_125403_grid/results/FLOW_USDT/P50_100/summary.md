# EMA Hourly Continuation — FLOW/USDT P50_100

**Symbol:** FLOW/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6898 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.2600 |
| sortino_ratio | -0.6329 |
| max_drawdown | 0.5303 |
| cagr | -0.2521 |
| net_avg_win | 62.2488 |
| net_avg_loss | -84.3153 |
| avg_hold_time_bars | 7.7467 |
| exposure | 0.1349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
