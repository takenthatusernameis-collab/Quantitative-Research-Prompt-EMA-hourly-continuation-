# EMA Hourly Continuation — SQD/USDT P55_89

**Symbol:** SQD/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6508 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 1.0713 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -4.1061 |
| sortino_ratio | -1.4398 |
| max_drawdown | 0.8262 |
| cagr | -0.5075 |
| net_avg_win | 51.1608 |
| net_avg_loss | -75.3414 |
| avg_hold_time_bars | 4.3617 |
| exposure | 0.1253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
