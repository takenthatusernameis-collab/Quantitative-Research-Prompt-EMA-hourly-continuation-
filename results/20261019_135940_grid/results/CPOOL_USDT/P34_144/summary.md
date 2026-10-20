# EMA Hourly Continuation — CPOOL/USDT P34_144

**Symbol:** CPOOL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.6459 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -3.7662 |
| sortino_ratio | -1.2975 |
| max_drawdown | 0.8138 |
| cagr | -0.4661 |
| net_avg_win | 52.2275 |
| net_avg_loss | -67.8764 |
| avg_hold_time_bars | 11.0758 |
| exposure | 0.3056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
