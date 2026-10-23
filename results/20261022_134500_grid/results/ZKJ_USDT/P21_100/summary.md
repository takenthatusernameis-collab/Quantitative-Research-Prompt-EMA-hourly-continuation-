# EMA Hourly Continuation — ZKJ/USDT P21_100

**Symbol:** ZKJ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.1802 |
| net_win_rate | 0.2940 |
| gross_profit_factor | 0.4663 |
| gross_win_rate | 0.3516 |
| sharpe_ratio | -9.2425 |
| sortino_ratio | -2.6419 |
| max_drawdown | 0.9751 |
| cagr | -0.7669 |
| net_avg_win | 20.0111 |
| net_avg_loss | -46.2384 |
| avg_hold_time_bars | 47.4945 |
| exposure | 0.7858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
