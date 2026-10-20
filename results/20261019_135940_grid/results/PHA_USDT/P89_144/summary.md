# EMA Hourly Continuation — PHA/USDT P89_144

**Symbol:** PHA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.4813 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8253 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -4.4159 |
| sortino_ratio | -1.3987 |
| max_drawdown | 0.8323 |
| cagr | -0.4921 |
| net_avg_win | 32.8414 |
| net_avg_loss | -56.9021 |
| avg_hold_time_bars | 5.0669 |
| exposure | 0.1170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
