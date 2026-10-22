# EMA Hourly Continuation — CYBER/USDT P89_200

**Symbol:** CYBER/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7263 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9177 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.5747 |
| sortino_ratio | -0.3769 |
| max_drawdown | 0.3534 |
| cagr | -0.1594 |
| net_avg_win | 68.9610 |
| net_avg_loss | -89.0505 |
| avg_hold_time_bars | 17.2064 |
| exposure | 0.2198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
