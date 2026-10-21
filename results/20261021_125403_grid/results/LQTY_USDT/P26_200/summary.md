# EMA Hourly Continuation — LQTY/USDT P26_200

**Symbol:** LQTY/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7152 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8653 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -1.6769 |
| sortino_ratio | -0.4277 |
| max_drawdown | 0.4238 |
| cagr | -0.1790 |
| net_avg_win | 64.3390 |
| net_avg_loss | -80.9667 |
| avg_hold_time_bars | 39.5232 |
| exposure | 0.5777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
