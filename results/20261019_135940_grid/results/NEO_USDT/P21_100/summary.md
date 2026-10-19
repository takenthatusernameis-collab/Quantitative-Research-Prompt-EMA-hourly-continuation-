# EMA Hourly Continuation — NEO/USDT P21_100

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.5432 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8663 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -4.7881 |
| sortino_ratio | -1.6909 |
| max_drawdown | 0.8705 |
| cagr | -0.5523 |
| net_avg_win | 36.4374 |
| net_avg_loss | -55.6671 |
| avg_hold_time_bars | 15.6154 |
| exposure | 0.4429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
