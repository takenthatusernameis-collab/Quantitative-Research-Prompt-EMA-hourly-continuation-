# EMA Hourly Continuation — MLK/USDT P89_100

**Symbol:** MLK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 804 |
| net_profit_factor | 0.1413 |
| net_win_rate | 0.1990 |
| gross_profit_factor | 0.3998 |
| gross_win_rate | 0.2264 |
| sharpe_ratio | -16.3581 |
| sortino_ratio | -7.1111 |
| max_drawdown | 1.0000 |
| cagr | -0.9809 |
| net_avg_win | 10.2821 |
| net_avg_loss | -18.0818 |
| avg_hold_time_bars | 2.3209 |
| exposure | 0.0844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
