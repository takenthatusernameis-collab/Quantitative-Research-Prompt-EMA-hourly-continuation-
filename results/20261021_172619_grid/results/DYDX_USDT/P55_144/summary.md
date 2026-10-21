# EMA Hourly Continuation — DYDX/USDT P55_144

**Symbol:** DYDX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7729 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9724 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -1.5752 |
| sortino_ratio | -0.4262 |
| max_drawdown | 0.4534 |
| cagr | -0.1785 |
| net_avg_win | 75.3801 |
| net_avg_loss | -94.3081 |
| avg_hold_time_bars | 14.4050 |
| exposure | 0.2344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
