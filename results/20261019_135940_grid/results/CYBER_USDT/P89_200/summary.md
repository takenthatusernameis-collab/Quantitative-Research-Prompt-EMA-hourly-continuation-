# EMA Hourly Continuation — CYBER/USDT P89_200

**Symbol:** CYBER/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.5734 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8462 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -3.0052 |
| sortino_ratio | -0.8061 |
| max_drawdown | 0.6148 |
| cagr | -0.3161 |
| net_avg_win | 50.3969 |
| net_avg_loss | -73.5358 |
| avg_hold_time_bars | 13.8722 |
| exposure | 0.2270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
