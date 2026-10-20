# EMA Hourly Continuation — YGG/USDT P26_100

**Symbol:** YGG/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.7034 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 1.0396 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -3.3248 |
| sortino_ratio | -1.2277 |
| max_drawdown | 0.7771 |
| cagr | -0.4425 |
| net_avg_win | 54.0807 |
| net_avg_loss | -74.0415 |
| avg_hold_time_bars | 10.9216 |
| exposure | 0.3405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
