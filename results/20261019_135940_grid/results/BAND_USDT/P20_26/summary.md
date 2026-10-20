# EMA Hourly Continuation — BAND/USDT P20_26

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.2689 |
| net_win_rate | 0.3942 |
| gross_profit_factor | 0.8249 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -12.2557 |
| sortino_ratio | -5.8848 |
| max_drawdown | 0.9996 |
| cagr | -0.9544 |
| net_avg_win | 8.2599 |
| net_avg_loss | -19.9876 |
| avg_hold_time_bars | 2.7502 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
