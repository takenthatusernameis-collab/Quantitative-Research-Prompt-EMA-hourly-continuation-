# EMA Hourly Continuation — ZKJ/USDT P50_200

**Symbol:** ZKJ/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 0.2199 |
| net_win_rate | 0.3474 |
| gross_profit_factor | 0.5630 |
| gross_win_rate | 0.3897 |
| sharpe_ratio | -5.7878 |
| sortino_ratio | -1.2244 |
| max_drawdown | 0.8049 |
| cagr | -0.4701 |
| net_avg_win | 30.3557 |
| net_avg_loss | -73.5032 |
| avg_hold_time_bars | 83.7512 |
| exposure | 0.8109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
