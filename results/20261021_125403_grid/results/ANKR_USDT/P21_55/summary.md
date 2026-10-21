# EMA Hourly Continuation — ANKR/USDT P21_55

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6223 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8573 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -4.2958 |
| sortino_ratio | -1.5009 |
| max_drawdown | 0.8318 |
| cagr | -0.5009 |
| net_avg_win | 50.5530 |
| net_avg_loss | -65.6228 |
| avg_hold_time_bars | 8.6395 |
| exposure | 0.2364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
