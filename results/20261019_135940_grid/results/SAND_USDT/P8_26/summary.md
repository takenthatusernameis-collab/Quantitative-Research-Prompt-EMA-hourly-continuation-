# EMA Hourly Continuation — SAND/USDT P8_26

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1500 |
| net_profit_factor | 0.3454 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.7918 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -10.8915 |
| sortino_ratio | -5.9244 |
| max_drawdown | 0.9995 |
| cagr | -0.9497 |
| net_avg_win | 8.1906 |
| net_avg_loss | -17.8379 |
| avg_hold_time_bars | 4.1333 |
| exposure | 0.2818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
