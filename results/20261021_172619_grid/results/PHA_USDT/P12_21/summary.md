# EMA Hourly Continuation — PHA/USDT P12_21

**Symbol:** PHA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7526 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0061 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.9021 |
| sortino_ratio | -0.5209 |
| max_drawdown | 0.5087 |
| cagr | -0.2126 |
| net_avg_win | 76.2807 |
| net_avg_loss | -98.6162 |
| avg_hold_time_bars | 5.2986 |
| exposure | 0.0879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
