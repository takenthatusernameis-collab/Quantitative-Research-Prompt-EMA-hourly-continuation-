# EMA Hourly Continuation — MINA/USDT P50_100

**Symbol:** MINA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.5399 |
| net_win_rate | 0.4463 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -5.4111 |
| sortino_ratio | -1.9339 |
| max_drawdown | 0.9134 |
| cagr | -0.6095 |
| net_avg_win | 37.0332 |
| net_avg_loss | -55.2974 |
| avg_hold_time_bars | 6.4681 |
| exposure | 0.1890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
