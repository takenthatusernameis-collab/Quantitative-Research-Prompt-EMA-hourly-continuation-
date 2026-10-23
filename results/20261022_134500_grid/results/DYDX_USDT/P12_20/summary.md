# EMA Hourly Continuation — DYDX/USDT P12_20

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1466 |
| net_profit_factor | 0.2791 |
| net_win_rate | 0.4079 |
| gross_profit_factor | 0.7604 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -12.8497 |
| sortino_ratio | -7.0134 |
| max_drawdown | 0.9999 |
| cagr | -0.9719 |
| net_avg_win | 6.4738 |
| net_avg_loss | -15.9793 |
| avg_hold_time_bars | 2.2483 |
| exposure | 0.1498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
