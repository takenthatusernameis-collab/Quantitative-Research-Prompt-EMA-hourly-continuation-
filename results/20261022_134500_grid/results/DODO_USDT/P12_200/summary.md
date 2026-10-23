# EMA Hourly Continuation — DODO/USDT P12_200

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.4990 |
| net_win_rate | 0.4125 |
| gross_profit_factor | 0.7237 |
| gross_win_rate | 0.4183 |
| sharpe_ratio | -4.9214 |
| sortino_ratio | -1.5751 |
| max_drawdown | 0.8595 |
| cagr | -0.5301 |
| net_avg_win | 39.0706 |
| net_avg_loss | -54.9841 |
| avg_hold_time_bars | 28.1692 |
| exposure | 0.6705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
