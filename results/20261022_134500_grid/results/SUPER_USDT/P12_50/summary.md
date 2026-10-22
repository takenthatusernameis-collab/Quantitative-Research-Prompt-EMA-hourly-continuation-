# EMA Hourly Continuation — SUPER/USDT P12_50

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.6114 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -5.3615 |
| sortino_ratio | -2.4789 |
| max_drawdown | 0.9495 |
| cagr | -0.6904 |
| net_avg_win | 29.5734 |
| net_avg_loss | -43.3017 |
| avg_hold_time_bars | 7.1612 |
| exposure | 0.3473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
