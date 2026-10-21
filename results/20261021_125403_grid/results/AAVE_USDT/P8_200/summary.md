# EMA Hourly Continuation — AAVE/USDT P8_200

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.9598 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1185 |
| gross_win_rate | 0.5316 |
| sharpe_ratio | -0.1562 |
| sortino_ratio | -0.0369 |
| max_drawdown | 0.2038 |
| cagr | -0.0212 |
| net_avg_win | 87.5294 |
| net_avg_loss | -103.5048 |
| avg_hold_time_bars | 64.6840 |
| exposure | 0.7909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
