# EMA Hourly Continuation — GTC/USDT P21_100

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.5809 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8465 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -4.2114 |
| sortino_ratio | -1.5250 |
| max_drawdown | 0.8398 |
| cagr | -0.5138 |
| net_avg_win | 38.6544 |
| net_avg_loss | -55.4475 |
| avg_hold_time_bars | 13.3439 |
| exposure | 0.4003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
