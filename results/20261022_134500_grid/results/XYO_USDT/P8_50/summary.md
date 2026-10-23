# EMA Hourly Continuation — XYO/USDT P8_50

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1283 |
| net_profit_factor | 0.4434 |
| net_win_rate | 0.4022 |
| gross_profit_factor | 0.8001 |
| gross_win_rate | 0.4217 |
| sharpe_ratio | -10.0833 |
| sortino_ratio | -5.0703 |
| max_drawdown | 0.9982 |
| cagr | -0.9184 |
| net_avg_win | 15.4095 |
| net_avg_loss | -23.3811 |
| avg_hold_time_bars | 7.6033 |
| exposure | 0.4414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
