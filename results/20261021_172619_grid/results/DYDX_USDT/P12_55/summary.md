# EMA Hourly Continuation — DYDX/USDT P12_55

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.7614 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.2325 |
| sortino_ratio | -0.7667 |
| max_drawdown | 0.6243 |
| cagr | -0.2973 |
| net_avg_win | 66.9651 |
| net_avg_loss | -82.0898 |
| avg_hold_time_bars | 14.6431 |
| exposure | 0.3860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
