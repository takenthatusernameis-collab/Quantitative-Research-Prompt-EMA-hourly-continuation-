# EMA Hourly Continuation — ALPINE/USDT P21_50

**Symbol:** ALPINE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 914 |
| net_profit_factor | 0.3888 |
| net_win_rate | 0.4070 |
| gross_profit_factor | 0.7117 |
| gross_win_rate | 0.4256 |
| sharpe_ratio | -8.6984 |
| sortino_ratio | -3.7341 |
| max_drawdown | 0.9901 |
| cagr | -0.8395 |
| net_avg_win | 16.9309 |
| net_avg_loss | -29.8842 |
| avg_hold_time_bars | 6.1619 |
| exposure | 0.2560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
