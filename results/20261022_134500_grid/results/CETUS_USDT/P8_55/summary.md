# EMA Hourly Continuation — CETUS/USDT P8_55

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1018 |
| net_profit_factor | 0.6651 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9920 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -5.1552 |
| sortino_ratio | -2.3075 |
| max_drawdown | 0.9430 |
| cagr | -0.6689 |
| net_avg_win | 39.1596 |
| net_avg_loss | -51.7063 |
| avg_hold_time_bars | 10.7210 |
| exposure | 0.4939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
