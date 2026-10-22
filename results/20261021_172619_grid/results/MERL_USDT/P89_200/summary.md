# EMA Hourly Continuation — MERL/USDT P89_200

**Symbol:** MERL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.7047 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8403 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -1.8950 |
| sortino_ratio | -0.4395 |
| max_drawdown | 0.4236 |
| cagr | -0.1839 |
| net_avg_win | 78.6578 |
| net_avg_loss | -92.5094 |
| avg_hold_time_bars | 15.9476 |
| exposure | 0.1941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
