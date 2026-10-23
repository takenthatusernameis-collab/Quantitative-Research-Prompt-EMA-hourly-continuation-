# EMA Hourly Continuation — ZIL/USDT P26_100

**Symbol:** ZIL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6010 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 1.0092 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -4.3002 |
| sortino_ratio | -1.5623 |
| max_drawdown | 0.8659 |
| cagr | -0.5304 |
| net_avg_win | 39.6400 |
| net_avg_loss | -61.9333 |
| avg_hold_time_bars | 11.2324 |
| exposure | 0.3405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
