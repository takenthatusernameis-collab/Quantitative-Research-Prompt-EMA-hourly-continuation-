# EMA Hourly Continuation — GALA/USDT P8_20

**Symbol:** GALA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6894 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.7669 |
| sortino_ratio | -0.8840 |
| max_drawdown | 0.6536 |
| cagr | -0.3333 |
| net_avg_win | 59.8140 |
| net_avg_loss | -78.1870 |
| avg_hold_time_bars | 5.5400 |
| exposure | 0.1259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
