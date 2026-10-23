# EMA Hourly Continuation — PROM/USDT P21_34

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1142 |
| net_profit_factor | 0.3454 |
| net_win_rate | 0.3914 |
| gross_profit_factor | 0.7999 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -11.6631 |
| sortino_ratio | -5.6034 |
| max_drawdown | 0.9993 |
| cagr | -0.9454 |
| net_avg_win | 11.7989 |
| net_avg_loss | -21.9674 |
| avg_hold_time_bars | 3.0517 |
| exposure | 0.1584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
