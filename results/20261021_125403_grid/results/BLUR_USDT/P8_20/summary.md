# EMA Hourly Continuation — BLUR/USDT P8_20

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.6577 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9112 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -3.6906 |
| sortino_ratio | -1.3292 |
| max_drawdown | 0.7899 |
| cagr | -0.4563 |
| net_avg_win | 50.4457 |
| net_avg_loss | -67.6488 |
| avg_hold_time_bars | 5.3950 |
| exposure | 0.1558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
