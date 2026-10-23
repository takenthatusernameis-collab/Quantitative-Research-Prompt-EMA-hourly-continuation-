# EMA Hourly Continuation — DYDX/USDT P20_34

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.4550 |
| net_win_rate | 0.4359 |
| gross_profit_factor | 1.0297 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -9.6658 |
| sortino_ratio | -4.6694 |
| max_drawdown | 0.9974 |
| cagr | -0.9056 |
| net_avg_win | 16.2331 |
| net_avg_loss | -27.5617 |
| avg_hold_time_bars | 2.5990 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
