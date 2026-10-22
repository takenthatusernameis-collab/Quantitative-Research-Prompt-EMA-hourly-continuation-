# EMA Hourly Continuation — ALPINE/USDT P8_34

**Symbol:** ALPINE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1141 |
| net_profit_factor | 0.4311 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.7278 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -9.0461 |
| sortino_ratio | -4.3053 |
| max_drawdown | 0.9951 |
| cagr | -0.8789 |
| net_avg_win | 15.9418 |
| net_avg_loss | -26.1836 |
| avg_hold_time_bars | 7.2594 |
| exposure | 0.3765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
