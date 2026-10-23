# EMA Hourly Continuation — PROM/USDT P34_55

**Symbol:** PROM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.3765 |
| net_win_rate | 0.3931 |
| gross_profit_factor | 0.8453 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -9.8882 |
| sortino_ratio | -4.2340 |
| max_drawdown | 0.9954 |
| cagr | -0.8829 |
| net_avg_win | 16.9346 |
| net_avg_loss | -29.1350 |
| avg_hold_time_bars | 3.6523 |
| exposure | 0.1499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
