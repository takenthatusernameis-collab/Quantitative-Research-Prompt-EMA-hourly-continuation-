# EMA Hourly Continuation — LTC/USDT P8_26

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.7000 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0740 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -2.7263 |
| sortino_ratio | -0.9405 |
| max_drawdown | 0.6603 |
| cagr | -0.3473 |
| net_avg_win | 52.1858 |
| net_avg_loss | -79.1233 |
| avg_hold_time_bars | 6.9842 |
| exposure | 0.1813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
