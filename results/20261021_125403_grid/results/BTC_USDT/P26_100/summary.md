# EMA Hourly Continuation — BTC/USDT P26_100

**Symbol:** BTC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6435 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0152 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -2.7576 |
| sortino_ratio | -0.7878 |
| max_drawdown | 0.6478 |
| cagr | -0.3030 |
| net_avg_win | 51.1352 |
| net_avg_loss | -81.2557 |
| avg_hold_time_bars | 19.4610 |
| exposure | 0.3495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
