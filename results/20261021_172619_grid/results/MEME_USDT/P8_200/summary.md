# EMA Hourly Continuation — MEME/USDT P8_200

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.8507 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0104 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -0.8831 |
| sortino_ratio | -0.2168 |
| max_drawdown | 0.3114 |
| cagr | -0.0968 |
| net_avg_win | 86.8971 |
| net_avg_loss | -102.8430 |
| avg_hold_time_bars | 59.6441 |
| exposure | 0.7998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
