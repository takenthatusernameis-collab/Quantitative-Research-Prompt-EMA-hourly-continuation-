# EMA Hourly Continuation — SHIB/USDT P34_55

**Symbol:** SHIB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6689 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9896 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.2103 |
| sortino_ratio | -0.5193 |
| max_drawdown | 0.4947 |
| cagr | -0.2113 |
| net_avg_win | 69.2657 |
| net_avg_loss | -99.7418 |
| avg_hold_time_bars | 6.0524 |
| exposure | 0.0735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
