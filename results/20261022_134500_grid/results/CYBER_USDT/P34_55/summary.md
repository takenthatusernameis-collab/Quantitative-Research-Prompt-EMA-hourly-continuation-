# EMA Hourly Continuation — CYBER/USDT P34_55

**Symbol:** CYBER/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 819 |
| net_profit_factor | 0.4910 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.9469 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -7.8112 |
| sortino_ratio | -3.1695 |
| max_drawdown | 0.9808 |
| cagr | -0.7920 |
| net_avg_win | 26.7264 |
| net_avg_loss | -41.4349 |
| avg_hold_time_bars | 4.2576 |
| exposure | 0.1585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
