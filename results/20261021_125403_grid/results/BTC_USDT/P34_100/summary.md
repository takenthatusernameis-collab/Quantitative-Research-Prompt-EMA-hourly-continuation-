# EMA Hourly Continuation — BTC/USDT P34_100

**Symbol:** BTC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.5855 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9539 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -3.2101 |
| sortino_ratio | -0.8790 |
| max_drawdown | 0.6901 |
| cagr | -0.3329 |
| net_avg_win | 47.8972 |
| net_avg_loss | -78.3200 |
| avg_hold_time_bars | 16.2397 |
| exposure | 0.2683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
