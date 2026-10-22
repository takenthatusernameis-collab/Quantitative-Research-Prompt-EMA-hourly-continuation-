# EMA Hourly Continuation — TRAC/USDT P20_26

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.2546 |
| net_win_rate | 0.3660 |
| gross_profit_factor | 0.7212 |
| gross_win_rate | 0.4144 |
| sharpe_ratio | -12.0231 |
| sortino_ratio | -5.3578 |
| max_drawdown | 0.9993 |
| cagr | -0.9433 |
| net_avg_win | 9.6166 |
| net_avg_loss | -21.7992 |
| avg_hold_time_bars | 3.3897 |
| exposure | 0.1495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
