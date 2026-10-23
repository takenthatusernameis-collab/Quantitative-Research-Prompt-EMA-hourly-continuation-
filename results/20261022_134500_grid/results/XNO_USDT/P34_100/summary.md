# EMA Hourly Continuation — XNO/USDT P34_100

**Symbol:** XNO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.5208 |
| net_win_rate | 0.4091 |
| gross_profit_factor | 0.8197 |
| gross_win_rate | 0.4153 |
| sharpe_ratio | -7.2050 |
| sortino_ratio | -2.9010 |
| max_drawdown | 0.9699 |
| cagr | -0.7503 |
| net_avg_win | 31.8239 |
| net_avg_loss | -42.3157 |
| avg_hold_time_bars | 7.1248 |
| exposure | 0.2620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
