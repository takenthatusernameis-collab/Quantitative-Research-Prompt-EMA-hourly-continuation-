# EMA Hourly Continuation — METIS/USDT P21_26

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1216 |
| net_profit_factor | 0.2402 |
| net_win_rate | 0.3528 |
| gross_profit_factor | 0.8177 |
| gross_win_rate | 0.4046 |
| sharpe_ratio | -14.5062 |
| sortino_ratio | -7.3638 |
| max_drawdown | 0.9999 |
| cagr | -0.9792 |
| net_avg_win | 7.3673 |
| net_avg_loss | -16.7217 |
| avg_hold_time_bars | 1.9350 |
| exposure | 0.1070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
