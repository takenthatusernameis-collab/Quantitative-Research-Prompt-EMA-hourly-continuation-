# EMA Hourly Continuation — POL/USDT P21_100

**Symbol:** POL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8143 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0423 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -1.1682 |
| sortino_ratio | -0.3406 |
| max_drawdown | 0.4177 |
| cagr | -0.1465 |
| net_avg_win | 67.8639 |
| net_avg_loss | -88.3435 |
| avg_hold_time_bars | 25.2306 |
| exposure | 0.4725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
