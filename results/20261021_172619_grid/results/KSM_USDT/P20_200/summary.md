# EMA Hourly Continuation — KSM/USDT P20_200

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.8120 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9989 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.1346 |
| sortino_ratio | -0.2754 |
| max_drawdown | 0.3729 |
| cagr | -0.1204 |
| net_avg_win | 82.0503 |
| net_avg_loss | -101.7463 |
| avg_hold_time_bars | 49.7889 |
| exposure | 0.6540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
