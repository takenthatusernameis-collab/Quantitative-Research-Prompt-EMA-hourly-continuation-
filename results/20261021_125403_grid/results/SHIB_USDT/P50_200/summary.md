# EMA Hourly Continuation — SHIB/USDT P50_200

**Symbol:** SHIB/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.7656 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9765 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -1.4434 |
| sortino_ratio | -0.3407 |
| max_drawdown | 0.3975 |
| cagr | -0.1453 |
| net_avg_win | 79.4172 |
| net_avg_loss | -99.9966 |
| avg_hold_time_bars | 30.6374 |
| exposure | 0.3802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
