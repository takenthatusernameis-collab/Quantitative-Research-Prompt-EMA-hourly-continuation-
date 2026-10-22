# EMA Hourly Continuation — BLUR/USDT P20_100

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.8743 |
| net_win_rate | 0.5198 |
| gross_profit_factor | 1.0884 |
| gross_win_rate | 0.5198 |
| sharpe_ratio | -0.9746 |
| sortino_ratio | -0.2977 |
| max_drawdown | 0.4617 |
| cagr | -0.1310 |
| net_avg_win | 87.9004 |
| net_avg_loss | -108.8413 |
| avg_hold_time_bars | 22.0947 |
| exposure | 0.4539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
