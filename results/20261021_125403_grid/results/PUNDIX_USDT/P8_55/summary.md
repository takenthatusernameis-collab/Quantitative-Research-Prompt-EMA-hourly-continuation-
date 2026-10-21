# EMA Hourly Continuation — PUNDIX/USDT P8_55

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9928 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -3.2001 |
| sortino_ratio | -1.2707 |
| max_drawdown | 0.7909 |
| cagr | -0.4418 |
| net_avg_win | 57.3107 |
| net_avg_loss | -73.8293 |
| avg_hold_time_bars | 12.8497 |
| exposure | 0.4509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
