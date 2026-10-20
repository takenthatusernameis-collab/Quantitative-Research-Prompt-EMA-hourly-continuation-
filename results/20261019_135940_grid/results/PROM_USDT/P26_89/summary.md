# EMA Hourly Continuation — PROM/USDT P26_89

**Symbol:** PROM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.4879 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -6.4198 |
| sortino_ratio | -2.4216 |
| max_drawdown | 0.9521 |
| cagr | -0.7001 |
| net_avg_win | 28.6818 |
| net_avg_loss | -44.7650 |
| avg_hold_time_bars | 9.5007 |
| exposure | 0.3157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
