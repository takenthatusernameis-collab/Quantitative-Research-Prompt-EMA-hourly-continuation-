# EMA Hourly Continuation — GMX/USDT P100_144

**Symbol:** GMX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.4663 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.8247 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -5.6823 |
| sortino_ratio | -1.8613 |
| max_drawdown | 0.8907 |
| cagr | -0.5857 |
| net_avg_win | 34.8889 |
| net_avg_loss | -55.0702 |
| avg_hold_time_bars | 4.4468 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
