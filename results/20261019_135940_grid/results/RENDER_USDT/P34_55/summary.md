# EMA Hourly Continuation — RENDER/USDT P34_55

**Symbol:** RENDER/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.4298 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.7898 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -8.4729 |
| sortino_ratio | -3.6810 |
| max_drawdown | 0.9822 |
| cagr | -0.8396 |
| net_avg_win | 21.2448 |
| net_avg_loss | -37.2343 |
| avg_hold_time_bars | 2.9235 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
