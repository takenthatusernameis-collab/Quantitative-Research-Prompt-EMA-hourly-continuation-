# EMA Hourly Continuation — VELO/USDT P89_100

**Symbol:** VELO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 97 |
| net_profit_factor | 0.8923 |
| net_win_rate | 0.5361 |
| gross_profit_factor | 1.1465 |
| gross_win_rate | 0.5361 |
| sharpe_ratio | -0.3283 |
| sortino_ratio | -0.0468 |
| max_drawdown | 0.1013 |
| cagr | -0.0220 |
| net_avg_win | 86.7372 |
| net_avg_loss | -112.3304 |
| avg_hold_time_bars | 7.2577 |
| exposure | 0.0320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
