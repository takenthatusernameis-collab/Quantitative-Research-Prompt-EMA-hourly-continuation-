# EMA Hourly Continuation — NEAR/USDT P34_55

**Symbol:** NEAR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7088 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9395 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.7281 |
| sortino_ratio | -0.4073 |
| max_drawdown | 0.3861 |
| cagr | -0.1707 |
| net_avg_win | 69.1520 |
| net_avg_loss | -92.6491 |
| avg_hold_time_bars | 5.9262 |
| exposure | 0.0730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
