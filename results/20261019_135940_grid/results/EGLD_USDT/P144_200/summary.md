# EMA Hourly Continuation — EGLD/USDT P144_200

**Symbol:** EGLD/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.4553 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.8763 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -3.8974 |
| sortino_ratio | -1.0772 |
| max_drawdown | 0.7331 |
| cagr | -0.4068 |
| net_avg_win | 33.5480 |
| net_avg_loss | -67.0557 |
| avg_hold_time_bars | 4.3429 |
| exposure | 0.0754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
