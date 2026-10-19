# EMA Hourly Continuation — ZBCN/USDT P20_50

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.5837 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9397 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -6.4117 |
| sortino_ratio | -2.9843 |
| max_drawdown | 0.9748 |
| cagr | -0.7733 |
| net_avg_win | 26.6252 |
| net_avg_loss | -40.0718 |
| avg_hold_time_bars | 3.7931 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
