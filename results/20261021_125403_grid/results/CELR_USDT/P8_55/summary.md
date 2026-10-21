# EMA Hourly Continuation — CELR/USDT P8_55

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.7345 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9364 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -2.9028 |
| sortino_ratio | -1.0976 |
| max_drawdown | 0.7239 |
| cagr | -0.3963 |
| net_avg_win | 59.1033 |
| net_avg_loss | -73.2913 |
| avg_hold_time_bars | 15.4540 |
| exposure | 0.4944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
