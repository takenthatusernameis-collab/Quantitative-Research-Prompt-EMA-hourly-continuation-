# EMA Hourly Continuation — XPR/USDT P8_55

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9642 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -2.1590 |
| sortino_ratio | -0.7311 |
| max_drawdown | 0.6018 |
| cagr | -0.2845 |
| net_avg_win | 64.9809 |
| net_avg_loss | -82.3651 |
| avg_hold_time_bars | 15.4581 |
| exposure | 0.3942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
