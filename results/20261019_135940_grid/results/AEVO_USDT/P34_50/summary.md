# EMA Hourly Continuation — AEVO/USDT P34_50

**Symbol:** AEVO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.3878 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.7585 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -8.1137 |
| sortino_ratio | -3.5652 |
| max_drawdown | 0.9878 |
| cagr | -0.8226 |
| net_avg_win | 14.9642 |
| net_avg_loss | -29.9771 |
| avg_hold_time_bars | 2.9644 |
| exposure | 0.1282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
