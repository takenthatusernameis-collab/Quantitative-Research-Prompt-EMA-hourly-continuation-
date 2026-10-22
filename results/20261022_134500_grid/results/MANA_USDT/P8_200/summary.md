# EMA Hourly Continuation — MANA/USDT P8_200

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6188 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9232 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.5290 |
| sortino_ratio | -0.5939 |
| max_drawdown | 0.5481 |
| cagr | -0.2571 |
| net_avg_win | 62.3246 |
| net_avg_loss | -90.7777 |
| avg_hold_time_bars | 63.5433 |
| exposure | 0.8347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
