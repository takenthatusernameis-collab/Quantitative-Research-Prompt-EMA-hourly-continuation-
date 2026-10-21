# EMA Hourly Continuation — RENDER/USDT P50_100

**Symbol:** RENDER/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7210 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9174 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.1558 |
| sortino_ratio | -0.6084 |
| max_drawdown | 0.4821 |
| cagr | -0.2441 |
| net_avg_win | 73.3253 |
| net_avg_loss | -91.9375 |
| avg_hold_time_bars | 8.2344 |
| exposure | 0.1465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
