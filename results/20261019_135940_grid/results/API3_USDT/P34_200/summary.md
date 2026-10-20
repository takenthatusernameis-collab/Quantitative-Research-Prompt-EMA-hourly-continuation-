# EMA Hourly Continuation — API3/USDT P34_200

**Symbol:** API3/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7426 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 1.0076 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0726 |
| sortino_ratio | -0.5923 |
| max_drawdown | 0.5754 |
| cagr | -0.2458 |
| net_avg_win | 72.4885 |
| net_avg_loss | -93.8954 |
| avg_hold_time_bars | 27.5728 |
| exposure | 0.5164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
