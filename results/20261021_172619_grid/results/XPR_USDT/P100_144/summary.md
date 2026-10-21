# EMA Hourly Continuation — XPR/USDT P100_144

**Symbol:** XPR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 169 |
| net_profit_factor | 0.6861 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.4993 |
| sortino_ratio | -0.2801 |
| max_drawdown | 0.2868 |
| cagr | -0.1198 |
| net_avg_win | 71.3358 |
| net_avg_loss | -102.7461 |
| avg_hold_time_bars | 8.6450 |
| exposure | 0.0664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
