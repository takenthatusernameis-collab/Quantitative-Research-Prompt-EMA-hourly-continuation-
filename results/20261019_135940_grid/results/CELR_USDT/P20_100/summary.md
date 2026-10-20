# EMA Hourly Continuation — CELR/USDT P20_100

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.5973 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8844 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.9840 |
| sortino_ratio | -1.3981 |
| max_drawdown | 0.8155 |
| cagr | -0.4829 |
| net_avg_win | 42.1907 |
| net_avg_loss | -60.2708 |
| avg_hold_time_bars | 16.9079 |
| exposure | 0.4736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
