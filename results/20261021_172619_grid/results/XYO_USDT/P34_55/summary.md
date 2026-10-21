# EMA Hourly Continuation — XYO/USDT P34_55

**Symbol:** XYO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.5098 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.7490 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -4.2370 |
| sortino_ratio | -1.1123 |
| max_drawdown | 0.7325 |
| cagr | -0.4034 |
| net_avg_win | 54.0985 |
| net_avg_loss | -74.6531 |
| avg_hold_time_bars | 6.6726 |
| exposure | 0.1024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
