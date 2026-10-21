# EMA Hourly Continuation — DOGS/USDT P20_26

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 110 |
| net_profit_factor | 0.5149 |
| net_win_rate | 0.4091 |
| gross_profit_factor | 0.6740 |
| gross_win_rate | 0.4091 |
| sharpe_ratio | -2.2310 |
| sortino_ratio | -0.3581 |
| max_drawdown | 0.3186 |
| cagr | -0.1521 |
| net_avg_win | 70.4602 |
| net_avg_loss | -94.7426 |
| avg_hold_time_bars | 4.5636 |
| exposure | 0.0266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
