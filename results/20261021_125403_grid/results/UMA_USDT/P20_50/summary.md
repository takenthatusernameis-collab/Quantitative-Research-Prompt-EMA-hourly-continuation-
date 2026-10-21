# EMA Hourly Continuation — UMA/USDT P20_50

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.6817 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -3.1039 |
| sortino_ratio | -1.0718 |
| max_drawdown | 0.7263 |
| cagr | -0.3898 |
| net_avg_win | 53.4200 |
| net_avg_loss | -74.6912 |
| avg_hold_time_bars | 8.3870 |
| exposure | 0.2226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
