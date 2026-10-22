# EMA Hourly Continuation — SKY/USDT P34_100

**Symbol:** SKY/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.5907 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9685 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -4.5332 |
| sortino_ratio | -1.5787 |
| max_drawdown | 0.8360 |
| cagr | -0.5433 |
| net_avg_win | 47.2533 |
| net_avg_loss | -72.5656 |
| avg_hold_time_bars | 10.4464 |
| exposure | 0.2988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
