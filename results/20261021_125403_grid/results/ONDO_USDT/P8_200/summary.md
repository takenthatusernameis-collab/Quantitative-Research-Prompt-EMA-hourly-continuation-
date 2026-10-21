# EMA Hourly Continuation — ONDO/USDT P8_200

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.8499 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9855 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -0.9307 |
| sortino_ratio | -0.2511 |
| max_drawdown | 0.3349 |
| cagr | -0.1112 |
| net_avg_win | 81.9695 |
| net_avg_loss | -95.3716 |
| avg_hold_time_bars | 44.4747 |
| exposure | 0.7197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
