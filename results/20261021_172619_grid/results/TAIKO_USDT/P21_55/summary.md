# EMA Hourly Continuation — TAIKO/USDT P21_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7039 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -2.5342 |
| sortino_ratio | -0.8232 |
| max_drawdown | 0.6463 |
| cagr | -0.3141 |
| net_avg_win | 58.8601 |
| net_avg_loss | -80.5884 |
| avg_hold_time_bars | 8.9487 |
| exposure | 0.2093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
