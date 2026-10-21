# EMA Hourly Continuation — CVX/USDT P21_55

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.7524 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9791 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -2.2471 |
| sortino_ratio | -0.7499 |
| max_drawdown | 0.5910 |
| cagr | -0.2919 |
| net_avg_win | 65.9950 |
| net_avg_loss | -84.5428 |
| avg_hold_time_bars | 7.7408 |
| exposure | 0.1914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
