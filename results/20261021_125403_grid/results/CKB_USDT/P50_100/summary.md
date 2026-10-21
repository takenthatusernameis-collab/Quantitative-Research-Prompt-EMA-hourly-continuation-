# EMA Hourly Continuation — CKB/USDT P50_100

**Symbol:** CKB/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.7786 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0452 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.7240 |
| sortino_ratio | -0.4837 |
| max_drawdown | 0.4685 |
| cagr | -0.1995 |
| net_avg_win | 77.9923 |
| net_avg_loss | -102.2946 |
| avg_hold_time_bars | 8.5471 |
| exposure | 0.1484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
