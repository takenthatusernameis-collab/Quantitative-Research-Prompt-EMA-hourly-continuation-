# EMA Hourly Continuation — ATH/USDT P34_55

**Symbol:** ATH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 839 |
| net_profit_factor | 0.4554 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8714 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -6.7640 |
| sortino_ratio | -2.8414 |
| max_drawdown | 0.9651 |
| cagr | -0.7578 |
| net_avg_win | 20.6276 |
| net_avg_loss | -39.5334 |
| avg_hold_time_bars | 2.8713 |
| exposure | 0.1168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
