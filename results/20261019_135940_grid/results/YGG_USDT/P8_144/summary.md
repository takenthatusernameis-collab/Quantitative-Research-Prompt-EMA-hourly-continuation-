# EMA Hourly Continuation — YGG/USDT P8_144

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.7050 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9637 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -2.6833 |
| sortino_ratio | -0.8819 |
| max_drawdown | 0.6674 |
| cagr | -0.3399 |
| net_avg_win | 59.4363 |
| net_avg_loss | -78.0333 |
| avg_hold_time_bars | 29.5396 |
| exposure | 0.7258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
