# EMA Hourly Continuation — PROM/USDT P21_89

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.5076 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.8967 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -6.1374 |
| sortino_ratio | -2.3213 |
| max_drawdown | 0.9452 |
| cagr | -0.6837 |
| net_avg_win | 30.1396 |
| net_avg_loss | -46.1054 |
| avg_hold_time_bars | 11.0108 |
| exposure | 0.3699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
