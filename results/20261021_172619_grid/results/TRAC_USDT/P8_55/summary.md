# EMA Hourly Continuation — TRAC/USDT P8_55

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.7358 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -2.6599 |
| sortino_ratio | -0.9586 |
| max_drawdown | 0.6928 |
| cagr | -0.3560 |
| net_avg_win | 61.6690 |
| net_avg_loss | -74.6687 |
| avg_hold_time_bars | 15.0281 |
| exposure | 0.4379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
