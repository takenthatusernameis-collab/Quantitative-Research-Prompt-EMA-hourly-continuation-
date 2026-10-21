# EMA Hourly Continuation — DGB/USDT P21_26

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 160 |
| net_profit_factor | 0.5814 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.8078 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -2.1526 |
| sortino_ratio | -0.3883 |
| max_drawdown | 0.4014 |
| cagr | -0.1640 |
| net_avg_win | 70.8640 |
| net_avg_loss | -97.2422 |
| avg_hold_time_bars | 6.6562 |
| exposure | 0.0484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
