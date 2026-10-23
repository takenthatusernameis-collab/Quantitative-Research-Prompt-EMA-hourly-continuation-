# EMA Hourly Continuation — UMA/USDT P89_200

**Symbol:** UMA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.4933 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.7850 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -4.3488 |
| sortino_ratio | -1.2774 |
| max_drawdown | 0.7875 |
| cagr | -0.4565 |
| net_avg_win | 39.9468 |
| net_avg_loss | -64.1809 |
| avg_hold_time_bars | 10.8241 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
