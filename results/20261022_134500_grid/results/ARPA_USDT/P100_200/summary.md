# EMA Hourly Continuation — ARPA/USDT P100_200

**Symbol:** ARPA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.4764 |
| net_win_rate | 0.4115 |
| gross_profit_factor | 0.7685 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -5.2466 |
| sortino_ratio | -1.5692 |
| max_drawdown | 0.8549 |
| cagr | -0.5332 |
| net_avg_win | 41.7516 |
| net_avg_loss | -61.2882 |
| avg_hold_time_bars | 9.4049 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
