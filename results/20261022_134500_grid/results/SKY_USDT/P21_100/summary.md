# EMA Hourly Continuation — SKY/USDT P21_100

**Symbol:** SKY/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.6821 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0453 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -3.2729 |
| sortino_ratio | -1.1298 |
| max_drawdown | 0.7566 |
| cagr | -0.4211 |
| net_avg_win | 58.2694 |
| net_avg_loss | -85.4215 |
| avg_hold_time_bars | 16.9940 |
| exposure | 0.4700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
