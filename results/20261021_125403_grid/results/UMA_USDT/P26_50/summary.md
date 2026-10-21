# EMA Hourly Continuation — UMA/USDT P26_50

**Symbol:** UMA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7072 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 1.0213 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -2.6880 |
| sortino_ratio | -0.8561 |
| max_drawdown | 0.6382 |
| cagr | -0.3251 |
| net_avg_win | 61.6146 |
| net_avg_loss | -86.7708 |
| avg_hold_time_bars | 7.1217 |
| exposure | 0.1596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
