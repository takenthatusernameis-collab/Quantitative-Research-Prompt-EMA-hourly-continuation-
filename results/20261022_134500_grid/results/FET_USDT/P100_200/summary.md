# EMA Hourly Continuation — FET/USDT P100_200

**Symbol:** FET/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.8167 |
| net_win_rate | 0.5306 |
| gross_profit_factor | 1.1648 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -1.3249 |
| sortino_ratio | -0.3600 |
| max_drawdown | 0.4299 |
| cagr | -0.1546 |
| net_avg_win | 80.2677 |
| net_avg_loss | -111.0728 |
| avg_hold_time_bars | 9.1139 |
| exposure | 0.1491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
