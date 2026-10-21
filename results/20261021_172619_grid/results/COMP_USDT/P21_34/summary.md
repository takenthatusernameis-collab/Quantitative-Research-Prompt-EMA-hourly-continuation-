# EMA Hourly Continuation — COMP/USDT P21_34

**Symbol:** COMP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.5996 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 0.9248 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -2.9218 |
| sortino_ratio | -0.8568 |
| max_drawdown | 0.6705 |
| cagr | -0.3243 |
| net_avg_win | 45.3050 |
| net_avg_loss | -74.8388 |
| avg_hold_time_bars | 4.9495 |
| exposure | 0.0936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
