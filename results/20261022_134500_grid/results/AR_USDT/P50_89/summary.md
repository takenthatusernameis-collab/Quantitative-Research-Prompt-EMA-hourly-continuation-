# EMA Hourly Continuation — AR/USDT P50_89

**Symbol:** AR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.4913 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8099 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -5.0672 |
| sortino_ratio | -1.8667 |
| max_drawdown | 0.8970 |
| cagr | -0.5950 |
| net_avg_win | 27.1431 |
| net_avg_loss | -47.7645 |
| avg_hold_time_bars | 4.4491 |
| exposure | 0.1391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
