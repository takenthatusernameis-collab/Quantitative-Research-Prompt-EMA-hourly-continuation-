# EMA Hourly Continuation — AXL/USDT P26_100

**Symbol:** AXL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.5862 |
| net_win_rate | 0.4346 |
| gross_profit_factor | 0.8553 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -5.4966 |
| sortino_ratio | -2.1200 |
| max_drawdown | 0.9241 |
| cagr | -0.6385 |
| net_avg_win | 39.7504 |
| net_avg_loss | -52.1256 |
| avg_hold_time_bars | 9.8679 |
| exposure | 0.3380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
