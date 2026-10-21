# EMA Hourly Continuation — POL/USDT P8_200

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 1.1216 |
| net_win_rate | 0.5685 |
| gross_profit_factor | 1.3067 |
| gross_win_rate | 0.5685 |
| sharpe_ratio | 0.6051 |
| sortino_ratio | 0.1375 |
| max_drawdown | 0.1532 |
| cagr | 0.0557 |
| net_avg_win | 98.2478 |
| net_avg_loss | -115.3886 |
| avg_hold_time_bars | 74.6266 |
| exposure | 0.8175 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
