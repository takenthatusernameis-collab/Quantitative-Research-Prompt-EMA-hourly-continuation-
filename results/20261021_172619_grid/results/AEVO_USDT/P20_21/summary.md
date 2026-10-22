# EMA Hourly Continuation — AEVO/USDT P20_21

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.5133 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.7368 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -3.1173 |
| sortino_ratio | -0.6715 |
| max_drawdown | 0.5653 |
| cagr | -0.2658 |
| net_avg_win | 58.2579 |
| net_avg_loss | -84.9012 |
| avg_hold_time_bars | 4.4585 |
| exposure | 0.0462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
