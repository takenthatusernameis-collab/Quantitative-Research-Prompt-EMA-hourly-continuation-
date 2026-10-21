# EMA Hourly Continuation — SYN/USDT P34_55

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.6951 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -2.2473 |
| sortino_ratio | -0.6390 |
| max_drawdown | 0.5628 |
| cagr | -0.2540 |
| net_avg_win | 62.1625 |
| net_avg_loss | -83.7343 |
| avg_hold_time_bars | 6.0886 |
| exposure | 0.1093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
