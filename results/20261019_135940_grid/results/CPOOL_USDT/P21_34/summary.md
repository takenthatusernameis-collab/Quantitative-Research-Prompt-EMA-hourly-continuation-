# EMA Hourly Continuation — CPOOL/USDT P21_34

**Symbol:** CPOOL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1089 |
| net_profit_factor | 0.5348 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8999 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -7.6804 |
| sortino_ratio | -3.5336 |
| max_drawdown | 0.9893 |
| cagr | -0.8342 |
| net_avg_win | 22.7897 |
| net_avg_loss | -36.0379 |
| avg_hold_time_bars | 2.7273 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
