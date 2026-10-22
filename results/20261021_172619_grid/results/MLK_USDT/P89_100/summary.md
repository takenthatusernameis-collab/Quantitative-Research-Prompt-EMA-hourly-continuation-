# EMA Hourly Continuation — MLK/USDT P89_100

**Symbol:** MLK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 141 |
| net_profit_factor | 0.2445 |
| net_win_rate | 0.2766 |
| gross_profit_factor | 0.3956 |
| gross_win_rate | 0.2837 |
| sharpe_ratio | -4.7079 |
| sortino_ratio | -0.7989 |
| max_drawdown | 0.6282 |
| cagr | -0.3201 |
| net_avg_win | 51.6390 |
| net_avg_loss | -80.7385 |
| avg_hold_time_bars | 5.7305 |
| exposure | 0.0366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
