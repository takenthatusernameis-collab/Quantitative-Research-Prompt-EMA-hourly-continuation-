# EMA Hourly Continuation — ETC/USDT P12_100

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.5566 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.9485 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -4.9891 |
| sortino_ratio | -1.8436 |
| max_drawdown | 0.8971 |
| cagr | -0.5873 |
| net_avg_win | 34.6542 |
| net_avg_loss | -55.0963 |
| avg_hold_time_bars | 17.2456 |
| exposure | 0.5393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
