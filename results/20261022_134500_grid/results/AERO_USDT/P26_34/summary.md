# EMA Hourly Continuation — AERO/USDT P26_34

**Symbol:** AERO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.1996 |
| net_win_rate | 0.3826 |
| gross_profit_factor | 0.4513 |
| gross_win_rate | 0.4064 |
| sharpe_ratio | -11.3506 |
| sortino_ratio | -5.0824 |
| max_drawdown | 0.9986 |
| cagr | -0.9266 |
| net_avg_win | 6.7288 |
| net_avg_loss | -20.8970 |
| avg_hold_time_bars | 2.0683 |
| exposure | 0.0909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
