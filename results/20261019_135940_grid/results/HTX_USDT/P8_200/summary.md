# EMA Hourly Continuation — HTX/USDT P8_200

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.3948 |
| net_win_rate | 0.3912 |
| gross_profit_factor | 0.8490 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -5.7560 |
| sortino_ratio | -1.4283 |
| max_drawdown | 0.8650 |
| cagr | -0.5454 |
| net_avg_win | 45.4115 |
| net_avg_loss | -73.8987 |
| avg_hold_time_bars | 58.2303 |
| exposure | 0.8353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
