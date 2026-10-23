# EMA Hourly Continuation — BIGTIME/USDT P21_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1111 |
| net_profit_factor | 0.4511 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.8564 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -8.8833 |
| sortino_ratio | -4.1824 |
| max_drawdown | 0.9945 |
| cagr | -0.8716 |
| net_avg_win | 16.8160 |
| net_avg_loss | -28.9860 |
| avg_hold_time_bars | 3.2286 |
| exposure | 0.1623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
