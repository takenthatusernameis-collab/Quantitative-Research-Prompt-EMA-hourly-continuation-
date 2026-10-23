# EMA Hourly Continuation — G/USDT P26_89

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.5472 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.8674 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -5.2665 |
| sortino_ratio | -1.9002 |
| max_drawdown | 0.8713 |
| cagr | -0.6008 |
| net_avg_win | 41.2542 |
| net_avg_loss | -60.1747 |
| avg_hold_time_bars | 11.8895 |
| exposure | 0.3563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
