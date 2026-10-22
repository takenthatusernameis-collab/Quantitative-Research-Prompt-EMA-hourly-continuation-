# EMA Hourly Continuation — BIGTIME/USDT P26_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.6255 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9331 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -2.5162 |
| sortino_ratio | -0.6293 |
| max_drawdown | 0.5382 |
| cagr | -0.2499 |
| net_avg_win | 57.8080 |
| net_avg_loss | -88.2768 |
| avg_hold_time_bars | 5.7410 |
| exposure | 0.0792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
