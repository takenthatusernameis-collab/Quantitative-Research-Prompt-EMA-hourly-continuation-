# EMA Hourly Continuation — DASH/USDT P20_200

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.7026 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -1.8116 |
| sortino_ratio | -0.4363 |
| max_drawdown | 0.4257 |
| cagr | -0.1827 |
| net_avg_win | 69.5648 |
| net_avg_loss | -87.3605 |
| avg_hold_time_bars | 46.3715 |
| exposure | 0.6070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
