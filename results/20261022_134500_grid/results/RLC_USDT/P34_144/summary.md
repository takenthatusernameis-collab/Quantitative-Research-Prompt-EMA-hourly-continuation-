# EMA Hourly Continuation — RLC/USDT P34_144

**Symbol:** RLC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.5804 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8561 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -3.9401 |
| sortino_ratio | -1.2697 |
| max_drawdown | 0.7898 |
| cagr | -0.4565 |
| net_avg_win | 45.1664 |
| net_avg_loss | -65.5353 |
| avg_hold_time_bars | 16.9333 |
| exposure | 0.4041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
