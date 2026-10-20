# EMA Hourly Continuation — EUL/USDT P26_100

**Symbol:** EUL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.5073 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.7470 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -4.7061 |
| sortino_ratio | -1.6202 |
| max_drawdown | 0.8631 |
| cagr | -0.5427 |
| net_avg_win | 33.2819 |
| net_avg_loss | -51.3264 |
| avg_hold_time_bars | 12.1700 |
| exposure | 0.3352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
