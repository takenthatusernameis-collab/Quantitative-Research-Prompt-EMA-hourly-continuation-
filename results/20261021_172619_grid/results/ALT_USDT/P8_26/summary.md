# EMA Hourly Continuation — ALT/USDT P8_26

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.6610 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -3.8679 |
| sortino_ratio | -1.5455 |
| max_drawdown | 0.8461 |
| cagr | -0.5088 |
| net_avg_win | 44.3373 |
| net_avg_loss | -58.3134 |
| avg_hold_time_bars | 7.1410 |
| exposure | 0.2555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
