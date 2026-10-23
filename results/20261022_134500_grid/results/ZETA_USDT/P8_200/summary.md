# EMA Hourly Continuation — ZETA/USDT P8_200

**Symbol:** ZETA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7488 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 1.0114 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -1.6136 |
| sortino_ratio | -0.4002 |
| max_drawdown | 0.4625 |
| cagr | -0.1700 |
| net_avg_win | 73.5446 |
| net_avg_loss | -96.3150 |
| avg_hold_time_bars | 59.9283 |
| exposure | 0.8325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
