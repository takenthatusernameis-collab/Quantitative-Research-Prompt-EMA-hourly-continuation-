# EMA Hourly Continuation — DOGS/USDT P50_100

**Symbol:** DOGS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7486 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9391 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -1.6851 |
| sortino_ratio | -0.4420 |
| max_drawdown | 0.3543 |
| cagr | -0.1840 |
| net_avg_win | 75.3457 |
| net_avg_loss | -94.5726 |
| avg_hold_time_bars | 9.5052 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
