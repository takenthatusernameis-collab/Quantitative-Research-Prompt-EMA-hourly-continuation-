# EMA Hourly Continuation — REQ/USDT P89_100

**Symbol:** REQ/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 192 |
| net_profit_factor | 0.3668 |
| net_win_rate | 0.3854 |
| gross_profit_factor | 0.6568 |
| gross_win_rate | 0.3854 |
| sharpe_ratio | -4.3847 |
| sortino_ratio | -0.8801 |
| max_drawdown | 0.6464 |
| cagr | -0.3390 |
| net_avg_win | 50.6123 |
| net_avg_loss | -86.5207 |
| avg_hold_time_bars | 5.8281 |
| exposure | 0.0509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
