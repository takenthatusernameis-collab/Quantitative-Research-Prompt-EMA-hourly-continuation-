# EMA Hourly Continuation — PHA/USDT P26_144

**Symbol:** PHA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.5587 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.7866 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -3.8765 |
| sortino_ratio | -1.2659 |
| max_drawdown | 0.7813 |
| cagr | -0.4520 |
| net_avg_win | 41.1081 |
| net_avg_loss | -58.6640 |
| avg_hold_time_bars | 18.0518 |
| exposure | 0.4439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
