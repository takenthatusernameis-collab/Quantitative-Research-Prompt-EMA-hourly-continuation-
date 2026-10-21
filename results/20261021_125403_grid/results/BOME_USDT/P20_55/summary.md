# EMA Hourly Continuation — BOME/USDT P20_55

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.7986 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.4477 |
| sortino_ratio | -0.4636 |
| max_drawdown | 0.4844 |
| cagr | -0.1935 |
| net_avg_win | 65.9198 |
| net_avg_loss | -83.5441 |
| avg_hold_time_bars | 8.7695 |
| exposure | 0.1989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
