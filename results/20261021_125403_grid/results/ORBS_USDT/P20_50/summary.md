# EMA Hourly Continuation — ORBS/USDT P20_50

**Symbol:** ORBS/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.5485 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.8141 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -5.0183 |
| sortino_ratio | -1.7023 |
| max_drawdown | 0.8653 |
| cagr | -0.5437 |
| net_avg_win | 43.0307 |
| net_avg_loss | -59.0160 |
| avg_hold_time_bars | 9.2509 |
| exposure | 0.2380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
