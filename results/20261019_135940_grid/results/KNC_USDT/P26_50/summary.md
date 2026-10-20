# EMA Hourly Continuation — KNC/USDT P26_50

**Symbol:** KNC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 874 |
| net_profit_factor | 0.4721 |
| net_win_rate | 0.4428 |
| gross_profit_factor | 0.9395 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -7.9056 |
| sortino_ratio | -3.3100 |
| max_drawdown | 0.9844 |
| cagr | -0.8070 |
| net_avg_win | 22.7360 |
| net_avg_loss | -38.2713 |
| avg_hold_time_bars | 5.0515 |
| exposure | 0.2007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
