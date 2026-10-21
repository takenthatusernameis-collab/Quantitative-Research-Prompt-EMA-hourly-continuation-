# EMA Hourly Continuation — BABYDOGE/USDT P21_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 52 |
| net_profit_factor | 1.0826 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1563 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | 0.2003 |
| sortino_ratio | 0.0209 |
| max_drawdown | 0.0523 |
| cagr | 0.0081 |
| net_avg_win | 96.0180 |
| net_avg_loss | -103.4702 |
| avg_hold_time_bars | 59.2115 |
| exposure | 0.1393 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
