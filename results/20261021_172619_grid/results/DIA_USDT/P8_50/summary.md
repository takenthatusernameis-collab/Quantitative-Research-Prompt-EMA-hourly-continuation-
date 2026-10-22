# EMA Hourly Continuation — DIA/USDT P8_50

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.7140 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9191 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -2.9471 |
| sortino_ratio | -1.1408 |
| max_drawdown | 0.7554 |
| cagr | -0.4083 |
| net_avg_win | 51.6028 |
| net_avg_loss | -66.6441 |
| avg_hold_time_bars | 12.4189 |
| exposure | 0.4159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
