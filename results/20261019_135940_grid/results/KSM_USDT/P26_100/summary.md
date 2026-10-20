# EMA Hourly Continuation — KSM/USDT P26_100

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6154 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -3.6692 |
| sortino_ratio | -1.2510 |
| max_drawdown | 0.7871 |
| cagr | -0.4529 |
| net_avg_win | 43.1896 |
| net_avg_loss | -67.6104 |
| avg_hold_time_bars | 14.0747 |
| exposure | 0.3768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
