# EMA Hourly Continuation — UNI/USDT P8_100

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7964 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9609 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.5128 |
| sortino_ratio | -0.4686 |
| max_drawdown | 0.4712 |
| cagr | -0.1950 |
| net_avg_win | 70.8288 |
| net_avg_loss | -86.3310 |
| avg_hold_time_bars | 30.1168 |
| exposure | 0.6448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
