# EMA Hourly Continuation — LPT/USDT P26_50

**Symbol:** LPT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6073 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -3.7863 |
| sortino_ratio | -1.1987 |
| max_drawdown | 0.7613 |
| cagr | -0.4243 |
| net_avg_win | 52.0211 |
| net_avg_loss | -70.7455 |
| avg_hold_time_bars | 5.9716 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
