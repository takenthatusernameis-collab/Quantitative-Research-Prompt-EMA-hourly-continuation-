# EMA Hourly Continuation — BLUR/USDT P89_100

**Symbol:** BLUR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 129 |
| net_profit_factor | 0.5352 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.7752 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -2.2279 |
| sortino_ratio | -0.3608 |
| max_drawdown | 0.3625 |
| cagr | -0.1532 |
| net_avg_win | 70.4530 |
| net_avg_loss | -100.9837 |
| avg_hold_time_bars | 4.4419 |
| exposure | 0.0259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
