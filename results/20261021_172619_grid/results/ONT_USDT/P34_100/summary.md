# EMA Hourly Continuation — ONT/USDT P34_100

**Symbol:** ONT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6445 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8308 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -2.9970 |
| sortino_ratio | -0.9031 |
| max_drawdown | 0.6636 |
| cagr | -0.3396 |
| net_avg_win | 57.6729 |
| net_avg_loss | -73.6070 |
| avg_hold_time_bars | 13.4580 |
| exposure | 0.2753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
