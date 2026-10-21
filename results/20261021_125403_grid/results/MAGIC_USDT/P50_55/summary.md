# EMA Hourly Continuation — MAGIC/USDT P50_55

**Symbol:** MAGIC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.5421 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8493 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -2.9452 |
| sortino_ratio | -0.5989 |
| max_drawdown | 0.5145 |
| cagr | -0.2428 |
| net_avg_win | 66.1159 |
| net_avg_loss | -98.0043 |
| avg_hold_time_bars | 4.1337 |
| exposure | 0.0380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
