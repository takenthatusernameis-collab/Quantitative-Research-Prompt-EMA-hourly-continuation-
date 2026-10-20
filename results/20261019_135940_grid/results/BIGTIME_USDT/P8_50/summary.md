# EMA Hourly Continuation — BIGTIME/USDT P8_50

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.6597 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9921 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -4.5024 |
| sortino_ratio | -1.9330 |
| max_drawdown | 0.9096 |
| cagr | -0.6091 |
| net_avg_win | 38.4606 |
| net_avg_loss | -54.3702 |
| avg_hold_time_bars | 11.6663 |
| exposure | 0.5000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
