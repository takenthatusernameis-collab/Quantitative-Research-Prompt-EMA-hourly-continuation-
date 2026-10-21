# EMA Hourly Continuation — CGPT/USDT P26_100

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.8478 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0432 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.1739 |
| sortino_ratio | -0.3513 |
| max_drawdown | 0.3926 |
| cagr | -0.1513 |
| net_avg_win | 85.1068 |
| net_avg_loss | -103.6656 |
| avg_hold_time_bars | 16.4368 |
| exposure | 0.3250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
