# EMA Hourly Continuation — RSR/USDT P21_50

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.8341 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.0679 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -1.2424 |
| sortino_ratio | -0.3906 |
| max_drawdown | 0.4284 |
| cagr | -0.1661 |
| net_avg_win | 74.5549 |
| net_avg_loss | -95.9877 |
| avg_hold_time_bars | 7.9748 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
