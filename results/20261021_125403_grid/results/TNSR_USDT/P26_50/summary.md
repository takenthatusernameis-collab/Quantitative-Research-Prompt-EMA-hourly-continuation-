# EMA Hourly Continuation — TNSR/USDT P26_50

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7418 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9919 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -2.2365 |
| sortino_ratio | -0.6992 |
| max_drawdown | 0.5886 |
| cagr | -0.2743 |
| net_avg_win | 67.2351 |
| net_avg_loss | -89.1301 |
| avg_hold_time_bars | 6.3473 |
| exposure | 0.1373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
