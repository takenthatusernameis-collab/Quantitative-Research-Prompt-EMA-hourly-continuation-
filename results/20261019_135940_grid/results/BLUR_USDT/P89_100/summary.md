# EMA Hourly Continuation — BLUR/USDT P89_100

**Symbol:** BLUR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.3288 |
| net_win_rate | 0.4010 |
| gross_profit_factor | 0.8117 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -8.4808 |
| sortino_ratio | -3.0045 |
| max_drawdown | 0.9787 |
| cagr | -0.7817 |
| net_avg_win | 19.7246 |
| net_avg_loss | -40.1593 |
| avg_hold_time_bars | 2.3284 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
