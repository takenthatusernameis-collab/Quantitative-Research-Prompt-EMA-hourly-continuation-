# EMA Hourly Continuation — CETUS/USDT P50_200

**Symbol:** CETUS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8088 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0773 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -1.2559 |
| sortino_ratio | -0.3283 |
| max_drawdown | 0.3436 |
| cagr | -0.1459 |
| net_avg_win | 78.4626 |
| net_avg_loss | -104.0645 |
| avg_hold_time_bars | 28.6813 |
| exposure | 0.4439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
