# EMA Hourly Continuation — ONE/USDT P8_100

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.7143 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -3.2141 |
| sortino_ratio | -1.1198 |
| max_drawdown | 0.7562 |
| cagr | -0.4111 |
| net_avg_win | 63.1799 |
| net_avg_loss | -81.1998 |
| avg_hold_time_bars | 25.3388 |
| exposure | 0.7003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
