# EMA Hourly Continuation — YGG/USDT P21_26

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.6063 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8675 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -2.6386 |
| sortino_ratio | -0.5939 |
| max_drawdown | 0.5240 |
| cagr | -0.2378 |
| net_avg_win | 67.5983 |
| net_avg_loss | -92.6319 |
| avg_hold_time_bars | 3.9839 |
| exposure | 0.0449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
