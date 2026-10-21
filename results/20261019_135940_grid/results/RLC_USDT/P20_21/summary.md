# EMA Hourly Continuation — RLC/USDT P20_21

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1179 |
| net_profit_factor | 0.1812 |
| net_win_rate | 0.3215 |
| gross_profit_factor | 0.7906 |
| gross_win_rate | 0.4334 |
| sharpe_ratio | -16.3792 |
| sortino_ratio | -8.4473 |
| max_drawdown | 1.0000 |
| cagr | -0.9903 |
| net_avg_win | 5.8393 |
| net_avg_loss | -15.2663 |
| avg_hold_time_bars | 1.9796 |
| exposure | 0.1061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
