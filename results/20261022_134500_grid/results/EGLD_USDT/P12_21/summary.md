# EMA Hourly Continuation — EGLD/USDT P12_21

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1461 |
| net_profit_factor | 0.2996 |
| net_win_rate | 0.4018 |
| gross_profit_factor | 0.9760 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -13.4927 |
| sortino_ratio | -7.3823 |
| max_drawdown | 0.9999 |
| cagr | -0.9771 |
| net_avg_win | 7.2878 |
| net_avg_loss | -16.3354 |
| avg_hold_time_bars | 2.3970 |
| exposure | 0.1592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
