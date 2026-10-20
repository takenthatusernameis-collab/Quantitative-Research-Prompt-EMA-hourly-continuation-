# EMA Hourly Continuation — SAFE/USDT P8_144

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.6073 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8489 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -3.2860 |
| sortino_ratio | -1.0430 |
| max_drawdown | 0.7218 |
| cagr | -0.3958 |
| net_avg_win | 46.4667 |
| net_avg_loss | -66.2197 |
| avg_hold_time_bars | 30.7446 |
| exposure | 0.7223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
