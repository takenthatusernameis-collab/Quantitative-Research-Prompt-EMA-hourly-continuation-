# EMA Hourly Continuation — TFUEL/USDT P8_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 933 |
| net_profit_factor | 0.5587 |
| net_win_rate | 0.4277 |
| gross_profit_factor | 0.8676 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -6.8368 |
| sortino_ratio | -2.9233 |
| max_drawdown | 0.9725 |
| cagr | -0.7572 |
| net_avg_win | 30.8429 |
| net_avg_loss | -41.2452 |
| avg_hold_time_bars | 14.1554 |
| exposure | 0.5976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
