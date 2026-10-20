# EMA Hourly Continuation — AGLD/USDT P34_100

**Symbol:** AGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.6198 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.9356 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -4.3721 |
| sortino_ratio | -1.5748 |
| max_drawdown | 0.8585 |
| cagr | -0.5285 |
| net_avg_win | 45.7288 |
| net_avg_loss | -62.9721 |
| avg_hold_time_bars | 9.8663 |
| exposure | 0.2938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
