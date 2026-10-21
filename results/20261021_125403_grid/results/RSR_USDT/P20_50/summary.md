# EMA Hourly Continuation — RSR/USDT P20_50

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.8121 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0361 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -1.4968 |
| sortino_ratio | -0.4794 |
| max_drawdown | 0.4857 |
| cagr | -0.1989 |
| net_avg_win | 72.9707 |
| net_avg_loss | -93.1652 |
| avg_hold_time_bars | 8.0362 |
| exposure | 0.1815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
