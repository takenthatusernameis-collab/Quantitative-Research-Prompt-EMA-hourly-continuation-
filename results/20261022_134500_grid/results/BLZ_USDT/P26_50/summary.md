# EMA Hourly Continuation — BLZ/USDT P26_50

**Symbol:** BLZ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.4270 |
| net_win_rate | 0.3908 |
| gross_profit_factor | 0.7933 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -9.6507 |
| sortino_ratio | -4.3083 |
| max_drawdown | 0.9952 |
| cagr | -0.8795 |
| net_avg_win | 19.0164 |
| net_avg_loss | -28.5664 |
| avg_hold_time_bars | 4.4399 |
| exposure | 0.2005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
