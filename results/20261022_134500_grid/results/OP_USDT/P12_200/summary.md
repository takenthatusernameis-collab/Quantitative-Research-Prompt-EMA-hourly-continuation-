# EMA Hourly Continuation — OP/USDT P12_200

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9549 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -1.5232 |
| sortino_ratio | -0.3459 |
| max_drawdown | 0.3468 |
| cagr | -0.1533 |
| net_avg_win | 75.0006 |
| net_avg_loss | -97.6883 |
| avg_hold_time_bars | 66.7985 |
| exposure | 0.7985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
