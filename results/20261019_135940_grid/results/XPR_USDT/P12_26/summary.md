# EMA Hourly Continuation — XPR/USDT P12_26

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1299 |
| net_profit_factor | 0.2948 |
| net_win_rate | 0.3634 |
| gross_profit_factor | 0.7059 |
| gross_win_rate | 0.3849 |
| sharpe_ratio | -14.6131 |
| sortino_ratio | -7.5537 |
| max_drawdown | 1.0000 |
| cagr | -0.9832 |
| net_avg_win | 8.8576 |
| net_avg_loss | -17.1468 |
| avg_hold_time_bars | 2.6859 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
