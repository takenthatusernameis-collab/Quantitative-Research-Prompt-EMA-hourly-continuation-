# EMA Hourly Continuation — ZIL/USDT P8_50

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1060 |
| net_profit_factor | 0.5349 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -6.0587 |
| sortino_ratio | -2.7699 |
| max_drawdown | 0.9705 |
| cagr | -0.7404 |
| net_avg_win | 22.0072 |
| net_avg_loss | -37.4334 |
| avg_hold_time_bars | 9.9604 |
| exposure | 0.4799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
