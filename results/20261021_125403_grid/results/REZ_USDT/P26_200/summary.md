# EMA Hourly Continuation — REZ/USDT P26_200

**Symbol:** REZ/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.9978 |
| net_win_rate | 0.5418 |
| gross_profit_factor | 1.1711 |
| gross_win_rate | 0.5418 |
| sharpe_ratio | 0.0435 |
| sortino_ratio | 0.0114 |
| max_drawdown | 0.2018 |
| cagr | -0.0016 |
| net_avg_win | 100.3645 |
| net_avg_loss | -118.9403 |
| avg_hold_time_bars | 38.8638 |
| exposure | 0.5791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
