# EMA Hourly Continuation — DEXE/USDT P26_144

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.9355 |
| net_win_rate | 0.5329 |
| gross_profit_factor | 1.1194 |
| gross_win_rate | 0.5329 |
| sharpe_ratio | -0.2878 |
| sortino_ratio | -0.0705 |
| max_drawdown | 0.2075 |
| cagr | -0.0360 |
| net_avg_win | 82.7577 |
| net_avg_loss | -100.9174 |
| avg_hold_time_bars | 46.9896 |
| exposure | 0.6173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
