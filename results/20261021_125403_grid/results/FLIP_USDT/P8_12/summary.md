# EMA Hourly Continuation — FLIP/USDT P8_12

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.4634 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -6.5098 |
| sortino_ratio | -2.0300 |
| max_drawdown | 0.9250 |
| cagr | -0.6411 |
| net_avg_win | 39.4873 |
| net_avg_loss | -61.2594 |
| avg_hold_time_bars | 7.6315 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
