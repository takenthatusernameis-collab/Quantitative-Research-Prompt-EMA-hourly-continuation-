# EMA Hourly Continuation — GMX/USDT P20_144

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6621 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8247 |
| gross_win_rate | 0.4447 |
| sharpe_ratio | -3.1253 |
| sortino_ratio | -0.9853 |
| max_drawdown | 0.6973 |
| cagr | -0.3658 |
| net_avg_win | 60.4068 |
| net_avg_loss | -73.0573 |
| avg_hold_time_bars | 21.8249 |
| exposure | 0.4930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
