# EMA Hourly Continuation — NOT/USDT P55_100

**Symbol:** NOT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7784 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 0.9992 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.2613 |
| sortino_ratio | -0.3222 |
| max_drawdown | 0.3094 |
| cagr | -0.1379 |
| net_avg_win | 68.5966 |
| net_avg_loss | -90.4563 |
| avg_hold_time_bars | 7.6993 |
| exposure | 0.1107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
