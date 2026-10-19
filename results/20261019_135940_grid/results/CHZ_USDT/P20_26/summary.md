# EMA Hourly Continuation — CHZ/USDT P20_26

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1246 |
| net_profit_factor | 0.2431 |
| net_win_rate | 0.3571 |
| gross_profit_factor | 0.7662 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -14.5626 |
| sortino_ratio | -7.4734 |
| max_drawdown | 0.9999 |
| cagr | -0.9802 |
| net_avg_win | 7.2174 |
| net_avg_loss | -16.4934 |
| avg_hold_time_bars | 1.9663 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
