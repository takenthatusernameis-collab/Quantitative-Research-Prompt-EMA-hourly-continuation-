# EMA Hourly Continuation — PUFFER/USDT P8_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.7856 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0358 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -1.3320 |
| sortino_ratio | -0.3486 |
| max_drawdown | 0.3799 |
| cagr | -0.1554 |
| net_avg_win | 74.9923 |
| net_avg_loss | -98.2497 |
| avg_hold_time_bars | 51.0072 |
| exposure | 0.8024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
