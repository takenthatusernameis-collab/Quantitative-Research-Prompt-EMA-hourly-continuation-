# EMA Hourly Continuation — SYN/USDT P8_20

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1574 |
| net_profit_factor | 0.4447 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.8032 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -9.7729 |
| sortino_ratio | -5.4621 |
| max_drawdown | 0.9988 |
| cagr | -0.9309 |
| net_avg_win | 11.7130 |
| net_avg_loss | -20.1883 |
| avg_hold_time_bars | 3.3170 |
| exposure | 0.2373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
