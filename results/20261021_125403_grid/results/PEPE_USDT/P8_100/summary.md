# EMA Hourly Continuation — PEPE/USDT P8_100

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.9530 |
| net_win_rate | 0.5319 |
| gross_profit_factor | 1.1273 |
| gross_win_rate | 0.5319 |
| sharpe_ratio | -0.2602 |
| sortino_ratio | -0.0773 |
| max_drawdown | 0.1810 |
| cagr | -0.0413 |
| net_avg_win | 90.4947 |
| net_avg_loss | -107.9064 |
| avg_hold_time_bars | 33.7636 |
| exposure | 0.6492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
