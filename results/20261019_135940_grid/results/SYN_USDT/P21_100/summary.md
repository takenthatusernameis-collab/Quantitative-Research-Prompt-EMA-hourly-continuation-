# EMA Hourly Continuation — SYN/USDT P21_100

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.7040 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 1.0027 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -2.9150 |
| sortino_ratio | -1.0381 |
| max_drawdown | 0.7246 |
| cagr | -0.3915 |
| net_avg_win | 54.3451 |
| net_avg_loss | -73.4249 |
| avg_hold_time_bars | 14.4969 |
| exposure | 0.4217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
