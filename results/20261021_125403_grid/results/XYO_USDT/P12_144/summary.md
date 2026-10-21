# EMA Hourly Continuation — XYO/USDT P12_144

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5770 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.7270 |
| gross_win_rate | 0.4204 |
| sharpe_ratio | -3.8109 |
| sortino_ratio | -1.1412 |
| max_drawdown | 0.7485 |
| cagr | -0.4115 |
| net_avg_win | 52.9549 |
| net_avg_loss | -66.5498 |
| avg_hold_time_bars | 29.9580 |
| exposure | 0.6127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
