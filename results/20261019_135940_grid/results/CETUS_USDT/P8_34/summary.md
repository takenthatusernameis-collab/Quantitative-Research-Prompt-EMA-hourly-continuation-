# EMA Hourly Continuation — CETUS/USDT P8_34

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1341 |
| net_profit_factor | 0.5926 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -7.2082 |
| sortino_ratio | -3.6944 |
| max_drawdown | 0.9892 |
| cagr | -0.8340 |
| net_avg_win | 23.3593 |
| net_avg_loss | -33.4916 |
| avg_hold_time_bars | 5.6010 |
| exposure | 0.3399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
