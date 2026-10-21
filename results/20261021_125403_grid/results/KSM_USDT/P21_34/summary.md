# EMA Hourly Continuation — KSM/USDT P21_34

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.5583 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -3.4171 |
| sortino_ratio | -0.9223 |
| max_drawdown | 0.6617 |
| cagr | -0.3454 |
| net_avg_win | 51.1007 |
| net_avg_loss | -76.8316 |
| avg_hold_time_bars | 4.9014 |
| exposure | 0.0791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
