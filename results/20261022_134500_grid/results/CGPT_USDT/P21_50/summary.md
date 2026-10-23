# EMA Hourly Continuation — CGPT/USDT P21_50

**Symbol:** CGPT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.5124 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.8693 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -6.9822 |
| sortino_ratio | -2.9648 |
| max_drawdown | 0.9746 |
| cagr | -0.7663 |
| net_avg_win | 25.6535 |
| net_avg_loss | -39.1689 |
| avg_hold_time_bars | 4.7723 |
| exposure | 0.1972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
