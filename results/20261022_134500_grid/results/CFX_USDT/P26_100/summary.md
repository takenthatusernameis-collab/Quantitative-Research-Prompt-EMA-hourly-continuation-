# EMA Hourly Continuation — CFX/USDT P26_100

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.6198 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9478 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -3.6421 |
| sortino_ratio | -1.2821 |
| max_drawdown | 0.7933 |
| cagr | -0.4562 |
| net_avg_win | 42.4255 |
| net_avg_loss | -63.9900 |
| avg_hold_time_bars | 12.8218 |
| exposure | 0.3631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
