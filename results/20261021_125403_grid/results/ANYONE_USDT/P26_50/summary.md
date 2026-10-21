# EMA Hourly Continuation — ANYONE/USDT P26_50

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.5804 |
| net_win_rate | 0.4162 |
| gross_profit_factor | 0.7123 |
| gross_win_rate | 0.4162 |
| sharpe_ratio | -3.5345 |
| sortino_ratio | -1.0112 |
| max_drawdown | 0.6633 |
| cagr | -0.3747 |
| net_avg_win | 58.7266 |
| net_avg_loss | -72.1361 |
| avg_hold_time_bars | 7.1378 |
| exposure | 0.1335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
