# EMA Hourly Continuation — KSM/USDT P26_50

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 908 |
| net_profit_factor | 0.4455 |
| net_win_rate | 0.4383 |
| gross_profit_factor | 0.8464 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -7.9854 |
| sortino_ratio | -3.4276 |
| max_drawdown | 0.9852 |
| cagr | -0.8118 |
| net_avg_win | 19.8787 |
| net_avg_loss | -34.8253 |
| avg_hold_time_bars | 4.4956 |
| exposure | 0.1855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
