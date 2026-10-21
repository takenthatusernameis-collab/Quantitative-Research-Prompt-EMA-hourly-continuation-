# EMA Hourly Continuation — REZ/USDT P50_200

**Symbol:** REZ/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 1.0225 |
| net_win_rate | 0.5508 |
| gross_profit_factor | 1.2150 |
| gross_win_rate | 0.5508 |
| sharpe_ratio | 0.1801 |
| sortino_ratio | 0.0459 |
| max_drawdown | 0.1706 |
| cagr | 0.0140 |
| net_avg_win | 94.4539 |
| net_avg_loss | -113.2789 |
| avg_hold_time_bars | 29.6164 |
| exposure | 0.4167 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
