# EMA Hourly Continuation — GMT/USDT P50_144

**Symbol:** GMT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.5904 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -4.0427 |
| sortino_ratio | -1.3056 |
| max_drawdown | 0.8076 |
| cagr | -0.4672 |
| net_avg_win | 46.1554 |
| net_avg_loss | -69.2468 |
| avg_hold_time_bars | 10.8693 |
| exposure | 0.2609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
