# EMA Hourly Continuation — CVX/USDT P26_50

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 933 |
| net_profit_factor | 0.4195 |
| net_win_rate | 0.4330 |
| gross_profit_factor | 0.7577 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -7.6094 |
| sortino_ratio | -3.2830 |
| max_drawdown | 0.9827 |
| cagr | -0.7999 |
| net_avg_win | 17.5756 |
| net_avg_loss | -31.9939 |
| avg_hold_time_bars | 3.8307 |
| exposure | 0.1625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
