# EMA Hourly Continuation — FLOKI/USDT P8_21

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6923 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9174 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.8024 |
| sortino_ratio | -0.8998 |
| max_drawdown | 0.6584 |
| cagr | -0.3376 |
| net_avg_win | 60.4196 |
| net_avg_loss | -79.0441 |
| avg_hold_time_bars | 5.4396 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
