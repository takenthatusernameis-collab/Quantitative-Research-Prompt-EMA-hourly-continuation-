# EMA Hourly Continuation — PENDLE/USDT P20_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6281 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9123 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -3.1220 |
| sortino_ratio | -0.9741 |
| max_drawdown | 0.7192 |
| cagr | -0.3742 |
| net_avg_win | 49.9377 |
| net_avg_loss | -70.7367 |
| avg_hold_time_bars | 25.8229 |
| exposure | 0.5834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
