# EMA Hourly Continuation — FIDA/USDT P26_50

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 917 |
| net_profit_factor | 0.4409 |
| net_win_rate | 0.4340 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -7.6515 |
| sortino_ratio | -3.2614 |
| max_drawdown | 0.9834 |
| cagr | -0.8004 |
| net_avg_win | 19.4755 |
| net_avg_loss | -33.8721 |
| avg_hold_time_bars | 4.6031 |
| exposure | 0.1910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
