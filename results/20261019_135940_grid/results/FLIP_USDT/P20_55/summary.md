# EMA Hourly Continuation — FLIP/USDT P20_55

**Symbol:** FLIP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.4250 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.8049 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -7.0088 |
| sortino_ratio | -2.4864 |
| max_drawdown | 0.9594 |
| cagr | -0.7174 |
| net_avg_win | 26.7236 |
| net_avg_loss | -44.1993 |
| avg_hold_time_bars | 10.1340 |
| exposure | 0.2957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
