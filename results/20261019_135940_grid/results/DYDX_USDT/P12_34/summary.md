# EMA Hourly Continuation — DYDX/USDT P12_34

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1262 |
| net_profit_factor | 0.5481 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 1.0595 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -8.0377 |
| sortino_ratio | -3.9912 |
| max_drawdown | 0.9932 |
| cagr | -0.8623 |
| net_avg_win | 20.8043 |
| net_avg_loss | -32.1770 |
| avg_hold_time_bars | 4.2773 |
| exposure | 0.2454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
