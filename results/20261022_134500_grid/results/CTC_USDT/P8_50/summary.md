# EMA Hourly Continuation — CTC/USDT P8_50

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1144 |
| net_profit_factor | 0.5165 |
| net_win_rate | 0.4441 |
| gross_profit_factor | 0.9338 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -7.4977 |
| sortino_ratio | -3.5480 |
| max_drawdown | 0.9885 |
| cagr | -0.8282 |
| net_avg_win | 20.7802 |
| net_avg_loss | -32.1326 |
| avg_hold_time_bars | 9.0629 |
| exposure | 0.4713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
