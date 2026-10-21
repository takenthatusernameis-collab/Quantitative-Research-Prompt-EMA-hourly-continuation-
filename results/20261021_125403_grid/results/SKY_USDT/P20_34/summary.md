# EMA Hourly Continuation — SKY/USDT P20_34

**Symbol:** SKY/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5847 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -3.7243 |
| sortino_ratio | -1.1387 |
| max_drawdown | 0.6625 |
| cagr | -0.4065 |
| net_avg_win | 53.4059 |
| net_avg_loss | -79.8076 |
| avg_hold_time_bars | 5.1482 |
| exposure | 0.1065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
