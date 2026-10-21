# EMA Hourly Continuation — AGLD/USDT P50_100

**Symbol:** AGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6275 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -3.2901 |
| sortino_ratio | -1.0189 |
| max_drawdown | 0.7071 |
| cagr | -0.3736 |
| net_avg_win | 53.7855 |
| net_avg_loss | -72.0875 |
| avg_hold_time_bars | 7.7979 |
| exposure | 0.1676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
