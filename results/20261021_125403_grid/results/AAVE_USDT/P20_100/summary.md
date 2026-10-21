# EMA Hourly Continuation — AAVE/USDT P20_100

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.8372 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0184 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -1.1054 |
| sortino_ratio | -0.3222 |
| max_drawdown | 0.3775 |
| cagr | -0.1396 |
| net_avg_win | 77.4327 |
| net_avg_loss | -94.7516 |
| avg_hold_time_bars | 21.3341 |
| exposure | 0.4005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
