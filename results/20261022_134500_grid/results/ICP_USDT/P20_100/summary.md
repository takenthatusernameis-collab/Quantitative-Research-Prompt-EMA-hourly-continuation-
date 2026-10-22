# EMA Hourly Continuation — ICP/USDT P20_100

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.6173 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -4.3675 |
| sortino_ratio | -1.6528 |
| max_drawdown | 0.8745 |
| cagr | -0.5516 |
| net_avg_win | 39.9439 |
| net_avg_loss | -59.7518 |
| avg_hold_time_bars | 12.2497 |
| exposure | 0.4059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
