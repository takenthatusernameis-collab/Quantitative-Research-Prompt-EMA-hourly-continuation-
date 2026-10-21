# EMA Hourly Continuation — FLOW/USDT P21_50

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7061 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9855 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.5850 |
| sortino_ratio | -0.8372 |
| max_drawdown | 0.6317 |
| cagr | -0.3185 |
| net_avg_win | 59.1613 |
| net_avg_loss | -80.8911 |
| avg_hold_time_bars | 7.2975 |
| exposure | 0.1695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
