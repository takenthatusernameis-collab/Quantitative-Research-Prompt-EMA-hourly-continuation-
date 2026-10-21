# EMA Hourly Continuation — DYDX/USDT P34_55

**Symbol:** DYDX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6473 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -2.5602 |
| sortino_ratio | -0.6692 |
| max_drawdown | 0.5640 |
| cagr | -0.2644 |
| net_avg_win | 63.2413 |
| net_avg_loss | -84.6687 |
| avg_hold_time_bars | 5.6756 |
| exposure | 0.0867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
