# EMA Hourly Continuation — TRAC/USDT P26_55

**Symbol:** TRAC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.4598 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8464 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -6.6231 |
| sortino_ratio | -2.6219 |
| max_drawdown | 0.9605 |
| cagr | -0.7210 |
| net_avg_win | 23.6725 |
| net_avg_loss | -40.1851 |
| avg_hold_time_bars | 5.8234 |
| exposure | 0.2083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
