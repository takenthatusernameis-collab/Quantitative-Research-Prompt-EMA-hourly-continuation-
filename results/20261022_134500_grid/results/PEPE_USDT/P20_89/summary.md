# EMA Hourly Continuation — PEPE/USDT P20_89

**Symbol:** PEPE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.5576 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.8232 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -5.3254 |
| sortino_ratio | -1.9295 |
| max_drawdown | 0.9083 |
| cagr | -0.6073 |
| net_avg_win | 39.0392 |
| net_avg_loss | -54.8078 |
| avg_hold_time_bars | 13.2526 |
| exposure | 0.4006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
