# EMA Hourly Continuation — BLUR/USDT P8_12

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6123 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -3.1479 |
| sortino_ratio | -0.8624 |
| max_drawdown | 0.6359 |
| cagr | -0.3261 |
| net_avg_win | 57.9012 |
| net_avg_loss | -83.4051 |
| avg_hold_time_bars | 4.1008 |
| exposure | 0.0681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
