# EMA Hourly Continuation — AERO/USDT P144_200

**Symbol:** AERO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.7236 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9222 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.3051 |
| sortino_ratio | -0.2488 |
| max_drawdown | 0.2748 |
| cagr | -0.1079 |
| net_avg_win | 75.9155 |
| net_avg_loss | -98.0660 |
| avg_hold_time_bars | 6.5506 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
