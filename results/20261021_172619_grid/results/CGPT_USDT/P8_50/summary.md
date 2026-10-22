# EMA Hourly Continuation — CGPT/USDT P8_50

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.8341 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0242 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -1.5006 |
| sortino_ratio | -0.5571 |
| max_drawdown | 0.5167 |
| cagr | -0.2288 |
| net_avg_win | 70.8911 |
| net_avg_loss | -87.5620 |
| avg_hold_time_bars | 13.9045 |
| exposure | 0.4235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
