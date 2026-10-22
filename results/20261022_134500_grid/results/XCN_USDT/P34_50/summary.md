# EMA Hourly Continuation — XCN/USDT P34_50

**Symbol:** XCN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1095 |
| net_profit_factor | 0.2401 |
| net_win_rate | 0.3379 |
| gross_profit_factor | 0.6767 |
| gross_win_rate | 0.3726 |
| sharpe_ratio | -13.5836 |
| sortino_ratio | -6.4880 |
| max_drawdown | 0.9998 |
| cagr | -0.9671 |
| net_avg_win | 8.5392 |
| net_avg_loss | -18.1485 |
| avg_hold_time_bars | 2.6365 |
| exposure | 0.1312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
