# EMA Hourly Continuation — CYBER/USDT P26_50

**Symbol:** CYBER/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 894 |
| net_profit_factor | 0.5073 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.9204 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -7.6986 |
| sortino_ratio | -3.2405 |
| max_drawdown | 0.9828 |
| cagr | -0.8008 |
| net_avg_win | 25.8145 |
| net_avg_loss | -39.7318 |
| avg_hold_time_bars | 4.9340 |
| exposure | 0.2005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
