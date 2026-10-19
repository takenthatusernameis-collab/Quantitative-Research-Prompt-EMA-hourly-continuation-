# EMA Hourly Continuation — SAND/USDT P26_50

**Symbol:** SAND/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 885 |
| net_profit_factor | 0.4405 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.8911 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -8.1790 |
| sortino_ratio | -3.4397 |
| max_drawdown | 0.9870 |
| cagr | -0.8197 |
| net_avg_win | 20.0718 |
| net_avg_loss | -35.4063 |
| avg_hold_time_bars | 3.9367 |
| exposure | 0.1584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
