# EMA Hourly Continuation — PEPE/USDT P21_100

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7861 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -1.5279 |
| sortino_ratio | -0.4255 |
| max_drawdown | 0.3961 |
| cagr | -0.1786 |
| net_avg_win | 77.4493 |
| net_avg_loss | -92.9953 |
| avg_hold_time_bars | 24.3780 |
| exposure | 0.4222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
