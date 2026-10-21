# EMA Hourly Continuation — DEEP/USDT P50_100

**Symbol:** DEEP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8785 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0812 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.7485 |
| sortino_ratio | -0.2041 |
| max_drawdown | 0.2427 |
| cagr | -0.0924 |
| net_avg_win | 85.6056 |
| net_avg_loss | -105.9201 |
| avg_hold_time_bars | 9.0903 |
| exposure | 0.1482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
