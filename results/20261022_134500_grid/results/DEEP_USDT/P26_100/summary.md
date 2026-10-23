# EMA Hourly Continuation — DEEP/USDT P26_100

**Symbol:** DEEP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.8235 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0829 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -1.5058 |
| sortino_ratio | -0.5163 |
| max_drawdown | 0.4238 |
| cagr | -0.2148 |
| net_avg_win | 75.3588 |
| net_avg_loss | -98.5134 |
| avg_hold_time_bars | 13.6334 |
| exposure | 0.3558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
