# EMA Hourly Continuation — CATI/USDT P21_50

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.5830 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7494 |
| gross_win_rate | 0.4212 |
| sharpe_ratio | -3.9660 |
| sortino_ratio | -1.2114 |
| max_drawdown | 0.6992 |
| cagr | -0.4309 |
| net_avg_win | 59.2573 |
| net_avg_loss | -73.9584 |
| avg_hold_time_bars | 8.6176 |
| exposure | 0.1828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
