# EMA Hourly Continuation — ALGO/USDT P20_144

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8349 |
| net_win_rate | 0.5421 |
| gross_profit_factor | 1.1983 |
| gross_win_rate | 0.5486 |
| sharpe_ratio | -1.1223 |
| sortino_ratio | -0.3413 |
| max_drawdown | 0.3676 |
| cagr | -0.1526 |
| net_avg_win | 68.5662 |
| net_avg_loss | -97.2311 |
| avg_hold_time_bars | 25.5356 |
| exposure | 0.5374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
