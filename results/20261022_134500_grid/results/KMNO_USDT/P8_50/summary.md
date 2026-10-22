# EMA Hourly Continuation — KMNO/USDT P8_50

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.6039 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.9114 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -5.3511 |
| sortino_ratio | -2.3254 |
| max_drawdown | 0.9360 |
| cagr | -0.6711 |
| net_avg_win | 33.0372 |
| net_avg_loss | -46.7040 |
| avg_hold_time_bars | 10.4819 |
| exposure | 0.4539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
