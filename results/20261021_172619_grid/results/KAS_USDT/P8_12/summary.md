# EMA Hourly Continuation — KAS/USDT P8_12

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 172 |
| net_profit_factor | 0.8596 |
| net_win_rate | 0.5465 |
| gross_profit_factor | 1.2095 |
| gross_win_rate | 0.5465 |
| sharpe_ratio | -0.6389 |
| sortino_ratio | -0.1217 |
| max_drawdown | 0.2422 |
| cagr | -0.0546 |
| net_avg_win | 85.6132 |
| net_avg_loss | -120.0217 |
| avg_hold_time_bars | 5.3953 |
| exposure | 0.0422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
