# EMA Hourly Continuation — EGLD/USDT P21_200

**Symbol:** EGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.8554 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0512 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -0.7855 |
| sortino_ratio | -0.1971 |
| max_drawdown | 0.2833 |
| cagr | -0.0888 |
| net_avg_win | 78.5297 |
| net_avg_loss | -97.3838 |
| avg_hold_time_bars | 45.6131 |
| exposure | 0.6324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
