# EMA Hourly Continuation — TRB/USDT P26_100

**Symbol:** TRB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.5093 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.8390 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -5.2529 |
| sortino_ratio | -1.8990 |
| max_drawdown | 0.9002 |
| cagr | -0.5969 |
| net_avg_win | 31.6256 |
| net_avg_loss | -50.4657 |
| avg_hold_time_bars | 12.7644 |
| exposure | 0.3801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
