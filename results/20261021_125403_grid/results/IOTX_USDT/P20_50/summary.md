# EMA Hourly Continuation — IOTX/USDT P20_50

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.7640 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0555 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -1.9959 |
| sortino_ratio | -0.6647 |
| max_drawdown | 0.5822 |
| cagr | -0.2623 |
| net_avg_win | 62.6451 |
| net_avg_loss | -87.3826 |
| avg_hold_time_bars | 6.6579 |
| exposure | 0.1619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
