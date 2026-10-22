# EMA Hourly Continuation — TRAC/USDT P26_200

**Symbol:** TRAC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6905 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -2.3702 |
| sortino_ratio | -0.6613 |
| max_drawdown | 0.5566 |
| cagr | -0.2637 |
| net_avg_win | 66.1084 |
| net_avg_loss | -84.1256 |
| avg_hold_time_bars | 32.0155 |
| exposure | 0.5632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
