# EMA Hourly Continuation — DOGS/USDT P20_144

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.9364 |
| net_win_rate | 0.5285 |
| gross_profit_factor | 1.1093 |
| gross_win_rate | 0.5285 |
| sharpe_ratio | -0.3464 |
| sortino_ratio | -0.0985 |
| max_drawdown | 0.1681 |
| cagr | -0.0495 |
| net_avg_win | 86.5402 |
| net_avg_loss | -103.6052 |
| avg_hold_time_bars | 30.7447 |
| exposure | 0.5431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
