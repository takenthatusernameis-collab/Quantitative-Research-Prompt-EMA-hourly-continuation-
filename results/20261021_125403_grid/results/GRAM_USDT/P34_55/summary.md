# EMA Hourly Continuation — GRAM/USDT P34_55

**Symbol:** GRAM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.6910 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 1.0457 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -1.8801 |
| sortino_ratio | -0.4337 |
| max_drawdown | 0.4042 |
| cagr | -0.1784 |
| net_avg_win | 66.9992 |
| net_avg_loss | -100.0358 |
| avg_hold_time_bars | 5.1641 |
| exposure | 0.0601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
