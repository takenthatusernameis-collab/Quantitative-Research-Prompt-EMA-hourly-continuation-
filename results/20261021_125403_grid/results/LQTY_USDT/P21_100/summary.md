# EMA Hourly Continuation — LQTY/USDT P21_100

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6990 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.8693 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -2.3568 |
| sortino_ratio | -0.7393 |
| max_drawdown | 0.5944 |
| cagr | -0.2887 |
| net_avg_win | 58.1960 |
| net_avg_loss | -74.2250 |
| avg_hold_time_bars | 19.6680 |
| exposure | 0.4343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
