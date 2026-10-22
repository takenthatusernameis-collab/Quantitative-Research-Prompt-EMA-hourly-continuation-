# EMA Hourly Continuation — NEAR/USDT P26_200

**Symbol:** NEAR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.9219 |
| net_win_rate | 0.5358 |
| gross_profit_factor | 1.1681 |
| gross_win_rate | 0.5389 |
| sharpe_ratio | -0.4228 |
| sortino_ratio | -0.1086 |
| max_drawdown | 0.2881 |
| cagr | -0.0533 |
| net_avg_win | 88.2279 |
| net_avg_loss | -110.4720 |
| avg_hold_time_bars | 41.3614 |
| exposure | 0.6035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
