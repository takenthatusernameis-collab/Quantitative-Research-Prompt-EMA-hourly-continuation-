# EMA Hourly Continuation — LUNC/USDT P50_200

**Symbol:** LUNC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5872 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.9027 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.5395 |
| sortino_ratio | -1.0370 |
| max_drawdown | 0.7315 |
| cagr | -0.3967 |
| net_avg_win | 49.6480 |
| net_avg_loss | -75.3952 |
| avg_hold_time_bars | 19.0526 |
| exposure | 0.3785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
