# EMA Hourly Continuation — CFG/USDT P89_100

**Symbol:** CFG/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.2619 |
| net_win_rate | 0.3651 |
| gross_profit_factor | 0.6509 |
| gross_win_rate | 0.3816 |
| sharpe_ratio | -9.1385 |
| sortino_ratio | -3.2452 |
| max_drawdown | 0.9848 |
| cagr | -0.8099 |
| net_avg_win | 15.7374 |
| net_avg_loss | -34.5571 |
| avg_hold_time_bars | 2.1530 |
| exposure | 0.0595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
