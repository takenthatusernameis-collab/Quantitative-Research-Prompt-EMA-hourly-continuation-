# EMA Hourly Continuation — RENDER/USDT P20_26

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.2658 |
| net_win_rate | 0.3583 |
| gross_profit_factor | 0.6529 |
| gross_win_rate | 0.4039 |
| sharpe_ratio | -13.9184 |
| sortino_ratio | -6.9210 |
| max_drawdown | 0.9997 |
| cagr | -0.9754 |
| net_avg_win | 9.8081 |
| net_avg_loss | -20.5989 |
| avg_hold_time_bars | 2.0553 |
| exposure | 0.1117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
