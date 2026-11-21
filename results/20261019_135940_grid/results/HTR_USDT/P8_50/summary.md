# EMA Hourly Continuation — HTR/USDT P8_50

**Symbol:** HTR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1179 |
| net_profit_factor | 0.5161 |
| net_win_rate | 0.3953 |
| gross_profit_factor | 0.7658 |
| gross_win_rate | 0.4046 |
| sharpe_ratio | -8.7974 |
| sortino_ratio | -4.2323 |
| max_drawdown | 0.9947 |
| cagr | -0.8734 |
| net_avg_win | 22.7605 |
| net_avg_loss | -28.8229 |
| avg_hold_time_bars | 7.6149 |
| exposure | 0.4081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
