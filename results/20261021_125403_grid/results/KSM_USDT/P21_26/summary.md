# EMA Hourly Continuation — KSM/USDT P21_26

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.5407 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8179 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -2.6952 |
| sortino_ratio | -0.5571 |
| max_drawdown | 0.4716 |
| cagr | -0.2243 |
| net_avg_win | 59.0532 |
| net_avg_loss | -90.0623 |
| avg_hold_time_bars | 4.2452 |
| exposure | 0.0401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
