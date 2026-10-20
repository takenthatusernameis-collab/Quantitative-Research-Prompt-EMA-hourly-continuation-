# EMA Hourly Continuation — GALA/USDT P89_100

**Symbol:** GALA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.3181 |
| net_win_rate | 0.3821 |
| gross_profit_factor | 0.8786 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -9.3452 |
| sortino_ratio | -3.3705 |
| max_drawdown | 0.9876 |
| cagr | -0.8257 |
| net_avg_win | 19.6053 |
| net_avg_loss | -38.1129 |
| avg_hold_time_bars | 2.1073 |
| exposure | 0.0589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
