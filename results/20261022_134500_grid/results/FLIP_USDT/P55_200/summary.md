# EMA Hourly Continuation — FLIP/USDT P55_200

**Symbol:** FLIP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.5336 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.7917 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -3.2039 |
| sortino_ratio | -0.7500 |
| max_drawdown | 0.6094 |
| cagr | -0.3029 |
| net_avg_win | 56.3575 |
| net_avg_loss | -80.8769 |
| avg_hold_time_bars | 28.0824 |
| exposure | 0.3561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
