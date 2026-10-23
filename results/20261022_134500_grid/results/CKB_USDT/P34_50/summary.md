# EMA Hourly Continuation — CKB/USDT P34_50

**Symbol:** CKB/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.3544 |
| net_win_rate | 0.3968 |
| gross_profit_factor | 0.7026 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -10.2081 |
| sortino_ratio | -4.4406 |
| max_drawdown | 0.9966 |
| cagr | -0.8955 |
| net_avg_win | 14.8246 |
| net_avg_loss | -27.5150 |
| avg_hold_time_bars | 2.5968 |
| exposure | 0.1098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
