# EMA Hourly Continuation — BLZ/USDT P26_200

**Symbol:** BLZ/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.6491 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8436 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -2.4166 |
| sortino_ratio | -0.5642 |
| max_drawdown | 0.5192 |
| cagr | -0.2309 |
| net_avg_win | 72.8160 |
| net_avg_loss | -91.9904 |
| avg_hold_time_bars | 59.4799 |
| exposure | 0.7349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
