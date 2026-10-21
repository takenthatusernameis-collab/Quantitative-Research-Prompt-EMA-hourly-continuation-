# EMA Hourly Continuation — HBAR/USDT P8_50

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.8740 |
| net_win_rate | 0.5381 |
| gross_profit_factor | 1.1464 |
| gross_win_rate | 0.5381 |
| sharpe_ratio | -1.0778 |
| sortino_ratio | -0.4223 |
| max_drawdown | 0.4551 |
| cagr | -0.1805 |
| net_avg_win | 69.0621 |
| net_avg_loss | -92.0740 |
| avg_hold_time_bars | 11.5545 |
| exposure | 0.3855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
