# EMA Hourly Continuation — ZETA/USDT P12_144

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7588 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.0606 |
| gross_win_rate | 0.5141 |
| sharpe_ratio | -1.7451 |
| sortino_ratio | -0.4599 |
| max_drawdown | 0.5270 |
| cagr | -0.2000 |
| net_avg_win | 74.3855 |
| net_avg_loss | -103.7320 |
| avg_hold_time_bars | 47.0480 |
| exposure | 0.7537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
