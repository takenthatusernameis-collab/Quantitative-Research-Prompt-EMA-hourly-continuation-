# EMA Hourly Continuation — SHIB/USDT P8_200

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8703 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0582 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -0.7293 |
| sortino_ratio | -0.1796 |
| max_drawdown | 0.2545 |
| cagr | -0.0812 |
| net_avg_win | 85.1995 |
| net_avg_loss | -103.3707 |
| avg_hold_time_bars | 57.6565 |
| exposure | 0.7705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
