# EMA Hourly Continuation — REZ/USDT P8_50

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1054 |
| net_profit_factor | 0.7178 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 1.0381 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -4.4473 |
| sortino_ratio | -2.0531 |
| max_drawdown | 0.9165 |
| cagr | -0.6243 |
| net_avg_win | 45.3540 |
| net_avg_loss | -59.4633 |
| avg_hold_time_bars | 9.5114 |
| exposure | 0.4625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
