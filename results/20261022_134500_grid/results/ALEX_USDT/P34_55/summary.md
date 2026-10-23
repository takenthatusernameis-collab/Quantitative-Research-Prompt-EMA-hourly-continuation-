# EMA Hourly Continuation — ALEX/USDT P34_55

**Symbol:** ALEX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.3877 |
| net_win_rate | 0.3501 |
| gross_profit_factor | 0.7502 |
| gross_win_rate | 0.3787 |
| sharpe_ratio | -9.5858 |
| sortino_ratio | -3.6665 |
| max_drawdown | 0.9918 |
| cagr | -0.8487 |
| net_avg_win | 24.4243 |
| net_avg_loss | -33.9411 |
| avg_hold_time_bars | 5.4373 |
| exposure | 0.1814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
