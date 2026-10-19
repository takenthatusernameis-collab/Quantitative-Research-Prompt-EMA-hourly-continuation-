# EMA Hourly Continuation — SUI/USDT P20_55

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 972 |
| net_profit_factor | 0.5964 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -7.0119 |
| sortino_ratio | -3.0453 |
| max_drawdown | 0.9805 |
| cagr | -0.7841 |
| net_avg_win | 32.7178 |
| net_avg_loss | -45.7516 |
| avg_hold_time_bars | 5.4938 |
| exposure | 0.2427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
