# EMA Hourly Continuation — ASTR/USDT P8_34

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 834 |
| net_profit_factor | 0.6682 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -3.7491 |
| sortino_ratio | -1.5422 |
| max_drawdown | 0.8335 |
| cagr | -0.5087 |
| net_avg_win | 41.5396 |
| net_avg_loss | -58.4109 |
| avg_hold_time_bars | 8.4436 |
| exposure | 0.3187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
