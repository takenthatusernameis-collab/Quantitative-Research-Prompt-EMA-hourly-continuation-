# EMA Hourly Continuation — ORBS/USDT P21_55

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.5672 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.8346 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -4.8307 |
| sortino_ratio | -1.6374 |
| max_drawdown | 0.8578 |
| cagr | -0.5314 |
| net_avg_win | 45.1436 |
| net_avg_loss | -61.4383 |
| avg_hold_time_bars | 9.6596 |
| exposure | 0.2490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
