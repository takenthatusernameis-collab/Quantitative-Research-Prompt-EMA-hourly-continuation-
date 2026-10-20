# EMA Hourly Continuation — AVA/USDT P20_55

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 942 |
| net_profit_factor | 0.4728 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8652 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -6.7400 |
| sortino_ratio | -2.9065 |
| max_drawdown | 0.9738 |
| cagr | -0.7617 |
| net_avg_win | 20.0075 |
| net_avg_loss | -36.4633 |
| avg_hold_time_bars | 5.0786 |
| exposure | 0.2175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
