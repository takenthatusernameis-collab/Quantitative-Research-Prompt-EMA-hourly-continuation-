# EMA Hourly Continuation — FLOW/USDT P8_12

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6325 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.4556 |
| sortino_ratio | -0.6138 |
| max_drawdown | 0.5170 |
| cagr | -0.2440 |
| net_avg_win | 59.0950 |
| net_avg_loss | -88.6036 |
| avg_hold_time_bars | 4.2318 |
| exposure | 0.0581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
