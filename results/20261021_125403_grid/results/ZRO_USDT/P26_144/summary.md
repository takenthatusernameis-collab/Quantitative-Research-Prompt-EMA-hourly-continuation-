# EMA Hourly Continuation — ZRO/USDT P26_144

**Symbol:** ZRO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7566 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8806 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -1.6997 |
| sortino_ratio | -0.4687 |
| max_drawdown | 0.4255 |
| cagr | -0.1952 |
| net_avg_win | 75.3098 |
| net_avg_loss | -87.7630 |
| avg_hold_time_bars | 27.4086 |
| exposure | 0.4695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
