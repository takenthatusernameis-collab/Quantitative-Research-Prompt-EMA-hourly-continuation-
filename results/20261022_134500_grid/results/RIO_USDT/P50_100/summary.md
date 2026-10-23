# EMA Hourly Continuation — RIO/USDT P50_100

**Symbol:** RIO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.4945 |
| net_win_rate | 0.4005 |
| gross_profit_factor | 0.7170 |
| gross_win_rate | 0.4019 |
| sharpe_ratio | -6.8152 |
| sortino_ratio | -2.6066 |
| max_drawdown | 0.9613 |
| cagr | -0.7217 |
| net_avg_win | 31.6754 |
| net_avg_loss | -42.7996 |
| avg_hold_time_bars | 4.5304 |
| exposure | 0.1537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
