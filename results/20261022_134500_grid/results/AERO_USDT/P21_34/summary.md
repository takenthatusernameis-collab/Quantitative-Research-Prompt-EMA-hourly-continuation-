# EMA Hourly Continuation — AERO/USDT P21_34

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1031 |
| net_profit_factor | 0.2986 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.6057 |
| gross_win_rate | 0.4403 |
| sharpe_ratio | -9.4059 |
| sortino_ratio | -4.2910 |
| max_drawdown | 0.9956 |
| cagr | -0.8840 |
| net_avg_win | 9.6753 |
| net_avg_loss | -23.9343 |
| avg_hold_time_bars | 2.4306 |
| exposure | 0.1139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
