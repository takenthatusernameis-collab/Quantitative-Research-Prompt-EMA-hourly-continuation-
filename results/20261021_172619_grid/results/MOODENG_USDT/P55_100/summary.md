# EMA Hourly Continuation — MOODENG/USDT P55_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.7716 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -1.5923 |
| sortino_ratio | -0.4410 |
| max_drawdown | 0.3757 |
| cagr | -0.1840 |
| net_avg_win | 76.1424 |
| net_avg_loss | -96.1552 |
| avg_hold_time_bars | 7.9805 |
| exposure | 0.1360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
