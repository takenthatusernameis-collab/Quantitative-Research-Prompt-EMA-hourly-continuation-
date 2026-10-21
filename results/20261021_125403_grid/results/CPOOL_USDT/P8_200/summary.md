# EMA Hourly Continuation — CPOOL/USDT P8_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7646 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8576 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -1.6632 |
| sortino_ratio | -0.4674 |
| max_drawdown | 0.4769 |
| cagr | -0.1952 |
| net_avg_win | 74.6306 |
| net_avg_loss | -84.6523 |
| avg_hold_time_bars | 40.2817 |
| exposure | 0.7214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
