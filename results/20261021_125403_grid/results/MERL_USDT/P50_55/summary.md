# EMA Hourly Continuation — MERL/USDT P50_55

**Symbol:** MERL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 153 |
| net_profit_factor | 0.5905 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.7907 |
| gross_win_rate | 0.4379 |
| sharpe_ratio | -2.0963 |
| sortino_ratio | -0.3690 |
| max_drawdown | 0.3645 |
| cagr | -0.1566 |
| net_avg_win | 74.7468 |
| net_avg_loss | -98.6187 |
| avg_hold_time_bars | 4.7124 |
| exposure | 0.0329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
