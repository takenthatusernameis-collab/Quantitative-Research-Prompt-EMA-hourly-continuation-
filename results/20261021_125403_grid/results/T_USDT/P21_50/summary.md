# EMA Hourly Continuation — T/USDT P21_50

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9730 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -3.8694 |
| sortino_ratio | -1.3251 |
| max_drawdown | 0.7948 |
| cagr | -0.4573 |
| net_avg_win | 50.3934 |
| net_avg_loss | -72.1538 |
| avg_hold_time_bars | 7.6337 |
| exposure | 0.1990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
