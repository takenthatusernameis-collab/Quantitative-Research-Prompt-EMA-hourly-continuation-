# EMA Hourly Continuation — DASH/USDT P55_100

**Symbol:** DASH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7038 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9659 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -1.9461 |
| sortino_ratio | -0.4987 |
| max_drawdown | 0.4573 |
| cagr | -0.2043 |
| net_avg_win | 66.0754 |
| net_avg_loss | -90.4325 |
| avg_hold_time_bars | 7.8125 |
| exposure | 0.1136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
