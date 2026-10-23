# EMA Hourly Continuation — AEVO/USDT P8_100

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.7310 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9964 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.6824 |
| sortino_ratio | -0.8975 |
| max_drawdown | 0.6832 |
| cagr | -0.3474 |
| net_avg_win | 64.6701 |
| net_avg_loss | -84.5031 |
| avg_hold_time_bars | 27.9206 |
| exposure | 0.7164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
