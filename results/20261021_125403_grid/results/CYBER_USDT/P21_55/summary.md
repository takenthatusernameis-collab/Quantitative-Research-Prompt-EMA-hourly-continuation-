# EMA Hourly Continuation — CYBER/USDT P21_55

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6348 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8440 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -3.6576 |
| sortino_ratio | -1.2570 |
| max_drawdown | 0.7734 |
| cagr | -0.4393 |
| net_avg_win | 50.2432 |
| net_avg_loss | -65.9598 |
| avg_hold_time_bars | 8.9691 |
| exposure | 0.2377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
