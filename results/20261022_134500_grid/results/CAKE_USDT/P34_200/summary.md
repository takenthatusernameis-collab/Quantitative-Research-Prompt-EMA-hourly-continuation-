# EMA Hourly Continuation — CAKE/USDT P34_200

**Symbol:** CAKE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.5796 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8971 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -3.2104 |
| sortino_ratio | -0.8447 |
| max_drawdown | 0.6738 |
| cagr | -0.3362 |
| net_avg_win | 53.6900 |
| net_avg_loss | -81.7412 |
| avg_hold_time_bars | 29.7301 |
| exposure | 0.4757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
