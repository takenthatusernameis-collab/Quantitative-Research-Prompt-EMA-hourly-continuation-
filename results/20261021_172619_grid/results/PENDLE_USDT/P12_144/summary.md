# EMA Hourly Continuation — PENDLE/USDT P12_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8239 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9485 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -1.1116 |
| sortino_ratio | -0.2958 |
| max_drawdown | 0.3595 |
| cagr | -0.1290 |
| net_avg_win | 80.6343 |
| net_avg_loss | -93.4749 |
| avg_hold_time_bars | 41.9713 |
| exposure | 0.6639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
