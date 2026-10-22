# EMA Hourly Continuation — QI/USDT P8_50

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 733 |
| net_profit_factor | 0.7424 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -2.9699 |
| sortino_ratio | -1.1447 |
| max_drawdown | 0.7512 |
| cagr | -0.4093 |
| net_avg_win | 60.1620 |
| net_avg_loss | -74.8735 |
| avg_hold_time_bars | 12.8909 |
| exposure | 0.4276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
