# EMA Hourly Continuation — SSV/USDT P12_100

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.5948 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -4.5441 |
| sortino_ratio | -1.6396 |
| max_drawdown | 0.8772 |
| cagr | -0.5438 |
| net_avg_win | 42.8952 |
| net_avg_loss | -57.3397 |
| avg_hold_time_bars | 19.6381 |
| exposure | 0.5918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
