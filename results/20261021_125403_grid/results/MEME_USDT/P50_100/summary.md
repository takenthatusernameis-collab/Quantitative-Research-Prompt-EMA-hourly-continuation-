# EMA Hourly Continuation — MEME/USDT P50_100

**Symbol:** MEME/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7599 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9855 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.6592 |
| sortino_ratio | -0.4654 |
| max_drawdown | 0.4246 |
| cagr | -0.1930 |
| net_avg_win | 68.9824 |
| net_avg_loss | -90.3090 |
| avg_hold_time_bars | 9.3394 |
| exposure | 0.1626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
