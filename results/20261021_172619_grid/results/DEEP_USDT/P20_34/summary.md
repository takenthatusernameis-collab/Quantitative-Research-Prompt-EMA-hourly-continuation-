# EMA Hourly Continuation — DEEP/USDT P20_34

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.8507 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.1192 |
| gross_win_rate | 0.5317 |
| sharpe_ratio | -0.9213 |
| sortino_ratio | -0.2497 |
| max_drawdown | 0.2203 |
| cagr | -0.1101 |
| net_avg_win | 79.6315 |
| net_avg_loss | -104.7782 |
| avg_hold_time_bars | 5.0493 |
| exposure | 0.0812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
