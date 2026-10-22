# EMA Hourly Continuation — ACE/USDT P21_50

**Symbol:** ACE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7281 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 0.9894 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -1.9553 |
| sortino_ratio | -0.6371 |
| max_drawdown | 0.5493 |
| cagr | -0.2531 |
| net_avg_win | 52.8418 |
| net_avg_loss | -75.4363 |
| avg_hold_time_bars | 8.3552 |
| exposure | 0.1959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
