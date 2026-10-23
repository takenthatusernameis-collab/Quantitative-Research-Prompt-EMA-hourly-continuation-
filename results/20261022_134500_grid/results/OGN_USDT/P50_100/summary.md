# EMA Hourly Continuation — OGN/USDT P50_100

**Symbol:** OGN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.4365 |
| net_win_rate | 0.4215 |
| gross_profit_factor | 0.7760 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -6.6485 |
| sortino_ratio | -2.4195 |
| max_drawdown | 0.9516 |
| cagr | -0.6950 |
| net_avg_win | 26.0957 |
| net_avg_loss | -43.5633 |
| avg_hold_time_bars | 6.9462 |
| exposure | 0.2103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
