# EMA Hourly Continuation — FLOW/USDT P26_100

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.7518 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9579 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.9222 |
| sortino_ratio | -0.5848 |
| max_drawdown | 0.5083 |
| cagr | -0.2364 |
| net_avg_win | 67.1200 |
| net_avg_loss | -85.4324 |
| avg_hold_time_bars | 16.4802 |
| exposure | 0.3401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
