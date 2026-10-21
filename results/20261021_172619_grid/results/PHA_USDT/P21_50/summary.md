# EMA Hourly Continuation — PHA/USDT P21_50

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.8266 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0574 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.4203 |
| sortino_ratio | -0.4619 |
| max_drawdown | 0.4714 |
| cagr | -0.1924 |
| net_avg_win | 75.5407 |
| net_avg_loss | -95.7792 |
| avg_hold_time_bars | 7.1621 |
| exposure | 0.1667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
