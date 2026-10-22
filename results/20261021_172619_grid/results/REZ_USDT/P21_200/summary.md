# EMA Hourly Continuation — REZ/USDT P21_200

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 1.0411 |
| net_win_rate | 0.5523 |
| gross_profit_factor | 1.2191 |
| gross_win_rate | 0.5523 |
| sharpe_ratio | 0.3131 |
| sortino_ratio | 0.0850 |
| max_drawdown | 0.1784 |
| cagr | 0.0305 |
| net_avg_win | 102.8324 |
| net_avg_loss | -121.8659 |
| avg_hold_time_bars | 37.6599 |
| exposure | 0.5977 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
