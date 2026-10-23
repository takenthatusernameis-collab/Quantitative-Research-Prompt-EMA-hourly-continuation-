# EMA Hourly Continuation — CELR/USDT P12_144

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -3.4294 |
| sortino_ratio | -1.0792 |
| max_drawdown | 0.7356 |
| cagr | -0.4010 |
| net_avg_win | 54.9612 |
| net_avg_loss | -71.4319 |
| avg_hold_time_bars | 29.0475 |
| exposure | 0.6638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
