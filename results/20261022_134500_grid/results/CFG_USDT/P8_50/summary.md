# EMA Hourly Continuation — CFG/USDT P8_50

**Symbol:** CFG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.4980 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.8048 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -5.7284 |
| sortino_ratio | -2.4726 |
| max_drawdown | 0.9514 |
| cagr | -0.6953 |
| net_avg_win | 22.2169 |
| net_avg_loss | -36.0964 |
| avg_hold_time_bars | 13.0981 |
| exposure | 0.5644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
