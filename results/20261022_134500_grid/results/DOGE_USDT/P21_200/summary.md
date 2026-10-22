# EMA Hourly Continuation — DOGE/USDT P21_200

**Symbol:** DOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.6368 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9908 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -2.9637 |
| sortino_ratio | -0.7655 |
| max_drawdown | 0.6411 |
| cagr | -0.3142 |
| net_avg_win | 65.4464 |
| net_avg_loss | -92.1014 |
| avg_hold_time_bars | 40.9885 |
| exposure | 0.6465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
