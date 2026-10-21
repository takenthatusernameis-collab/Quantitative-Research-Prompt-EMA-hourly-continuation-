# EMA Hourly Continuation — REQ/USDT P26_100

**Symbol:** REQ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6435 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -3.3348 |
| sortino_ratio | -1.0613 |
| max_drawdown | 0.7121 |
| cagr | -0.3863 |
| net_avg_win | 54.2825 |
| net_avg_loss | -75.6583 |
| avg_hold_time_bars | 14.9879 |
| exposure | 0.3386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
