# EMA Hourly Continuation — XMR/USDT P21_50

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1398 |
| net_profit_factor | 0.2384 |
| net_win_rate | 0.3920 |
| gross_profit_factor | 0.6369 |
| gross_win_rate | 0.4113 |
| sharpe_ratio | -13.1391 |
| sortino_ratio | -6.9681 |
| max_drawdown | 0.9999 |
| cagr | -0.9738 |
| net_avg_win | 5.7126 |
| net_avg_loss | -15.4464 |
| avg_hold_time_bars | 2.9471 |
| exposure | 0.1873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
