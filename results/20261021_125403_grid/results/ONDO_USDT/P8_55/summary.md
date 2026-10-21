# EMA Hourly Continuation — ONDO/USDT P8_55

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.8703 |
| net_win_rate | 0.5157 |
| gross_profit_factor | 1.0608 |
| gross_win_rate | 0.5157 |
| sharpe_ratio | -1.1016 |
| sortino_ratio | -0.3994 |
| max_drawdown | 0.4252 |
| cagr | -0.1716 |
| net_avg_win | 77.1001 |
| net_avg_loss | -94.3386 |
| avg_hold_time_bars | 14.6525 |
| exposure | 0.4236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
