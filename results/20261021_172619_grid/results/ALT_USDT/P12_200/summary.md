# EMA Hourly Continuation — ALT/USDT P12_200

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7839 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -1.3329 |
| sortino_ratio | -0.3381 |
| max_drawdown | 0.3640 |
| cagr | -0.1459 |
| net_avg_win | 77.0401 |
| net_avg_loss | -92.8471 |
| avg_hold_time_bars | 51.2145 |
| exposure | 0.7380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
