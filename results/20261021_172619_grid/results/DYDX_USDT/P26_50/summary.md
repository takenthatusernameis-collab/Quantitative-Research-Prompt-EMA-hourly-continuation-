# EMA Hourly Continuation — DYDX/USDT P26_50

**Symbol:** DYDX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6703 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -2.5346 |
| sortino_ratio | -0.7264 |
| max_drawdown | 0.5809 |
| cagr | -0.2824 |
| net_avg_win | 60.1921 |
| net_avg_loss | -80.9024 |
| avg_hold_time_bars | 6.6873 |
| exposure | 0.1225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
