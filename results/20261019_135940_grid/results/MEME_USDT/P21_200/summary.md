# EMA Hourly Continuation — MEME/USDT P21_200

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7939 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0728 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -1.3451 |
| sortino_ratio | -0.3613 |
| max_drawdown | 0.3806 |
| cagr | -0.1557 |
| net_avg_win | 74.0849 |
| net_avg_loss | -95.4403 |
| avg_hold_time_bars | 40.3399 |
| exposure | 0.6528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
