# EMA Hourly Continuation — SAND/USDT P55_100

**Symbol:** SAND/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.4359 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8046 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -5.8812 |
| sortino_ratio | -2.0107 |
| max_drawdown | 0.9208 |
| cagr | -0.6344 |
| net_avg_win | 26.7333 |
| net_avg_loss | -50.0363 |
| avg_hold_time_bars | 5.3970 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
