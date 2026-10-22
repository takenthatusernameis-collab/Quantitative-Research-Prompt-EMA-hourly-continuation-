# EMA Hourly Continuation — PIXEL/USDT P20_89

**Symbol:** PIXEL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.7184 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9946 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -2.8717 |
| sortino_ratio | -1.0532 |
| max_drawdown | 0.7331 |
| cagr | -0.3933 |
| net_avg_win | 55.0704 |
| net_avg_loss | -73.5516 |
| avg_hold_time_bars | 14.0782 |
| exposure | 0.4319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
