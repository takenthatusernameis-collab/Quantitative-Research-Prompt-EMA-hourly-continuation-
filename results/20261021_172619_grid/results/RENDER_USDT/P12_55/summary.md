# EMA Hourly Continuation — RENDER/USDT P12_55

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.8177 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0248 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -1.5290 |
| sortino_ratio | -0.5657 |
| max_drawdown | 0.4830 |
| cagr | -0.2316 |
| net_avg_win | 66.4718 |
| net_avg_loss | -85.0697 |
| avg_hold_time_bars | 9.7435 |
| exposure | 0.2947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
