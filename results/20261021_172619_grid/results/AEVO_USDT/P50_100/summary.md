# EMA Hourly Continuation — AEVO/USDT P50_100

**Symbol:** AEVO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7388 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9667 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.9385 |
| sortino_ratio | -0.5811 |
| max_drawdown | 0.5080 |
| cagr | -0.2344 |
| net_avg_win | 63.6092 |
| net_avg_loss | -84.5419 |
| avg_hold_time_bars | 8.1977 |
| exposure | 0.1632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
