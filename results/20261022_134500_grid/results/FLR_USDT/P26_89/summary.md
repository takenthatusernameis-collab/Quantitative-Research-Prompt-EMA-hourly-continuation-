# EMA Hourly Continuation — FLR/USDT P26_89

**Symbol:** FLR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 855 |
| net_profit_factor | 0.4802 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.8688 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -7.1574 |
| sortino_ratio | -2.9381 |
| max_drawdown | 0.9743 |
| cagr | -0.7663 |
| net_avg_win | 24.4552 |
| net_avg_loss | -38.4802 |
| avg_hold_time_bars | 7.9123 |
| exposure | 0.3075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
