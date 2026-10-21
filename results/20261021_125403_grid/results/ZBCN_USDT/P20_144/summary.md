# EMA Hourly Continuation — ZBCN/USDT P20_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 1.0355 |
| net_win_rate | 0.5470 |
| gross_profit_factor | 1.1888 |
| gross_win_rate | 0.5470 |
| sharpe_ratio | 0.3056 |
| sortino_ratio | 0.0911 |
| max_drawdown | 0.2661 |
| cagr | 0.0317 |
| net_avg_win | 102.7424 |
| net_avg_loss | -119.8032 |
| avg_hold_time_bars | 24.7855 |
| exposure | 0.4759 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
