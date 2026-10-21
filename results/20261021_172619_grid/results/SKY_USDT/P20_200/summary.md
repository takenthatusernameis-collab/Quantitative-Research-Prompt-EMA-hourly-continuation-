# EMA Hourly Continuation — SKY/USDT P20_200

**Symbol:** SKY/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.9465 |
| net_win_rate | 0.5362 |
| gross_profit_factor | 1.1406 |
| gross_win_rate | 0.5362 |
| sharpe_ratio | -0.2636 |
| sortino_ratio | -0.0700 |
| max_drawdown | 0.2569 |
| cagr | -0.0365 |
| net_avg_win | 87.7611 |
| net_avg_loss | -107.2052 |
| avg_hold_time_bars | 39.8514 |
| exposure | 0.6133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
