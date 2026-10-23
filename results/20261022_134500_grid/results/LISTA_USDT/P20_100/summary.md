# EMA Hourly Continuation — LISTA/USDT P20_100

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.7002 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9797 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -2.9879 |
| sortino_ratio | -1.0381 |
| max_drawdown | 0.6864 |
| cagr | -0.3877 |
| net_avg_win | 58.5365 |
| net_avg_loss | -78.1439 |
| avg_hold_time_bars | 16.3286 |
| exposure | 0.4495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
