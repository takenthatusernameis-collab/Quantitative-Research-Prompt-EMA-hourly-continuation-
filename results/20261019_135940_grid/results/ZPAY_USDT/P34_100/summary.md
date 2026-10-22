# EMA Hourly Continuation — ZPAY/USDT P34_100

**Symbol:** ZPAY/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.4443 |
| net_win_rate | 0.3405 |
| gross_profit_factor | 0.5910 |
| gross_win_rate | 0.3455 |
| sharpe_ratio | -6.7215 |
| sortino_ratio | -2.3068 |
| max_drawdown | 0.9393 |
| cagr | -0.6643 |
| net_avg_win | 36.3377 |
| net_avg_loss | -42.2273 |
| avg_hold_time_bars | 13.9719 |
| exposure | 0.3825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
