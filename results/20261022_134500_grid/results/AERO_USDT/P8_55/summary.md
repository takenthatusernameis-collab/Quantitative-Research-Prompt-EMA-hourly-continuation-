# EMA Hourly Continuation — AERO/USDT P8_55

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 996 |
| net_profit_factor | 0.6358 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -4.7451 |
| sortino_ratio | -2.1096 |
| max_drawdown | 0.9222 |
| cagr | -0.6348 |
| net_avg_win | 34.1137 |
| net_avg_loss | -48.1347 |
| avg_hold_time_bars | 10.6215 |
| exposure | 0.4809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
