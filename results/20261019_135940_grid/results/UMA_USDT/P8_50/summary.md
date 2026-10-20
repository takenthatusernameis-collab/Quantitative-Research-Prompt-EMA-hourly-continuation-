# EMA Hourly Continuation — UMA/USDT P8_50

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.5230 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -6.9043 |
| sortino_ratio | -3.2551 |
| max_drawdown | 0.9811 |
| cagr | -0.7926 |
| net_avg_win | 21.2938 |
| net_avg_loss | -33.2700 |
| avg_hold_time_bars | 8.5441 |
| exposure | 0.4361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
