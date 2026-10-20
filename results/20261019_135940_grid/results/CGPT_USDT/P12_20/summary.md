# EMA Hourly Continuation — CGPT/USDT P12_20

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1428 |
| net_profit_factor | 0.3098 |
| net_win_rate | 0.3929 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4237 |
| sharpe_ratio | -13.5431 |
| sortino_ratio | -7.3011 |
| max_drawdown | 0.9999 |
| cagr | -0.9773 |
| net_avg_win | 8.0022 |
| net_avg_loss | -16.7110 |
| avg_hold_time_bars | 2.2423 |
| exposure | 0.1455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
