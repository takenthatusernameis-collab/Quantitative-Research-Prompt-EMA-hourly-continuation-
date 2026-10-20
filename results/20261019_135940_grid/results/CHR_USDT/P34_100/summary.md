# EMA Hourly Continuation — CHR/USDT P34_100

**Symbol:** CHR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.5909 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8860 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -4.6808 |
| sortino_ratio | -1.7382 |
| max_drawdown | 0.8801 |
| cagr | -0.5654 |
| net_avg_win | 39.4918 |
| net_avg_loss | -56.3124 |
| avg_hold_time_bars | 8.4373 |
| exposure | 0.2680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
