# EMA Hourly Continuation — ATOM/USDT P21_55

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.4344 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.8381 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -7.1506 |
| sortino_ratio | -3.0314 |
| max_drawdown | 0.9754 |
| cagr | -0.7685 |
| net_avg_win | 18.7590 |
| net_avg_loss | -34.9515 |
| avg_hold_time_bars | 5.5448 |
| exposure | 0.2248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
