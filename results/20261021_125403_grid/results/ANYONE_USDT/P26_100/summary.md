# EMA Hourly Continuation — ANYONE/USDT P26_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.7029 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8108 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -2.3153 |
| sortino_ratio | -0.6960 |
| max_drawdown | 0.5378 |
| cagr | -0.2750 |
| net_avg_win | 66.7503 |
| net_avg_loss | -77.9319 |
| avg_hold_time_bars | 16.3547 |
| exposure | 0.3355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
