# EMA Hourly Continuation — XPR/USDT P8_50

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.7536 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9663 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.2320 |
| sortino_ratio | -0.7649 |
| max_drawdown | 0.6169 |
| cagr | -0.2956 |
| net_avg_win | 63.4814 |
| net_avg_loss | -81.3496 |
| avg_hold_time_bars | 13.8641 |
| exposure | 0.3617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
