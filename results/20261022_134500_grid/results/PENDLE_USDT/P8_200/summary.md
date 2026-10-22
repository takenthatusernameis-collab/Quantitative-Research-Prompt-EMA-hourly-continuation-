# EMA Hourly Continuation — PENDLE/USDT P8_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.7724 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0242 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -1.4592 |
| sortino_ratio | -0.3739 |
| max_drawdown | 0.4306 |
| cagr | -0.1622 |
| net_avg_win | 74.2359 |
| net_avg_loss | -96.1110 |
| avg_hold_time_bars | 54.7012 |
| exposure | 0.8155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
