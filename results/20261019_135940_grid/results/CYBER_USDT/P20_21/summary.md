# EMA Hourly Continuation — CYBER/USDT P20_21

**Symbol:** CYBER/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1210 |
| net_profit_factor | 0.1369 |
| net_win_rate | 0.3107 |
| gross_profit_factor | 0.5976 |
| gross_win_rate | 0.4083 |
| sharpe_ratio | -16.7422 |
| sortino_ratio | -8.7080 |
| max_drawdown | 1.0000 |
| cagr | -0.9918 |
| net_avg_win | 4.2184 |
| net_avg_loss | -13.8921 |
| avg_hold_time_bars | 2.3562 |
| exposure | 0.1296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
