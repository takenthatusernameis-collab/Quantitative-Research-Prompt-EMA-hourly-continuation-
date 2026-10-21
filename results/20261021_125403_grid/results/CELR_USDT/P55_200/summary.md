# EMA Hourly Continuation — CELR/USDT P55_200

**Symbol:** CELR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7163 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8694 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -1.6868 |
| sortino_ratio | -0.4168 |
| max_drawdown | 0.4031 |
| cagr | -0.1751 |
| net_avg_win | 67.9052 |
| net_avg_loss | -84.7270 |
| avg_hold_time_bars | 29.7954 |
| exposure | 0.4085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
