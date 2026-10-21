# EMA Hourly Continuation — MLK/USDT P34_50

**Symbol:** MLK/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.2997 |
| net_win_rate | 0.3294 |
| gross_profit_factor | 0.5229 |
| gross_win_rate | 0.3412 |
| sharpe_ratio | -5.4505 |
| sortino_ratio | -1.2440 |
| max_drawdown | 0.7793 |
| cagr | -0.4439 |
| net_avg_win | 39.3469 |
| net_avg_loss | -64.4968 |
| avg_hold_time_bars | 6.0902 |
| exposure | 0.0703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
