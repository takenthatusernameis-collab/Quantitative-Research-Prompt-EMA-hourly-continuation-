# EMA Hourly Continuation — BRETT/USDT P89_100

**Symbol:** BRETT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.3978 |
| net_win_rate | 0.4144 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -7.7694 |
| sortino_ratio | -2.7602 |
| max_drawdown | 0.9663 |
| cagr | -0.7590 |
| net_avg_win | 25.8310 |
| net_avg_loss | -45.9553 |
| avg_hold_time_bars | 1.9899 |
| exposure | 0.0571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
