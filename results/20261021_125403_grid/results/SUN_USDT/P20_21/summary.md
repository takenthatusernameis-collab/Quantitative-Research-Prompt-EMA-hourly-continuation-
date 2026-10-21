# EMA Hourly Continuation — SUN/USDT P20_21

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.2840 |
| net_win_rate | 0.3624 |
| gross_profit_factor | 0.7367 |
| gross_win_rate | 0.4007 |
| sharpe_ratio | -6.8738 |
| sortino_ratio | -1.7248 |
| max_drawdown | 0.8904 |
| cagr | -0.5838 |
| net_avg_win | 33.9582 |
| net_avg_loss | -67.9551 |
| avg_hold_time_bars | 5.4878 |
| exposure | 0.0713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
