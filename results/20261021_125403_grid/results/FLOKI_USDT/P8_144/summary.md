# EMA Hourly Continuation — FLOKI/USDT P8_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8832 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0332 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -0.7246 |
| sortino_ratio | -0.1981 |
| max_drawdown | 0.3454 |
| cagr | -0.0903 |
| net_avg_win | 86.4539 |
| net_avg_loss | -101.7394 |
| avg_hold_time_bars | 44.9559 |
| exposure | 0.7418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
