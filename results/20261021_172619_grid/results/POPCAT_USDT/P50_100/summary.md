# EMA Hourly Continuation — POPCAT/USDT P50_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7568 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -1.8634 |
| sortino_ratio | -0.5449 |
| max_drawdown | 0.4608 |
| cagr | -0.2223 |
| net_avg_win | 74.9711 |
| net_avg_loss | -91.6875 |
| avg_hold_time_bars | 9.2320 |
| exposure | 0.1765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
