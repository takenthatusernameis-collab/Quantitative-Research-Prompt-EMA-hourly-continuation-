# EMA Hourly Continuation — NMR/USDT P12_50

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1171 |
| net_profit_factor | 0.6127 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -7.2497 |
| sortino_ratio | -3.4957 |
| max_drawdown | 0.9865 |
| cagr | -0.8158 |
| net_avg_win | 29.1989 |
| net_avg_loss | -39.9519 |
| avg_hold_time_bars | 6.4039 |
| exposure | 0.3409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
