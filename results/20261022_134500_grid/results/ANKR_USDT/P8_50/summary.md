# EMA Hourly Continuation — ANKR/USDT P8_50

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.5974 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -6.3158 |
| sortino_ratio | -2.7583 |
| max_drawdown | 0.9651 |
| cagr | -0.7330 |
| net_avg_win | 33.0196 |
| net_avg_loss | -45.9400 |
| avg_hold_time_bars | 12.3742 |
| exposure | 0.5366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
