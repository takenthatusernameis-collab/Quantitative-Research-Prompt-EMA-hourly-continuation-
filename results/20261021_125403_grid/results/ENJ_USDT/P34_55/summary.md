# EMA Hourly Continuation — ENJ/USDT P34_55

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0423 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -1.7965 |
| sortino_ratio | -0.4882 |
| max_drawdown | 0.4744 |
| cagr | -0.2006 |
| net_avg_win | 66.8043 |
| net_avg_loss | -93.9803 |
| avg_hold_time_bars | 5.1365 |
| exposure | 0.0834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
