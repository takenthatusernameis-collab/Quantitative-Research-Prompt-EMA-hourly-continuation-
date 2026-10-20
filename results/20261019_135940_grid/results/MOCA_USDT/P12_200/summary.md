# EMA Hourly Continuation — MOCA/USDT P12_200

**Symbol:** MOCA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.5289 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.7509 |
| gross_win_rate | 0.4364 |
| sharpe_ratio | -4.1327 |
| sortino_ratio | -1.1926 |
| max_drawdown | 0.7383 |
| cagr | -0.4376 |
| net_avg_win | 50.0009 |
| net_avg_loss | -70.1505 |
| avg_hold_time_bars | 37.3974 |
| exposure | 0.7218 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
