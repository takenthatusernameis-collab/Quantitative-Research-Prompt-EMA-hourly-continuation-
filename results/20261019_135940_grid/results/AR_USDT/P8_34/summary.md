# EMA Hourly Continuation — AR/USDT P8_34

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1395 |
| net_profit_factor | 0.5097 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -7.9631 |
| sortino_ratio | -4.1692 |
| max_drawdown | 0.9941 |
| cagr | -0.8696 |
| net_avg_win | 16.5363 |
| net_avg_loss | -26.3314 |
| avg_hold_time_bars | 5.5950 |
| exposure | 0.3548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
