# EMA Hourly Continuation — TRAC/USDT P89_144

**Symbol:** TRAC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.7863 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0366 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -1.2218 |
| sortino_ratio | -0.3017 |
| max_drawdown | 0.3009 |
| cagr | -0.1297 |
| net_avg_win | 71.7592 |
| net_avg_loss | -95.6955 |
| avg_hold_time_bars | 6.8712 |
| exposure | 0.0921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
