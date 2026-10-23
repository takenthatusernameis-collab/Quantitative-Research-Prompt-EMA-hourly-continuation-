# EMA Hourly Continuation — ALPINE/USDT P8_12

**Symbol:** ALPINE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1403 |
| net_profit_factor | 0.2487 |
| net_win_rate | 0.3443 |
| gross_profit_factor | 0.5982 |
| gross_win_rate | 0.4056 |
| sharpe_ratio | -15.4063 |
| sortino_ratio | -8.3120 |
| max_drawdown | 1.0000 |
| cagr | -0.9873 |
| net_avg_win | 6.8523 |
| net_avg_loss | -14.4668 |
| avg_hold_time_bars | 3.8453 |
| exposure | 0.2452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
