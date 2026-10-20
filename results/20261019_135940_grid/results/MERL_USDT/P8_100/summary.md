# EMA Hourly Continuation — MERL/USDT P8_100

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.7905 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 1.0174 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -2.0197 |
| sortino_ratio | -0.7065 |
| max_drawdown | 0.6360 |
| cagr | -0.2846 |
| net_avg_win | 70.9298 |
| net_avg_loss | -88.2688 |
| avg_hold_time_bars | 24.8391 |
| exposure | 0.6895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
