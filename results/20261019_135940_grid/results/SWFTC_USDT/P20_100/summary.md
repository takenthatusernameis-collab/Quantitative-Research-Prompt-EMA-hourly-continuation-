# EMA Hourly Continuation — SWFTC/USDT P20_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.4830 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7485 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -6.0753 |
| sortino_ratio | -2.2333 |
| max_drawdown | 0.9369 |
| cagr | -0.6652 |
| net_avg_win | 29.9441 |
| net_avg_loss | -45.9473 |
| avg_hold_time_bars | 12.6851 |
| exposure | 0.3955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
