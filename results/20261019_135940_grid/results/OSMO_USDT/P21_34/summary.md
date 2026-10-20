# EMA Hourly Continuation — OSMO/USDT P21_34

**Symbol:** OSMO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1152 |
| net_profit_factor | 0.3441 |
| net_win_rate | 0.3785 |
| gross_profit_factor | 0.9110 |
| gross_win_rate | 0.4045 |
| sharpe_ratio | -12.6627 |
| sortino_ratio | -6.1667 |
| max_drawdown | 0.9996 |
| cagr | -0.9570 |
| net_avg_win | 12.0308 |
| net_avg_loss | -21.2873 |
| avg_hold_time_bars | 2.9418 |
| exposure | 0.1540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
