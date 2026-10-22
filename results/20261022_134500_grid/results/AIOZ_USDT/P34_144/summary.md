# EMA Hourly Continuation — AIOZ/USDT P34_144

**Symbol:** AIOZ/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.9286 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -3.7352 |
| sortino_ratio | -1.2128 |
| max_drawdown | 0.7787 |
| cagr | -0.4449 |
| net_avg_win | 54.4449 |
| net_avg_loss | -73.5529 |
| avg_hold_time_bars | 16.9963 |
| exposure | 0.4172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
