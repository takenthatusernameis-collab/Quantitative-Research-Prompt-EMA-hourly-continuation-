# EMA Hourly Continuation — BOME/USDT P26_50

**Symbol:** BOME/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.8233 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -1.0620 |
| sortino_ratio | -0.2986 |
| max_drawdown | 0.3617 |
| cagr | -0.1296 |
| net_avg_win | 69.2369 |
| net_avg_loss | -90.9902 |
| avg_hold_time_bars | 6.0420 |
| exposure | 0.1046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
