# EMA Hourly Continuation — DYDX/USDT P21_200

**Symbol:** DYDX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.8270 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -0.9567 |
| sortino_ratio | -0.2352 |
| max_drawdown | 0.2917 |
| cagr | -0.1044 |
| net_avg_win | 78.6591 |
| net_avg_loss | -93.2093 |
| avg_hold_time_bars | 47.2054 |
| exposure | 0.6373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
