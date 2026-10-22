# EMA Hourly Continuation — LUNA/USDT P21_100

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7499 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9497 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -2.0648 |
| sortino_ratio | -0.6126 |
| max_drawdown | 0.5218 |
| cagr | -0.2459 |
| net_avg_win | 73.2060 |
| net_avg_loss | -90.6432 |
| avg_hold_time_bars | 17.2176 |
| exposure | 0.3381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
