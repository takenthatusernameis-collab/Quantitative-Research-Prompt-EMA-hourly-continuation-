# EMA Hourly Continuation — AAVE/USDT P8_200

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7342 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 1.0111 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.8215 |
| sortino_ratio | -0.4815 |
| max_drawdown | 0.4840 |
| cagr | -0.2056 |
| net_avg_win | 69.2982 |
| net_avg_loss | -92.7923 |
| avg_hold_time_bars | 49.6006 |
| exposure | 0.7959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
