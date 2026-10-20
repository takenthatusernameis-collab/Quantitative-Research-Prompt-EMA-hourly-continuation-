# EMA Hourly Continuation — XPR/USDT P50_100

**Symbol:** XPR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.3339 |
| net_win_rate | 0.3880 |
| gross_profit_factor | 0.6520 |
| gross_win_rate | 0.3994 |
| sharpe_ratio | -8.1495 |
| sortino_ratio | -2.8946 |
| max_drawdown | 0.9735 |
| cagr | -0.7637 |
| net_avg_win | 20.4122 |
| net_avg_loss | -38.7571 |
| avg_hold_time_bars | 5.5552 |
| exposure | 0.1555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
