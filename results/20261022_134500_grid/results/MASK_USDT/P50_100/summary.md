# EMA Hourly Continuation — MASK/USDT P50_100

**Symbol:** MASK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.4066 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.8080 |
| gross_win_rate | 0.4666 |
| sharpe_ratio | -6.5342 |
| sortino_ratio | -2.3525 |
| max_drawdown | 0.9517 |
| cagr | -0.6954 |
| net_avg_win | 22.2791 |
| net_avg_loss | -43.7164 |
| avg_hold_time_bars | 6.1900 |
| exposure | 0.1851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
