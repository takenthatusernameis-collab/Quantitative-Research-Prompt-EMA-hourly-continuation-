# EMA Hourly Continuation — DYDX/USDT P12_21

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1462 |
| net_profit_factor | 0.3028 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.7873 |
| gross_win_rate | 0.4364 |
| sharpe_ratio | -12.4102 |
| sortino_ratio | -6.7639 |
| max_drawdown | 0.9998 |
| cagr | -0.9668 |
| net_avg_win | 7.1899 |
| net_avg_loss | -16.7142 |
| avg_hold_time_bars | 2.3509 |
| exposure | 0.1562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
