# EMA Hourly Continuation — EIGEN/USDT P26_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7690 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 1.0161 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7944 |
| sortino_ratio | -0.5251 |
| max_drawdown | 0.4485 |
| cagr | -0.2189 |
| net_avg_win | 76.9505 |
| net_avg_loss | -97.7894 |
| avg_hold_time_bars | 26.7299 |
| exposure | 0.5176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
