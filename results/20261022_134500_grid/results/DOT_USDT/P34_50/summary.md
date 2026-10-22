# EMA Hourly Continuation — DOT/USDT P34_50

**Symbol:** DOT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 870 |
| net_profit_factor | 0.3607 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.8918 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -9.1633 |
| sortino_ratio | -3.8399 |
| max_drawdown | 0.9934 |
| cagr | -0.8625 |
| net_avg_win | 14.7468 |
| net_avg_loss | -31.7047 |
| avg_hold_time_bars | 2.5701 |
| exposure | 0.1016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
