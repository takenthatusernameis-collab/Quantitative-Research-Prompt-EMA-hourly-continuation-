# EMA Hourly Continuation — KMNO/USDT P21_26

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.7847 |
| net_win_rate | 0.5410 |
| gross_profit_factor | 1.1923 |
| gross_win_rate | 0.5464 |
| sharpe_ratio | -0.9957 |
| sortino_ratio | -0.1958 |
| max_drawdown | 0.2254 |
| cagr | -0.0864 |
| net_avg_win | 73.7540 |
| net_avg_loss | -110.7698 |
| avg_hold_time_bars | 4.7049 |
| exposure | 0.0398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
