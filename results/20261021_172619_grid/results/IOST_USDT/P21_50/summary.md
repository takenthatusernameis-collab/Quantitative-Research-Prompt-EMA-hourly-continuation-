# EMA Hourly Continuation — IOST/USDT P21_50

**Symbol:** IOST/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.6574 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9690 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -3.1703 |
| sortino_ratio | -1.0879 |
| max_drawdown | 0.7218 |
| cagr | -0.3929 |
| net_avg_win | 48.6065 |
| net_avg_loss | -72.1492 |
| avg_hold_time_bars | 7.4518 |
| exposure | 0.1934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
