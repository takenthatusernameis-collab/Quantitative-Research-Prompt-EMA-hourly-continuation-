# EMA Hourly Continuation — YFI/USDT P8_21

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1736 |
| net_profit_factor | 0.2599 |
| net_win_rate | 0.4032 |
| gross_profit_factor | 0.7858 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -14.7284 |
| sortino_ratio | -8.7602 |
| max_drawdown | 1.0000 |
| cagr | -0.9883 |
| net_avg_win | 5.0156 |
| net_avg_loss | -13.0413 |
| avg_hold_time_bars | 3.3687 |
| exposure | 0.2646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
