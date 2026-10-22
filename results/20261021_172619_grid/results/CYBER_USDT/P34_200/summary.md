# EMA Hourly Continuation — CYBER/USDT P34_200

**Symbol:** CYBER/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.9046 |
| net_win_rate | 0.5219 |
| gross_profit_factor | 1.0828 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -0.4934 |
| sortino_ratio | -0.1224 |
| max_drawdown | 0.2176 |
| cagr | -0.0579 |
| net_avg_win | 85.1377 |
| net_avg_loss | -102.7347 |
| avg_hold_time_bars | 37.5455 |
| exposure | 0.5069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
