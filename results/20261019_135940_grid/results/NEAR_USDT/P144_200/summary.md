# EMA Hourly Continuation — NEAR/USDT P144_200

**Symbol:** NEAR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6241 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 1.0319 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -2.9114 |
| sortino_ratio | -0.8126 |
| max_drawdown | 0.6382 |
| cagr | -0.3181 |
| net_avg_win | 53.4104 |
| net_avg_loss | -85.1391 |
| avg_hold_time_bars | 4.3429 |
| exposure | 0.0760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
