# EMA Hourly Continuation — SUPER/USDT P26_55

**Symbol:** SUPER/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.5016 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8304 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -6.1760 |
| sortino_ratio | -2.6575 |
| max_drawdown | 0.9599 |
| cagr | -0.7166 |
| net_avg_win | 23.0663 |
| net_avg_loss | -38.2110 |
| avg_hold_time_bars | 4.8165 |
| exposure | 0.2016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
