# EMA Hourly Continuation — T/USDT P26_34

**Symbol:** T/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.3114 |
| net_win_rate | 0.3780 |
| gross_profit_factor | 0.7981 |
| gross_win_rate | 0.4336 |
| sharpe_ratio | -10.8993 |
| sortino_ratio | -4.5302 |
| max_drawdown | 0.9976 |
| cagr | -0.9087 |
| net_avg_win | 14.1409 |
| net_avg_loss | -27.5944 |
| avg_hold_time_bars | 3.5995 |
| exposure | 0.1375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
