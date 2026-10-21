# EMA Hourly Continuation — RENDER/USDT P100_200

**Symbol:** RENDER/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.9165 |
| net_win_rate | 0.5355 |
| gross_profit_factor | 1.1402 |
| gross_win_rate | 0.5355 |
| sharpe_ratio | -0.3859 |
| sortino_ratio | -0.0873 |
| max_drawdown | 0.2018 |
| cagr | -0.0423 |
| net_avg_win | 86.7599 |
| net_avg_loss | -109.1553 |
| avg_hold_time_bars | 15.2986 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
