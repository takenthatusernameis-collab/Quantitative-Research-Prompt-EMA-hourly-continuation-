# EMA Hourly Continuation — DYDX/USDT P21_200

**Symbol:** DYDX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.7060 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9826 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.9049 |
| sortino_ratio | -0.5298 |
| max_drawdown | 0.4995 |
| cagr | -0.2233 |
| net_avg_win | 57.8650 |
| net_avg_loss | -81.9611 |
| avg_hold_time_bars | 36.4179 |
| exposure | 0.6456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
