# EMA Hourly Continuation — ANKR/USDT P26_200

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6223 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8923 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -3.1181 |
| sortino_ratio | -0.8436 |
| max_drawdown | 0.6557 |
| cagr | -0.3352 |
| net_avg_win | 62.1535 |
| net_avg_loss | -84.4713 |
| avg_hold_time_bars | 37.1779 |
| exposure | 0.6270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
