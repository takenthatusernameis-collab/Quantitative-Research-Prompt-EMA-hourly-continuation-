# EMA Hourly Continuation — T/USDT P21_50

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.4912 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.9053 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -7.1540 |
| sortino_ratio | -2.8716 |
| max_drawdown | 0.9718 |
| cagr | -0.7558 |
| net_avg_win | 26.4910 |
| net_avg_loss | -41.9610 |
| avg_hold_time_bars | 6.0260 |
| exposure | 0.2206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
