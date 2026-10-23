# EMA Hourly Continuation — VELO/USDT P20_100

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 733 |
| net_profit_factor | 0.7208 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9994 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.7908 |
| sortino_ratio | -1.0672 |
| max_drawdown | 0.7659 |
| cagr | -0.3971 |
| net_avg_win | 50.8811 |
| net_avg_loss | -70.0138 |
| avg_hold_time_bars | 12.4789 |
| exposure | 0.4158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
