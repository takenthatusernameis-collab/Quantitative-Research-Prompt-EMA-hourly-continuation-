# EMA Hourly Continuation — SAND/USDT P50_200

**Symbol:** SAND/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7213 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0527 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -2.0287 |
| sortino_ratio | -0.5406 |
| max_drawdown | 0.5045 |
| cagr | -0.2283 |
| net_avg_win | 68.0256 |
| net_avg_loss | -96.4344 |
| avg_hold_time_bars | 25.1556 |
| exposure | 0.4116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
