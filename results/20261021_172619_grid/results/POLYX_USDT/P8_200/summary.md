# EMA Hourly Continuation — POLYX/USDT P8_200

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.9062 |
| net_win_rate | 0.5240 |
| gross_profit_factor | 1.0836 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -0.4809 |
| sortino_ratio | -0.1181 |
| max_drawdown | 0.2022 |
| cagr | -0.0561 |
| net_avg_win | 85.1807 |
| net_avg_loss | -103.4665 |
| avg_hold_time_bars | 59.7740 |
| exposure | 0.7934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
