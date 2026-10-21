# EMA Hourly Continuation — MERL/USDT P21_89

**Symbol:** MERL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7640 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9017 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -1.9503 |
| sortino_ratio | -0.6070 |
| max_drawdown | 0.5420 |
| cagr | -0.2445 |
| net_avg_win | 72.5780 |
| net_avg_loss | -84.4885 |
| avg_hold_time_bars | 16.9958 |
| exposure | 0.3703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
