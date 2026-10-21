# EMA Hourly Continuation — DEXE/USDT P34_100

**Symbol:** DEXE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.8112 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0312 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -1.0936 |
| sortino_ratio | -0.2960 |
| max_drawdown | 0.3823 |
| cagr | -0.1287 |
| net_avg_win | 68.6682 |
| net_avg_loss | -89.5446 |
| avg_hold_time_bars | 26.3427 |
| exposure | 0.4263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
