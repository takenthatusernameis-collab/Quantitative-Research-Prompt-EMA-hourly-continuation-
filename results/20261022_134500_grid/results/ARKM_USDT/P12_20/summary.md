# EMA Hourly Continuation — ARKM/USDT P12_20

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1517 |
| net_profit_factor | 0.3433 |
| net_win_rate | 0.3902 |
| gross_profit_factor | 0.6753 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -13.3532 |
| sortino_ratio | -7.3728 |
| max_drawdown | 0.9999 |
| cagr | -0.9768 |
| net_avg_win | 8.8308 |
| net_avg_loss | -16.4617 |
| avg_hold_time_bars | 2.1365 |
| exposure | 0.1473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
