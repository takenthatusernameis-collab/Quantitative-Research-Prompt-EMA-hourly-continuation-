# EMA Hourly Continuation — TWT/USDT P34_100

**Symbol:** TWT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.4857 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -5.8613 |
| sortino_ratio | -2.1359 |
| max_drawdown | 0.9344 |
| cagr | -0.6499 |
| net_avg_win | 29.2213 |
| net_avg_loss | -49.0487 |
| avg_hold_time_bars | 9.2006 |
| exposure | 0.2794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
