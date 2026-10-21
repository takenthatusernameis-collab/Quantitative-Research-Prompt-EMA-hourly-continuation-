# EMA Hourly Continuation — CATI/USDT P34_89

**Symbol:** CATI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.6302 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.7948 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -2.8399 |
| sortino_ratio | -0.7945 |
| max_drawdown | 0.5570 |
| cagr | -0.3075 |
| net_avg_win | 63.2816 |
| net_avg_loss | -80.7810 |
| avg_hold_time_bars | 13.7523 |
| exposure | 0.2435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
