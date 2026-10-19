# EMA Hourly Continuation — SAND/USDT P12_100

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.5370 |
| net_win_rate | 0.4363 |
| gross_profit_factor | 0.8469 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -5.1771 |
| sortino_ratio | -1.7849 |
| max_drawdown | 0.8918 |
| cagr | -0.5848 |
| net_avg_win | 38.6544 |
| net_avg_loss | -55.7125 |
| avg_hold_time_bars | 20.7059 |
| exposure | 0.5760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
