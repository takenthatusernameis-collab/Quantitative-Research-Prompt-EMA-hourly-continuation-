# EMA Hourly Continuation — LSK/USDT P8_50

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.6652 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 1.0637 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -4.6898 |
| sortino_ratio | -2.0310 |
| max_drawdown | 0.9128 |
| cagr | -0.6166 |
| net_avg_win | 40.0065 |
| net_avg_loss | -56.3949 |
| avg_hold_time_bars | 10.3929 |
| exposure | 0.4412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
