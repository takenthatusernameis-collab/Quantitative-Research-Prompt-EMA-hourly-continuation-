# EMA Hourly Continuation — SYN/USDT P8_21

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1546 |
| net_profit_factor | 0.4631 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.8205 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -9.3874 |
| sortino_ratio | -5.1908 |
| max_drawdown | 0.9983 |
| cagr | -0.9217 |
| net_avg_win | 12.7770 |
| net_avg_loss | -21.3246 |
| avg_hold_time_bars | 3.5369 |
| exposure | 0.2485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
