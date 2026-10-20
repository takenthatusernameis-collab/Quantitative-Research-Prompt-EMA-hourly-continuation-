# EMA Hourly Continuation — SLP/USDT P26_100

**Symbol:** SLP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.6366 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9958 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -4.4147 |
| sortino_ratio | -1.6745 |
| max_drawdown | 0.8735 |
| cagr | -0.5558 |
| net_avg_win | 43.9145 |
| net_avg_loss | -62.6582 |
| avg_hold_time_bars | 10.9040 |
| exposure | 0.3613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
