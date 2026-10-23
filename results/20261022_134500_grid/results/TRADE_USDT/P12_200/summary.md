# EMA Hourly Continuation — TRADE/USDT P12_200

**Symbol:** TRADE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6486 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.7963 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -2.5008 |
| sortino_ratio | -0.6473 |
| max_drawdown | 0.5587 |
| cagr | -0.2608 |
| net_avg_win | 65.4601 |
| net_avg_loss | -80.9514 |
| avg_hold_time_bars | 45.9199 |
| exposure | 0.7034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
