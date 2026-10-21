# EMA Hourly Continuation — MERL/USDT P20_144

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.8375 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9621 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -1.1825 |
| sortino_ratio | -0.3197 |
| max_drawdown | 0.4285 |
| cagr | -0.1387 |
| net_avg_win | 92.4473 |
| net_avg_loss | -103.8160 |
| avg_hold_time_bars | 33.6295 |
| exposure | 0.5503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
