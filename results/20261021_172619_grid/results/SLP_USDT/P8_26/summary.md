# EMA Hourly Continuation — SLP/USDT P8_26

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.7108 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9691 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -3.1374 |
| sortino_ratio | -1.2510 |
| max_drawdown | 0.7657 |
| cagr | -0.4355 |
| net_avg_win | 49.4095 |
| net_avg_loss | -66.7010 |
| avg_hold_time_bars | 5.7067 |
| exposure | 0.2008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
