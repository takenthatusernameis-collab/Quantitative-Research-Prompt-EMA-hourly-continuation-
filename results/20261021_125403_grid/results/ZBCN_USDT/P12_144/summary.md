# EMA Hourly Continuation — ZBCN/USDT P12_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 1.0709 |
| net_win_rate | 0.5549 |
| gross_profit_factor | 1.2224 |
| gross_win_rate | 0.5549 |
| sharpe_ratio | 0.5976 |
| sortino_ratio | 0.1927 |
| max_drawdown | 0.1953 |
| cagr | 0.0765 |
| net_avg_win | 112.3214 |
| net_avg_loss | -130.7372 |
| avg_hold_time_bars | 25.8530 |
| exposure | 0.5777 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
