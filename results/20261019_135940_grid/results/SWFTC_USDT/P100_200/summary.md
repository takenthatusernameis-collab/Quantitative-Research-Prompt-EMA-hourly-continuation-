# EMA Hourly Continuation — SWFTC/USDT P100_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.5429 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.8920 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -4.3981 |
| sortino_ratio | -1.2801 |
| max_drawdown | 0.7892 |
| cagr | -0.4600 |
| net_avg_win | 49.4620 |
| net_avg_loss | -73.2794 |
| avg_hold_time_bars | 8.9717 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
