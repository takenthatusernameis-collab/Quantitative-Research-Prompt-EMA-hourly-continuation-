# EMA Hourly Continuation — RENDER/USDT P26_50

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.7395 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9873 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.8066 |
| sortino_ratio | -0.5020 |
| max_drawdown | 0.4328 |
| cagr | -0.2054 |
| net_avg_win | 68.6679 |
| net_avg_loss | -92.8576 |
| avg_hold_time_bars | 6.0000 |
| exposure | 0.1026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
