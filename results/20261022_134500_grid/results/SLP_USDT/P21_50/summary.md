# EMA Hourly Continuation — SLP/USDT P21_50

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1127 |
| net_profit_factor | 0.5062 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.8849 |
| gross_win_rate | 0.4303 |
| sharpe_ratio | -9.2197 |
| sortino_ratio | -4.3748 |
| max_drawdown | 0.9959 |
| cagr | -0.8848 |
| net_avg_win | 21.6689 |
| net_avg_loss | -30.7349 |
| avg_hold_time_bars | 4.3283 |
| exposure | 0.2217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
