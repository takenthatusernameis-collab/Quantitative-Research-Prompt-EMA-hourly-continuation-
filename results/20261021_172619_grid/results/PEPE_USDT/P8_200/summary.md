# EMA Hourly Continuation — PEPE/USDT P8_200

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.9488 |
| net_win_rate | 0.5290 |
| gross_profit_factor | 1.1114 |
| gross_win_rate | 0.5290 |
| sharpe_ratio | -0.2286 |
| sortino_ratio | -0.0547 |
| max_drawdown | 0.1264 |
| cagr | -0.0290 |
| net_avg_win | 90.5168 |
| net_avg_loss | -107.1454 |
| avg_hold_time_bars | 62.9384 |
| exposure | 0.7896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
