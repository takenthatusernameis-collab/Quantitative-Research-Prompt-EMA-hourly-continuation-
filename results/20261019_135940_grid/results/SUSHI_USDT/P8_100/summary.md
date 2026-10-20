# EMA Hourly Continuation — SUSHI/USDT P8_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.5653 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8357 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -4.9164 |
| sortino_ratio | -1.7846 |
| max_drawdown | 0.8899 |
| cagr | -0.5799 |
| net_avg_win | 38.3594 |
| net_avg_loss | -54.1766 |
| avg_hold_time_bars | 21.4705 |
| exposure | 0.6587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
