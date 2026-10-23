# EMA Hourly Continuation — FLIP/USDT P34_50

**Symbol:** FLIP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.3123 |
| net_win_rate | 0.3406 |
| gross_profit_factor | 0.7577 |
| gross_win_rate | 0.4013 |
| sharpe_ratio | -9.9533 |
| sortino_ratio | -3.5069 |
| max_drawdown | 0.9910 |
| cagr | -0.8444 |
| net_avg_win | 22.2743 |
| net_avg_loss | -36.8438 |
| avg_hold_time_bars | 5.4469 |
| exposure | 0.1468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
