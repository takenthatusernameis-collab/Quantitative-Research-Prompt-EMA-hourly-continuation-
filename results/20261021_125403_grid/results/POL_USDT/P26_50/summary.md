# EMA Hourly Continuation — POL/USDT P26_50

**Symbol:** POL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6067 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8555 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -2.8065 |
| sortino_ratio | -0.7869 |
| max_drawdown | 0.6006 |
| cagr | -0.3024 |
| net_avg_win | 50.7117 |
| net_avg_loss | -74.5325 |
| avg_hold_time_bars | 7.0234 |
| exposure | 0.1226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
