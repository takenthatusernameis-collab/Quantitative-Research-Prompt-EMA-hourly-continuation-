# EMA Hourly Continuation — BDX/USDT P89_200

**Symbol:** BDX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.4922 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8060 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.4987 |
| sortino_ratio | -0.8834 |
| max_drawdown | 0.6480 |
| cagr | -0.3321 |
| net_avg_win | 43.4925 |
| net_avg_loss | -75.1332 |
| avg_hold_time_bars | 11.2557 |
| exposure | 0.1581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
