# EMA Hourly Continuation — XAI/USDT P34_50

**Symbol:** XAI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.6525 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9021 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -2.6726 |
| sortino_ratio | -0.7115 |
| max_drawdown | 0.5799 |
| cagr | -0.2780 |
| net_avg_win | 64.3448 |
| net_avg_loss | -87.3633 |
| avg_hold_time_bars | 4.9251 |
| exposure | 0.0777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
