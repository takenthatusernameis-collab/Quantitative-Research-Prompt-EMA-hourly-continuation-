# EMA Hourly Continuation — TRAC/USDT P20_34

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.3704 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.7970 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -8.9069 |
| sortino_ratio | -3.7985 |
| max_drawdown | 0.9930 |
| cagr | -0.8587 |
| net_avg_win | 14.8211 |
| net_avg_loss | -29.7474 |
| avg_hold_time_bars | 4.3626 |
| exposure | 0.1832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
