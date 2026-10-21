# EMA Hourly Continuation — DASH/USDT P26_100

**Symbol:** DASH/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7718 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0080 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.8140 |
| sortino_ratio | -0.5422 |
| max_drawdown | 0.5241 |
| cagr | -0.2208 |
| net_avg_win | 72.8873 |
| net_avg_loss | -92.7256 |
| avg_hold_time_bars | 15.9495 |
| exposure | 0.3161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
