# EMA Hourly Continuation — CWEB/USDT P8_50

**Symbol:** CWEB/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.4867 |
| net_win_rate | 0.3948 |
| gross_profit_factor | 0.8724 |
| gross_win_rate | 0.4043 |
| sharpe_ratio | -8.8751 |
| sortino_ratio | -3.6226 |
| max_drawdown | 0.9913 |
| cagr | -0.8471 |
| net_avg_win | 28.1314 |
| net_avg_loss | -37.7077 |
| avg_hold_time_bars | 14.5366 |
| exposure | 0.5590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
