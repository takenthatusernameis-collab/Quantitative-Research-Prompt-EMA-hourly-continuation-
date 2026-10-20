# EMA Hourly Continuation — RIO/USDT P26_34

**Symbol:** RIO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1135 |
| net_profit_factor | 0.2598 |
| net_win_rate | 0.3427 |
| gross_profit_factor | 0.5008 |
| gross_win_rate | 0.3568 |
| sharpe_ratio | -12.7551 |
| sortino_ratio | -6.1478 |
| max_drawdown | 0.9996 |
| cagr | -0.9582 |
| net_avg_win | 9.0198 |
| net_avg_loss | -18.1032 |
| avg_hold_time_bars | 2.1330 |
| exposure | 0.1111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
