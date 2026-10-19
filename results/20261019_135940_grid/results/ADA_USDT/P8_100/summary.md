# EMA Hourly Continuation — ADA/USDT P8_100

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5545 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8665 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -4.5003 |
| sortino_ratio | -1.6255 |
| max_drawdown | 0.8627 |
| cagr | -0.5405 |
| net_avg_win | 35.2516 |
| net_avg_loss | -54.4135 |
| avg_hold_time_bars | 21.5632 |
| exposure | 0.6440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
