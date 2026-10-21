# EMA Hourly Continuation — ATH/USDT P21_50

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.8375 |
| net_win_rate | 0.5177 |
| gross_profit_factor | 1.0765 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -1.1368 |
| sortino_ratio | -0.3362 |
| max_drawdown | 0.3402 |
| cagr | -0.1448 |
| net_avg_win | 77.4953 |
| net_avg_loss | -99.3105 |
| avg_hold_time_bars | 7.8662 |
| exposure | 0.1510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
