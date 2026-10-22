# EMA Hourly Continuation — CGPT/USDT P21_100

**Symbol:** CGPT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.8513 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0413 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -1.1201 |
| sortino_ratio | -0.3412 |
| max_drawdown | 0.3744 |
| cagr | -0.1476 |
| net_avg_win | 82.2374 |
| net_avg_loss | -100.5403 |
| avg_hold_time_bars | 19.0953 |
| exposure | 0.3915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
