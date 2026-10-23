# EMA Hourly Continuation — BLZ/USDT P100_144

**Symbol:** BLZ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.5141 |
| net_win_rate | 0.4185 |
| gross_profit_factor | 0.8809 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -6.2463 |
| sortino_ratio | -2.0732 |
| max_drawdown | 0.9244 |
| cagr | -0.6385 |
| net_avg_win | 42.2855 |
| net_avg_loss | -59.1893 |
| avg_hold_time_bars | 5.8297 |
| exposure | 0.1456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
