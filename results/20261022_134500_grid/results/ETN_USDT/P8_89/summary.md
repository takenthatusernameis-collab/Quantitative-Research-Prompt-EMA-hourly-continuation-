# EMA Hourly Continuation — ETN/USDT P8_89

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 834 |
| net_profit_factor | 0.3285 |
| net_win_rate | 0.3381 |
| gross_profit_factor | 0.4711 |
| gross_win_rate | 0.3525 |
| sharpe_ratio | -10.1294 |
| sortino_ratio | -4.4748 |
| max_drawdown | 0.9906 |
| cagr | -0.8901 |
| net_avg_win | 17.1815 |
| net_avg_loss | -26.7184 |
| avg_hold_time_bars | 11.8777 |
| exposure | 0.5381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
