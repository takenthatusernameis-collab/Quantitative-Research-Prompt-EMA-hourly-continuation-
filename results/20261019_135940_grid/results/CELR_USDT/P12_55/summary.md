# EMA Hourly Continuation — CELR/USDT P12_55

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 982 |
| net_profit_factor | 0.5619 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.9005 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -5.7861 |
| sortino_ratio | -2.5477 |
| max_drawdown | 0.9537 |
| cagr | -0.7024 |
| net_avg_win | 27.2210 |
| net_avg_loss | -40.8105 |
| avg_hold_time_bars | 8.8778 |
| exposure | 0.3945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
