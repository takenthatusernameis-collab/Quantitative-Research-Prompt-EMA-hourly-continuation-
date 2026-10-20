# EMA Hourly Continuation — CATI/USDT P34_55

**Symbol:** CATI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 833 |
| net_profit_factor | 0.4130 |
| net_win_rate | 0.4082 |
| gross_profit_factor | 0.7643 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -9.4328 |
| sortino_ratio | -4.2546 |
| max_drawdown | 0.9878 |
| cagr | -0.8774 |
| net_avg_win | 20.4306 |
| net_avg_loss | -34.1177 |
| avg_hold_time_bars | 3.1705 |
| exposure | 0.1448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
