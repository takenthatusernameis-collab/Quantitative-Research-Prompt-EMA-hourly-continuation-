# EMA Hourly Continuation — TURBO/USDT P34_144

**Symbol:** TURBO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.9553 |
| net_win_rate | 0.5359 |
| gross_profit_factor | 1.1501 |
| gross_win_rate | 0.5359 |
| sharpe_ratio | -0.2481 |
| sortino_ratio | -0.0718 |
| max_drawdown | 0.2486 |
| cagr | -0.0385 |
| net_avg_win | 94.2206 |
| net_avg_loss | -113.9001 |
| avg_hold_time_bars | 19.8473 |
| exposure | 0.3616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
