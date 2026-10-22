# EMA Hourly Continuation — XMR/USDT P26_100

**Symbol:** XMR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.4008 |
| net_win_rate | 0.4206 |
| gross_profit_factor | 0.7914 |
| gross_win_rate | 0.4325 |
| sharpe_ratio | -8.7004 |
| sortino_ratio | -3.8890 |
| max_drawdown | 0.9924 |
| cagr | -0.8555 |
| net_avg_win | 15.6560 |
| net_avg_loss | -28.3571 |
| avg_hold_time_bars | 6.5288 |
| exposure | 0.2991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
