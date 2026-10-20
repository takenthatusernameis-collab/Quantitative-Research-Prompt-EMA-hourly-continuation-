# EMA Hourly Continuation — YGG/USDT P8_50

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1120 |
| net_profit_factor | 0.6740 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -5.3746 |
| sortino_ratio | -2.5240 |
| max_drawdown | 0.9546 |
| cagr | -0.7005 |
| net_avg_win | 37.2854 |
| net_avg_loss | -49.3397 |
| avg_hold_time_bars | 9.0571 |
| exposure | 0.4590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
