# EMA Hourly Continuation — IOST/USDT P8_100

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.8446 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0794 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -1.2452 |
| sortino_ratio | -0.3954 |
| max_drawdown | 0.4379 |
| cagr | -0.1694 |
| net_avg_win | 80.0212 |
| net_avg_loss | -101.5724 |
| avg_hold_time_bars | 30.4867 |
| exposure | 0.6776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
