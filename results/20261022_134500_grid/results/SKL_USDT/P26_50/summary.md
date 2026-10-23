# EMA Hourly Continuation — SKL/USDT P26_50

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.4750 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8987 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -7.5345 |
| sortino_ratio | -3.3894 |
| max_drawdown | 0.9846 |
| cagr | -0.8059 |
| net_avg_win | 19.4330 |
| net_avg_loss | -34.1922 |
| avg_hold_time_bars | 3.9622 |
| exposure | 0.1812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
