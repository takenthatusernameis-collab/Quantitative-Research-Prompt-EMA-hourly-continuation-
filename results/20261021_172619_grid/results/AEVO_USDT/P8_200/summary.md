# EMA Hourly Continuation — AEVO/USDT P8_200

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 0.8884 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0269 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -0.5104 |
| sortino_ratio | -0.1065 |
| max_drawdown | 0.2087 |
| cagr | -0.0500 |
| net_avg_win | 89.4694 |
| net_avg_loss | -103.5802 |
| avg_hold_time_bars | 88.5962 |
| exposure | 0.8539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
