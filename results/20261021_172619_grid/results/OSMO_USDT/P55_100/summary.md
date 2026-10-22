# EMA Hourly Continuation — OSMO/USDT P55_100

**Symbol:** OSMO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6001 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -3.0986 |
| sortino_ratio | -0.8579 |
| max_drawdown | 0.6352 |
| cagr | -0.3258 |
| net_avg_win | 55.1539 |
| net_avg_loss | -76.2890 |
| avg_hold_time_bars | 7.9310 |
| exposure | 0.1359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
