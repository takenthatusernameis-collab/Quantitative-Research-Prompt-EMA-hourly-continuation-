# EMA Hourly Continuation — MERL/USDT P8_26

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1542 |
| net_profit_factor | 0.5289 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.7932 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -7.4717 |
| sortino_ratio | -4.1242 |
| max_drawdown | 0.9935 |
| cagr | -0.8640 |
| net_avg_win | 15.7718 |
| net_avg_loss | -25.2492 |
| avg_hold_time_bars | 3.9948 |
| exposure | 0.2808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
