# EMA Hourly Continuation — MOCA/USDT P55_100

**Symbol:** MOCA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.6996 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9336 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -2.1333 |
| sortino_ratio | -0.5729 |
| max_drawdown | 0.4734 |
| cagr | -0.2314 |
| net_avg_win | 67.7513 |
| net_avg_loss | -90.9679 |
| avg_hold_time_bars | 8.0531 |
| exposure | 0.1292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
