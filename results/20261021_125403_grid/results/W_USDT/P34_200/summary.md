# EMA Hourly Continuation — W/USDT P34_200

**Symbol:** W/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 1.0929 |
| net_win_rate | 0.5616 |
| gross_profit_factor | 1.2718 |
| gross_win_rate | 0.5616 |
| sharpe_ratio | 0.5580 |
| sortino_ratio | 0.1390 |
| max_drawdown | 0.1651 |
| cagr | 0.0558 |
| net_avg_win | 104.7774 |
| net_avg_loss | -122.8374 |
| avg_hold_time_bars | 38.9384 |
| exposure | 0.5168 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
