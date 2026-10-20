# EMA Hourly Continuation — ROSE/USDT P8_200

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8100 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0649 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -1.1337 |
| sortino_ratio | -0.2728 |
| max_drawdown | 0.3164 |
| cagr | -0.1217 |
| net_avg_win | 81.2101 |
| net_avg_loss | -103.0812 |
| avg_hold_time_bars | 64.4583 |
| exposure | 0.8438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
