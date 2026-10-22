# EMA Hourly Continuation — CYBER/USDT P21_200

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.8458 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0007 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9383 |
| sortino_ratio | -0.2356 |
| max_drawdown | 0.3223 |
| cagr | -0.1048 |
| net_avg_win | 86.4360 |
| net_avg_loss | -102.1936 |
| avg_hold_time_bars | 45.8604 |
| exposure | 0.6420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
