# EMA Hourly Continuation — UMA/USDT P8_55

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.7489 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9892 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -2.7069 |
| sortino_ratio | -1.0559 |
| max_drawdown | 0.7127 |
| cagr | -0.3849 |
| net_avg_win | 57.1393 |
| net_avg_loss | -74.6711 |
| avg_hold_time_bars | 13.3145 |
| exposure | 0.4503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
