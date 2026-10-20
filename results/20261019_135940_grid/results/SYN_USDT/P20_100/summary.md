# EMA Hourly Continuation — SYN/USDT P20_100

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.7089 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 1.0043 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.8582 |
| sortino_ratio | -1.0191 |
| max_drawdown | 0.7162 |
| cagr | -0.3841 |
| net_avg_win | 55.1276 |
| net_avg_loss | -73.9587 |
| avg_hold_time_bars | 15.1395 |
| exposure | 0.4390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
