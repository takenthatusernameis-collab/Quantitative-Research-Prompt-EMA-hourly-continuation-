# EMA Hourly Continuation — AAVE/USDT P21_100

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5900 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -3.8736 |
| sortino_ratio | -1.3705 |
| max_drawdown | 0.8286 |
| cagr | -0.4833 |
| net_avg_win | 38.3177 |
| net_avg_loss | -59.8303 |
| avg_hold_time_bars | 13.7965 |
| exposure | 0.3976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
