# EMA Hourly Continuation — WOO/USDT P55_100

**Symbol:** WOO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.5569 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.9120 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -5.1754 |
| sortino_ratio | -1.7514 |
| max_drawdown | 0.8882 |
| cagr | -0.5724 |
| net_avg_win | 43.1208 |
| net_avg_loss | -62.5723 |
| avg_hold_time_bars | 6.1270 |
| exposure | 0.1601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
