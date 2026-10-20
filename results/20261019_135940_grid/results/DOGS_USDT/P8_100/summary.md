# EMA Hourly Continuation — DOGS/USDT P8_100

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.6918 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 0.9999 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -3.1743 |
| sortino_ratio | -1.2184 |
| max_drawdown | 0.7237 |
| cagr | -0.4442 |
| net_avg_win | 50.1685 |
| net_avg_loss | -73.2013 |
| avg_hold_time_bars | 19.0016 |
| exposure | 0.6441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
