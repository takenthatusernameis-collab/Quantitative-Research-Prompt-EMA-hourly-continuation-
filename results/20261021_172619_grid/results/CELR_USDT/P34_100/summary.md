# EMA Hourly Continuation — CELR/USDT P34_100

**Symbol:** CELR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9585 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -1.9809 |
| sortino_ratio | -0.6264 |
| max_drawdown | 0.5290 |
| cagr | -0.2506 |
| net_avg_win | 65.1261 |
| net_avg_loss | -83.4600 |
| avg_hold_time_bars | 12.2485 |
| exposure | 0.2721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
