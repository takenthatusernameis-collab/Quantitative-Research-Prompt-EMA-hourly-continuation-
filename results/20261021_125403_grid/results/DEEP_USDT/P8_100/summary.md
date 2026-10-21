# EMA Hourly Continuation — DEEP/USDT P8_100

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.9107 |
| net_win_rate | 0.5120 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -0.5507 |
| sortino_ratio | -0.1610 |
| max_drawdown | 0.2610 |
| cagr | -0.0762 |
| net_avg_win | 88.0884 |
| net_avg_loss | -101.4764 |
| avg_hold_time_bars | 35.9401 |
| exposure | 0.6797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
