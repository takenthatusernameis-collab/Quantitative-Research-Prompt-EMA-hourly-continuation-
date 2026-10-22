# EMA Hourly Continuation — BIGTIME/USDT P55_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7948 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0684 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -1.5932 |
| sortino_ratio | -0.4563 |
| max_drawdown | 0.4724 |
| cagr | -0.1890 |
| net_avg_win | 77.9264 |
| net_avg_loss | -102.5697 |
| avg_hold_time_bars | 8.0100 |
| exposure | 0.1446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
