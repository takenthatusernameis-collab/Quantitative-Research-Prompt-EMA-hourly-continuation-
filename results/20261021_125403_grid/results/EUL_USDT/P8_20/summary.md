# EMA Hourly Continuation — EUL/USDT P8_20

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6338 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -3.1634 |
| sortino_ratio | -1.1019 |
| max_drawdown | 0.7397 |
| cagr | -0.3967 |
| net_avg_win | 43.9615 |
| net_avg_loss | -63.1188 |
| avg_hold_time_bars | 7.3098 |
| exposure | 0.1974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
