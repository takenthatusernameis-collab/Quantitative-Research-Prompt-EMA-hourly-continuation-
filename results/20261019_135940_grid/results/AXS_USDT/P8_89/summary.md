# EMA Hourly Continuation — AXS/USDT P8_89

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.6473 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9689 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -3.8814 |
| sortino_ratio | -1.4037 |
| max_drawdown | 0.8300 |
| cagr | -0.4962 |
| net_avg_win | 46.8864 |
| net_avg_loss | -66.6389 |
| avg_hold_time_bars | 21.1815 |
| exposure | 0.6441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
