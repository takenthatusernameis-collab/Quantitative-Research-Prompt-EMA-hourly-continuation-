# EMA Hourly Continuation — SUSHI/USDT P8_20

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6848 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.9509 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.2605 |
| sortino_ratio | -1.1347 |
| max_drawdown | 0.7343 |
| cagr | -0.4054 |
| net_avg_win | 55.8894 |
| net_avg_loss | -74.7688 |
| avg_hold_time_bars | 5.3384 |
| exposure | 0.1435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
