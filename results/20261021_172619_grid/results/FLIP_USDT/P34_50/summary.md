# EMA Hourly Continuation — FLIP/USDT P34_50

**Symbol:** FLIP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.4085 |
| net_win_rate | 0.3993 |
| gross_profit_factor | 0.7680 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -5.0086 |
| sortino_ratio | -1.2296 |
| max_drawdown | 0.7744 |
| cagr | -0.4455 |
| net_avg_win | 45.6004 |
| net_avg_loss | -74.2096 |
| avg_hold_time_bars | 8.4232 |
| exposure | 0.1122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
