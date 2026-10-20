# EMA Hourly Continuation — PUFFER/USDT P21_100

**Symbol:** PUFFER/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.8280 |
| net_win_rate | 0.5299 |
| gross_profit_factor | 1.1485 |
| gross_win_rate | 0.5363 |
| sharpe_ratio | -1.3316 |
| sortino_ratio | -0.4556 |
| max_drawdown | 0.3760 |
| cagr | -0.1975 |
| net_avg_win | 69.6080 |
| net_avg_loss | -94.7625 |
| avg_hold_time_bars | 17.4658 |
| exposure | 0.4626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
