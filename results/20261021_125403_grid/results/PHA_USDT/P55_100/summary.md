# EMA Hourly Continuation — PHA/USDT P55_100

**Symbol:** PHA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.6356 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8086 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -2.6380 |
| sortino_ratio | -0.6978 |
| max_drawdown | 0.5588 |
| cagr | -0.2746 |
| net_avg_win | 62.2762 |
| net_avg_loss | -79.0987 |
| avg_hold_time_bars | 7.9135 |
| exposure | 0.1248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
