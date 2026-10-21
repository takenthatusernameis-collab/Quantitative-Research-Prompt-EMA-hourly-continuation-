# EMA Hourly Continuation — JASMY/USDT P34_100

**Symbol:** JASMY/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.7882 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 0.9819 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -1.4045 |
| sortino_ratio | -0.4156 |
| max_drawdown | 0.4208 |
| cagr | -0.1745 |
| net_avg_win | 66.4769 |
| net_avg_loss | -85.1310 |
| avg_hold_time_bars | 12.0047 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
