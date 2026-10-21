# EMA Hourly Continuation — BAT/USDT P26_50

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.6305 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9545 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -3.4374 |
| sortino_ratio | -1.1573 |
| max_drawdown | 0.7475 |
| cagr | -0.4115 |
| net_avg_win | 47.0363 |
| net_avg_loss | -70.1320 |
| avg_hold_time_bars | 5.7078 |
| exposure | 0.1430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
